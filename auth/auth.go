package auth

import (
	"context"
	"net/http"
	"time"

	"github.com/dgrijalva/jwt-go"

	"github.com/go-chi/jwtauth"
)

type TokenAuth struct {
	auth    *jwtauth.JWTAuth
	expire  time.Duration
	refresh time.Duration
}

func (t *TokenAuth) Authorization(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		token, _, err := jwtauth.FromContext(r.Context())
		if err != nil {
			http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
			return
		}

		if !token.Valid {
			http.Error(w, http.StatusText(http.StatusUnauthorized), http.StatusUnauthorized)
			return
		}

		next.ServeHTTP(w, r)
	})
}

func (t *TokenAuth) Verifier(next http.Handler) http.Handler {
	return jwtauth.Verifier(t.auth)(next)
}

func (t *TokenAuth) CreateToken(claims jwt.MapClaims) (tokenStr string, err error) {
	jwtauth.SetIssuedNow(claims)
	jwtauth.SetExpiryIn(claims, t.expire)
	_, tokenStr, err = t.auth.Encode(claims)
	return
}

func (t *TokenAuth) ClaimsFromContext(ctx context.Context) (claims jwt.MapClaims) {
	_, claims, _ = jwtauth.FromContext(ctx)
	return
}

func New(secret string) *TokenAuth {
	return &TokenAuth{
		auth:    jwtauth.New("HS256", []byte(secret), nil),
		expire:  time.Minute * 30,
		refresh: time.Minute * 30,
	}
}
