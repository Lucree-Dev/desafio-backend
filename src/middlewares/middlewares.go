package middlewares

import (
	"log"
	"lucree/src/response"
	"lucree/src/service"
	"net/http"
)

func Log(next http.HandlerFunc) http.HandlerFunc {
	return func(rw http.ResponseWriter, r *http.Request) {
		log.Printf("\n %s %s %s", r.Method, r.RequestURI, r.Host)
		next(rw, r)
	}
}

// Authentic the user
func Authenticate(next http.HandlerFunc) http.HandlerFunc {
	return func(rw http.ResponseWriter, r *http.Request) {
		if err := service.ValidateToken(r); err != nil {
			response.Erro(rw, http.StatusUnauthorized, err)
			return
		}
		next(rw, r)
	}
}
