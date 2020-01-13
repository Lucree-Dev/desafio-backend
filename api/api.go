package api

import (
	"net/http"

	"github.com/n0bode/desafio-backend/internal/models"

	"github.com/go-chi/chi"
	"github.com/go-chi/render"
)

func routeCreateAccount(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()

	var account models.Account
	if err := render.DecodeJSON(r.Body, &account); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}
	/*

		while is a big void inside here

	*/
	w.WriteHeader(http.StatusCreated)
}

func routeFriends(w http.ResponseWriter, r *http.Request) {

}

func setContentJSON(handler http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Header().Set("Accept", "application/json")

		handler.ServeHTTP(w, r)
	})
}

func restrictRoutes(route chi.Router) {
	route.Get("/friends", routeFriends)
}

func Route() (route *chi.Mux) {
	route = chi.NewRouter()

	//Set header to accept Json content
	route.Use(setContentJSON)

	//Create routes
	route.Mount("/account", route.Group(func(r chi.Router) {
		r.Post("/person", routeCreateAccount)

		r.Group(restrictRoutes)
	}))

	return
}
