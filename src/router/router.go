package router

import (
	"lucree/src/router/routes"

	"github.com/gorilla/mux"
)

// Will return a preconfigured route
func Generate() *mux.Router {

	r := mux.NewRouter()
	return routes.Config(r)
}
