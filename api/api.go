package api

import (
	"net/http"

	"github.com/dgrijalva/jwt-go"
	"github.com/n0bode/desafio-backend/auth"
	"github.com/n0bode/desafio-backend/internal/models"

	"github.com/go-chi/chi"
	"github.com/go-chi/render"
)

type Api struct {
	auth *auth.TokenAuth
}

func (api *Api) routeCreateAccount(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()

	var account models.Account
	if err := render.DecodeJSON(r.Body, &account); err != nil {
		http.Error(w, http.StatusText(http.StatusBadRequest), http.StatusBadRequest)
		return
	}

	/*

		while is a big void inside here

	*/

	//Creating token for authentication(JWT)
	tokenStr, err := api.auth.CreateToken(jwt.MapClaims{
		"user_id": account.UserID,
	})

	//Error to create token(JWT)
	if err != nil {
		http.Error(w, http.StatusText(http.StatusBadRequest), http.StatusBadRequest)
		return
	}

	//If all is ok
	w.WriteHeader(http.StatusCreated)
	render.JSON(w, r, map[string]interface{}{
		"token": tokenStr,
	})
}

func (api *Api) restrictRoutes(route chi.Router) {
	//Check token is valid
	route.Use(api.auth.Verifier)
	route.Use(api.auth.Authorization)
}

func (api *Api) Route() *chi.Mux {
	route := chi.NewRouter()

	//Set header to accept Json content
	//route.Use(util.SetContentJSON)

	//Create routes
	route.Mount("/account", route.Group(func(r chi.Router) {
		r.Post("/person", api.routeCreateAccount)

		//Restrict Area only to be acess with JWT
		r.Group(api.restrictRoutes)
	}))
	return route
}

func New() *Api {

	return &Api{
		auth: auth.New("Hello WorldNONU"),
	}
}
