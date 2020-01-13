package api

import (
	"net/http"

	"github.com/n0bode/desafio-backend/internal/models"

	"github.com/go-chi/chi"
	"github.com/go-chi/render"
)

func createAccount(w http.ResponseWriter, r *http.Request) {
	defer r.Body.Close()

	var account models.Account
	if err := render.DecodeJSON(r.Body, &account); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	w.WriteHeader(http.StatusCreated)
	render.JSON(w, r, account)

}

func setContentJSON(handler http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Header().Set("Accept", "application/json")

		handler.ServeHTTP(w, r)
	})
}

func Route() (route *chi.Mux) {
	route = chi.NewRouter()

	//Set header accept Json content
	route.Use(setContentJSON)

	//Create route to create account
	//Public route (NO AUTHENTICATION)
	route.Post("/", createAccount)

	return
}
