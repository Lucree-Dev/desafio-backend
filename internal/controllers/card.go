package controllers

import (
	"net/http"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (uc UserController) CreateCard(req []models.Card) (int, error) {
	err := uc.db.CreateCard(req)
	if err != nil {
		return http.StatusInternalServerError, err
	}

	return http.StatusOK, nil
}

func (uc UserController) ListCards(id string) ([]models.Card, int, error) {
	cards, err := uc.db.ListCards(id)
	if err != nil {
		return []models.Card{}, http.StatusInternalServerError, err
	}

	return cards, http.StatusOK, nil
}

func (uc UserController) Transfer(req []models.Transfer) (int, error) {
	err := uc.db.CreateTransfers(req)
	if err != nil {
		return http.StatusInternalServerError, err
	}

	return http.StatusOK, nil
}
