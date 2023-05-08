package auth

import (
	"context"
	"net/http"
	"strings"
)

type contextKey string

const (
	claimsContextKey contextKey = "claims"
)

func JWTMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		tokenString := strings.TrimPrefix(r.Header.Get("Authorization"), "Bearer ")

		token, err := VerifyToken(tokenString)
		if err != nil {
			w.WriteHeader(http.StatusUnauthorized)
			return
		}

		if !token.Valid {
			w.WriteHeader(http.StatusUnauthorized)
			return
		}

		ctx := context.WithValue(r.Context(), claimsContextKey, token.Claims)
		next.ServeHTTP(w, r.WithContext(ctx))
	})
}
