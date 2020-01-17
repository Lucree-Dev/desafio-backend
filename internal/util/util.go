package util

import (
	"bytes"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"net/http"
	"os"

	"github.com/go-chi/render"
)

func SetHeaderJson(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Accept", "application/json")
}

func AcceptJson(next http.HandlerFunc) http.HandlerFunc {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		if render.GetAcceptedContentType(r) == render.ContentTypeJSON {
			http.Error(w, http.StatusText(http.StatusNotAcceptable), http.StatusNotAcceptable)
			return
		}
		next.ServeHTTP(w, r)
	})
}

func EncodeToSha256(args ...string) string {
	var b bytes.Buffer
	for _, arg := range args {
		b.WriteString(arg)
	}
	data := sha256.Sum256(b.Bytes())
	return hex.EncodeToString(data[:])
}

func GetEnv(key, valueDefault string) (value string) {
	if value = os.Getenv(key); len(value) == 0 {
		value = valueDefault
	}
	return
}

func Address() (addr string) {
	host := GetEnv("API_HOST", "localhost")
	port := GetEnv("API_PORT", "8080")
	return fmt.Sprintf("%s:%s", host, port)
}
