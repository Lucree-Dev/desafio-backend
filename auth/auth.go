package auth

import (
	"context"
	"net/http"
	"sync"
	"time"

	"github.com/go-chi/jwtauth"
	"github.com/go-chi/render"

	"github.com/dgrijalva/jwt-go"

	"github.com/n0bode/desafio-backend/internal/util"
)

type TokenAuth struct {
	auth      *jwtauth.JWTAuth
	expire    time.Duration
	refresh   time.Duration
	blacklist map[string]bool
	m         *sync.Mutex
}

func (t *TokenAuth) Authorization(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {

		token, _, err := jwtauth.FromContext(r.Context())

		if err != nil {
			util.SetHeaderJson(w)
			w.WriteHeader(http.StatusUnauthorized)
			render.JSON(w, r, map[string]string{
				"message": "Unauthorized",
			})
			return
		}

		if _, ok := t.blacklist[token.Raw]; ok {
			util.SetHeaderJson(w)
			w.WriteHeader(http.StatusUnauthorized)
			render.JSON(w, r, map[string]string{
				"message": "Unauthorized",
			})
		}

		if !token.Valid {
			util.SetHeaderJson(w)
			w.WriteHeader(http.StatusUnauthorized)
			render.JSON(w, r, map[string]string{
				"message": "Authorization Expired",
			})
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

func (t *TokenAuth) AddToBlackList(token *jwt.Token) {
	defer t.m.Unlock()
	t.m.Lock()
	t.blacklist[token.Raw] = true
}

func (t *TokenAuth) Token(r *http.Request) (*jwt.Token, error) {
	tokenStr := jwtauth.TokenFromHeader(r)
	return t.auth.Decode(tokenStr)
}

func New(secret string) *TokenAuth {
	return &TokenAuth{
		auth:      jwtauth.New("HS256", []byte(secret), nil),
		expire:    time.Minute * 30,
		refresh:   time.Minute * 30,
		m:         &sync.Mutex{},
		blacklist: make(map[string]bool),
	}
}
