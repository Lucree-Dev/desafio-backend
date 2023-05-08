package controllers

import (
	"fmt"
	"net/http"

	"github.com/Lucree-Dev/desafio-backend/internal/auth"
	"github.com/Lucree-Dev/desafio-backend/internal/models"
	accountrepo "github.com/Lucree-Dev/desafio-backend/internal/repository"
	"golang.org/x/crypto/bcrypt"
)

type UserController struct {
	db *accountrepo.Repository
}

func NewUserController(db *accountrepo.Repository) *UserController {
	return &UserController{
		db: db,
	}
}

func (uc UserController) CreatePerson(user models.User) ([]byte, error) {
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(user.Password), bcrypt.DefaultCost)
	if err != nil {
		return []byte{}, fmt.Errorf("internal server error")
	}

	user.Password = string(hashedPassword)

	err = uc.db.CreateUser(&user)
	if err != nil {
		return []byte{}, fmt.Errorf("internal server error")
	}

	token, err := auth.GenerateToken(user)
	if err != nil {
		return []byte{}, fmt.Errorf("internal server error")
	}

	return token, nil
}

func (uc UserController) Login(req models.LoginRequest) ([]byte, int, error) {
	user, err := uc.db.Login(req)
	if err != nil {
		return []byte{}, http.StatusInternalServerError, err
	}

	if user.Password == "" {
		return []byte{}, http.StatusNotFound, fmt.Errorf("user not found")
	}

	if !checkPasswordHash(req.Password, user.Password) {
		return []byte{}, http.StatusUnauthorized, fmt.Errorf("invalid password")
	}

	token, err := auth.GenerateToken(user)
	if err != nil {
		return []byte{}, http.StatusInternalServerError, fmt.Errorf("internal server error")
	}

	return token, http.StatusOK, nil
}

func checkPasswordHash(password, hash string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(hash), []byte(password))
	return err == nil
}
