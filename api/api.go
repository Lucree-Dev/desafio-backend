package api

import (
	"fmt"
	"log"
	"net/http"
	"time"

	"gopkg.in/go-playground/validator.v9"

	re "gopkg.in/rethinkdb/rethinkdb-go.v6"

	"github.com/n0bode/desafio-backend/api/bankstatement"
	"github.com/n0bode/desafio-backend/api/session"
	"github.com/n0bode/desafio-backend/auth"
	"github.com/n0bode/desafio-backend/database"
	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"

	"github.com/go-chi/chi"
	"github.com/go-chi/render"
)

type Api struct {
	auth     *auth.TokenAuth
	db       *re.Session
	validate *validator.Validate
}

func (api *Api) routePostAccount(w http.ResponseWriter, r *http.Request) {
	//Set Content-Type application/json
	util.SetHeaderJson(w)

	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)

	var account models.Account
	if err := render.DecodeJSON(r.Body, &account); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Content Invalid"
		return
	}

	if err := api.validate.Struct(&account); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Missing Fields"
		return
	}

	cursor, err := re.Table("accounts").Filter(
		re.Row.Field("username").Eq(account.Username).Or(
			re.Row.Field("user_id").Eq(account.UserID),
		),
	).Run(api.db)
	if err != nil {
		w.WriteHeader(http.StatusConflict)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	if !cursor.IsNil() {
		w.WriteHeader(http.StatusConflict)
		resp["message"] = "User already exists"
		return
	}

	account.Password = util.EncodeToSha256(account.Password)
	err = re.Table("accounts").Insert(account).Exec(api.db)
	if err != nil {
		w.WriteHeader(http.StatusConflict)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	resp["message"] = "Account created with Success"
	w.WriteHeader(http.StatusCreated)
}

func (api *Api) routePostCard(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)

	util.SetHeaderJson(w)

	var card models.CreditCard
	if err := render.DecodeJSON(r.Body, &card); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Content Invalid"
		return
	}

	//Check if creditcard has all fields necessaries
	if err := api.validate.Struct(&card); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Missing Fields"
		return
	}

	claims := api.auth.ClaimsFromContext(r.Context())
	card.UserID = claims["user_id"].(string)

	cursor, err := re.Table("creditcards").Filter(re.Row.Field("card_id").Eq(card.CardID)).Run(api.db)

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	if !cursor.IsNil() {
		w.WriteHeader(http.StatusConflict)
		resp["message"] = "Card Already Registered"
		return
	}

	info, err := re.Table("creditcards").Insert(card).RunWrite(api.db)
	if err != nil || info.Inserted == 0 {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	w.WriteHeader(http.StatusCreated)
	resp["message"] = "CreditCard Added"
}

func (api *Api) routeGetCard(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer render.JSON(w, r, resp)

	util.SetHeaderJson(w)
	claims := api.auth.ClaimsFromContext(r.Context())

	cursor, err := re.Table("creditcards").Filter(re.Row.Field("user_id").Eq(claims["user_id"])).Run(api.db)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	var cards []models.CreditCard
	cursor.All(&cards)

	w.WriteHeader(http.StatusOK)
	resp["message"] = "Success"
	resp["data"] = cards
}

func (api *Api) routeGetFriends(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)
	claims := api.auth.ClaimsFromContext(r.Context())

	//Create foreign key for RethinkDB
	cursor, err := re.Table("friends").Filter(
		re.Row.Field("user_id").Eq(claims["user_id"]).Or(
			re.Row.Field("friend_id").Eq(claims["user_id"])),
	).EqJoin(
		"friend_id", re.Table("accounts"), re.EqJoinOpts{
			Index: "user_id",
		},
	).Field("right").Without("password", "id").Run(api.db)

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	friends := make([]models.Account, 0)
	cursor.All(&friends)

	util.SetHeaderJson(w)
	w.WriteHeader(http.StatusOK)
	resp["message"] = "Success"
	resp["data"] = friends
}

func (api *Api) routePostTransfer(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)

	util.SetHeaderJson(w)

	var transfer models.Transfer
	if err := render.DecodeJSON(r.Body, &transfer); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Content Invalid"
		return
	}

	//Check if transfere has all fields
	if err := api.validate.Struct(&transfer); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Missing Fields"
		return
	}

	claims := api.auth.ClaimsFromContext(r.Context())
	transfer.UserID = claims["user_id"].(string)
	transfer.Date = time.Now().Format("MM/dd/YYYY")
	transfer.FromCard = transfer.BillingCard.CardID
	transfer.Value = transfer.TotalToPay

	cursor, err := re.Table("accounts").Filter(re.Row.Field("user_id").Eq(transfer.FriendID)).Run(api.db)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	if cursor.IsNil() {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "Friend is not exists"
		return
	}

	info, err := re.Table("transfers").Insert(transfer).RunWrite(api.db)
	if err != nil || info.Inserted == 0 {
		w.WriteHeader(http.StatusBadRequest)
		fmt.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	w.WriteHeader(http.StatusOK)
	resp["message"] = "Transfer Added"
}

func (api *Api) restrictRoutes(route chi.Router) {
	//Middleware token(JWT) is valid
	route.Use(api.auth.Verifier)
	route.Use(api.auth.Authorization)

	//Route Friends
	route.Get("/friends", api.routeGetFriends) //GET

	//Route Cards
	route.Post("/card", util.AcceptJson(api.routePostCard)) //POST
	route.Get("/cards", api.routeGetCard)                   //GET

	//Route Transfer
	route.Post("/transfer", util.AcceptJson(api.routePostTransfer))

	//Route bank-statement
	bank := bankstatement.New(api.auth, api.db)
	route.Mount("/bank-statement", bank.Route())
}

func (api *Api) Route() *chi.Mux {
	route := chi.NewRouter()
	session := session.New(api.auth, api.db)

	//Create Route to session
	route.Mount("/session", session.Route())

	//Create routes
	route.Mount("/account", route.Group(func(r chi.Router) {
		//Accept Json, this method makes route accept only json content as body
		r.Post("/person", util.AcceptJson(api.routePostAccount))
		//Restrict Area only to be access with JWT
		r.Group(api.restrictRoutes)
	}))
	return route
}

func New() *Api {
	return &Api{
		auth:     auth.New(util.GetEnv("JWT_SECRET", "SECRET01")),
		db:       database.New(),
		validate: validator.New(),
	}
}
