package api

import (
	"log"
	"net/http"

	"github.com/dgrijalva/jwt-go"
	"github.com/n0bode/desafio-backend/auth"
	"github.com/n0bode/desafio-backend/database"
	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"

	"github.com/go-pg/pg"

	"github.com/go-chi/chi"
	"github.com/go-chi/render"
)

type Api struct {
	auth *auth.TokenAuth
	db   *pg.DB
}

func (api *Api) routeCreateAccount(w http.ResponseWriter, r *http.Request) {
	//Set Content-Type application/json
	util.SetHeaderJson(w)

	resp := make(map[string]interface{})
	resp["message"] = ""

	defer func() {
		render.JSON(w, r, resp)
		r.Body.Close()
	}()

	var account models.Account
	if err := render.DecodeJSON(r.Body, &account); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "content invalid"
		return
	}

	/*
		while is a big void inside here
	*/
	inserted, err := api.db.Model(&account).Where("username = ?", account.Username).SelectOrInsert()

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		log.Println("Error to insert account into database")
		resp["message"] = "try again later"
		return
	}

	if !inserted {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "username already exists"
		return
	}

	//Creating token for authentication(JWT)
	tokenStr, err := api.auth.CreateToken(jwt.MapClaims{
		"user_id": account.UserID,
	})

	//Error to create token(JWT)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		resp["message"] = "cannot create authentication"
		return
	}

	//Return StatusCreated and Token(JWT)
	w.WriteHeader(http.StatusCreated)
	resp["data"] = map[string]interface{}{
		"token": tokenStr,
	}
}

func (api *Api) routeCreateCard(w http.ResponseWriter, r *http.Request) {

}

func (api *Api) restrictRoutes(route chi.Router) {
	//Middleware token(JWT) is valid
	route.Use(api.auth.Verifier)
	route.Use(api.auth.Authorization)

	//Route POST create card
	route.Post("/card", api.routeCreateCard)
}

func (api *Api) Route() *chi.Mux {
	route := chi.NewRouter()

	//Set header to accept Json content
	//route.Use(util.SetContentJSON)

	//Create routes
	route.Mount("/account", route.Group(func(r chi.Router) {
		//Accept Json, this method makes route accept only json content as body
		r.Post("/person", util.AcceptJson(api.routeCreateAccount))

		//Restrict Area only to be access with JWT
		r.Group(api.restrictRoutes)
	}))
	return route
}

func New() *Api {
	return &Api{
		auth: auth.New("Hello WorldNONU"),
		db:   database.New(),
	}
}
