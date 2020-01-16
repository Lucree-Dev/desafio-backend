package session

import (
	"log"
	"net/http"

	re "gopkg.in/rethinkdb/rethinkdb-go.v6"

	"github.com/n0bode/desafio-backend/internal/util"

	"github.com/go-chi/render"

	"github.com/n0bode/desafio-backend/internal/models"

	"github.com/dgrijalva/jwt-go"
	"github.com/go-chi/chi"
	"github.com/n0bode/desafio-backend/auth"
)

type Api struct {
	auth      *auth.TokenAuth
	db        *re.Session
	blacklist map[string]bool
}

func New(auth *auth.TokenAuth, db *re.Session) (api *Api) {
	return &Api{
		auth: auth,
		db:   db,
	}
}

func (api *Api) routePostSession(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)

	var account models.Account
	if err := render.DecodeJSON(r.Body, &account); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Content Invalid"
		return
	}

	account.Password = util.EncodeToSha256(account.Password)
	cursor, err := re.Table("accounts").Filter(re.Row.Field("username").Eq(account.Username).And(re.Row.Field("password").Eq(account.Password))).Run(api.db)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	if cursor.IsNil() {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Username Not Exists"
		return
	}

	if cursor.One(&account) != nil {
		w.WriteHeader(http.StatusBadRequest)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	//Creating token for authentication(JWT)
	tokenStr, err := api.auth.CreateToken(jwt.MapClaims{
		"user_id": account.UserID,
	})

	//Error to create token(JWT)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Cannot Create Authentication"
		return
	}

	//Return StatusCreated and Token(JWT)
	resp["message"] = "Success"
	w.WriteHeader(http.StatusCreated)
	resp["data"] = map[string]interface{}{
		"token": tokenStr,
	}
}

func (api *Api) routeDeleteSession(w http.ResponseWriter, r *http.Request) {
	//Get user_id from JWTClaims
	token, err := api.auth.Token(r)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	if !token.Valid {
		return
	}
	api.auth.AddToBlackList(token)
}

func (api *Api) Route() (route *chi.Mux) {
	route = chi.NewRouter()

	//Route to access login to create an authorization
	route.Post("/", util.AcceptJson(api.routePostSession))
	route.Delete("/", api.routeDeleteSession)
	return
}
