package controllers

import (
	"fmt"
	"net/http"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (uc UserController) GetAllFriends(username string) ([]*models.User, int, error) {
	friends, err := uc.db.GetAllFriends(username)
	if err != nil {
		return nil, http.StatusInternalServerError, err
	}

	if len(friends) == 0 {
		return nil, http.StatusNotFound, fmt.Errorf("friends not found")

	}

	return friends, http.StatusOK, nil
}
