package http

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"strings"

	"github.com/Lucree-Dev/desafio-backend/internal/controllers"
	"github.com/Lucree-Dev/desafio-backend/internal/models"
	accountrepo "github.com/Lucree-Dev/desafio-backend/internal/repository"
	uuid "github.com/satori/go.uuid"

	"github.com/golang-jwt/jwt"
	"github.com/gorilla/mux"
)

type HttpHandler struct {
	repository *accountrepo.Repository
}

func NewHttpHandler(repository *accountrepo.Repository) *HttpHandler {
	return &HttpHandler{
		repository: repository,
	}
}

func (handler *HttpHandler) CreatePersonHandler(w http.ResponseWriter, r *http.Request) {
	var user models.User
	err := json.NewDecoder(r.Body).Decode(&user)
	if err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	err = user.Validate()
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		json.NewEncoder(w).Encode(map[string]string{"error": err.Error()})
		return
	}

	uc := controllers.NewUserController(handler.repository)

	token, err := uc.CreatePerson(user)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusOK)
	w.Write(token)
}

func (handler *HttpHandler) LoginHandler(w http.ResponseWriter, r *http.Request) {
	var req models.LoginRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	uc := controllers.NewUserController(handler.repository)
	token, statuscode, err := uc.Login(req)
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	w.WriteHeader(statuscode)
	w.Write(token)
}

func (handler *HttpHandler) GetFriends(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	username := vars["username"]
	if username == "" {
		http.Error(w, "invalid username", http.StatusBadRequest)
		return
	}

	uc := controllers.NewUserController(handler.repository)
	friends, statuscode, err := uc.GetAllFriends(username)
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	friendsJSON, err := json.Marshal(friends)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	w.WriteHeader(statuscode)
	w.Write(friendsJSON)
}

func (handler *HttpHandler) CreateCard(w http.ResponseWriter, r *http.Request) {
	var req []models.Card
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	userid := getUserID(r)
	uuid, err := uuid.FromString(userid)
	if err != nil {
		fmt.Println(err)
	}

	for i := 0; i < len(req); i++ {
		req[i].UserID = uuid
	}

	uc := controllers.NewUserController(handler.repository)
	statuscode, err := uc.CreateCard(req)
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	w.WriteHeader(statuscode)
}

func (handler *HttpHandler) ListCards(w http.ResponseWriter, r *http.Request) {
	userid := getUserID(r)
	uuid, err := uuid.FromString(userid)
	if err != nil {
		fmt.Println(err)
	}

	uc := controllers.NewUserController(handler.repository)
	cards, statuscode, err := uc.ListCards(uuid.String())
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	cardsJSON, err := json.Marshal(cards)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	w.Write(cardsJSON)
	w.WriteHeader(statuscode)
}

func (handler *HttpHandler) Transfer(w http.ResponseWriter, r *http.Request) {
	var req []models.Transfer
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "invalid request", http.StatusBadRequest)
		return
	}

	userid := getUserID(r)
	uuid, err := uuid.FromString(userid)
	if err != nil {
		fmt.Println(err)
	}

	for i := 0; i < len(req); i++ {
		req[i].UserID = uuid
	}

	uc := controllers.NewUserController(handler.repository)
	statuscode, err := uc.Transfer(req)
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	w.WriteHeader(statuscode)
}

func (handler *HttpHandler) ListTransfersByID(w http.ResponseWriter, r *http.Request) {
	vars := mux.Vars(r)
	userID := vars["userid"]
	if userID == "" {
		http.Error(w, "invalid userid", http.StatusBadRequest)
		return
	}

	_, err := uuid.FromString(userID)
	if err != nil {
		http.Error(w, "invalid uuid", http.StatusBadRequest)
		return
	}

	uc := controllers.NewUserController(handler.repository)
	tranfers, statuscode, err := uc.ListTransfersByID(userID)
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	tranfersJSON, err := json.Marshal(tranfers)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	w.Write(tranfersJSON)
	w.WriteHeader(statuscode)
}

func (handler *HttpHandler) ListTransfers(w http.ResponseWriter, r *http.Request) {

	uc := controllers.NewUserController(handler.repository)
	tranfers, statuscode, err := uc.ListTransfers()
	if err != nil {
		http.Error(w, err.Error(), statuscode)
		return
	}

	tranfersJSON, err := json.Marshal(tranfers)
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
	}

	w.Write(tranfersJSON)
	w.WriteHeader(statuscode)
}

func getUserID(r *http.Request) string {
	tokenString := strings.TrimPrefix(r.Header.Get("Authorization"), "Bearer ")
	claims, _ := extractClaims(tokenString)
	userID := claims["userid"].(string)

	return userID
}

func extractClaims(tokenStr string) (jwt.MapClaims, bool) {
	hmacSecretString := "secret"
	hmacSecret := []byte(hmacSecretString)
	token, err := jwt.Parse(tokenStr, func(token *jwt.Token) (interface{}, error) {
		return hmacSecret, nil
	})

	if err != nil {
		return nil, false
	}

	if claims, ok := token.Claims.(jwt.MapClaims); ok && token.Valid {
		return claims, true
	} else {
		log.Printf("Invalid JWT Token")
		return nil, false
	}
}
