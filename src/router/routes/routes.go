package routes

import (
	"lucree/src/middlewares"
	"net/http"

	"github.com/gorilla/mux"
)

type Route struct {
	Url           string
	Method        string
	Function      func(http.ResponseWriter, *http.Request)
	LoginRequired bool
}

// Put all routes into the router
func Config(r *mux.Router) *mux.Router {
	routes := routerPersons
	routes = append(routes, routerLogin)
	routes = append(routes, routerCards...)
	routes = append(routes, routerTransfer...)
	for _, route := range routes {
		if route.LoginRequired {
			r.HandleFunc(route.Url, middlewares.Log(middlewares.Authenticate(route.Function))).Methods(route.Method)
		} else {
			r.HandleFunc(route.Url, middlewares.Log(route.Function)).Methods(route.Method)
		}
	}

	return r
}
