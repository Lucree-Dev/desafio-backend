package auth

import (
	"encoding/json"
	"errors"
	"time"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
	jwt "github.com/dgrijalva/jwt-go"
)

const (
	expirationTime = 24 * time.Hour
	secretKey      = "secret"
)

func GenerateToken(user models.User) ([]byte, error) {
	token := jwt.New(jwt.SigningMethodHS256)
	claims := token.Claims.(jwt.MapClaims)
	claims["name"] = user.FirstName + " " + user.LastName
	claims["userid"] = user.UserID
	claims["iat"] = time.Now().Unix()
	claims["exp"] = time.Now().Add(expirationTime).Unix()

	tokenString, err := token.SignedString([]byte(secretKey))
	if err != nil {
		return []byte{}, err
	}

	jsonResponse, err := json.Marshal(map[string]string{"token": tokenString})
	if err != nil {
		return []byte{}, err
	}

	return jsonResponse, nil
}

func VerifyToken(tokenString string) (*jwt.Token, error) {
	return jwt.Parse(tokenString, func(token *jwt.Token) (interface{}, error) {
		if _, ok := token.Method.(*jwt.SigningMethodHMAC); !ok {
			return nil, errors.New("unexpected signing method")
		}

		return []byte(secretKey), nil
	})
}
