package controllers

import (
	"net/http"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (uc UserController) ListTransfersByID(id string) ([]models.Transfer, int, error) {
	transfers, err := uc.db.ListTransfersByID(id)
	if err != nil {
		return []models.Transfer{}, http.StatusInternalServerError, err
	}

	return transfers, http.StatusOK, nil
}

func (uc UserController) ListTransfers() ([]models.TranfersResponse, int, error) {
	transfers, err := uc.db.ListTransfers()
	if err != nil {
		return []models.TranfersResponse{}, http.StatusInternalServerError, err
	}

	return transfers, http.StatusOK, nil
}
