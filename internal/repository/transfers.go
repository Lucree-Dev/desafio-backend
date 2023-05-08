package repository

import (
	"fmt"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (repo *Repository) CreateTransfers(transfers []models.Transfer) error {
	for _, transfer := range transfers {
		err := repo.database.Create(&transfer).Error
		if err != nil {
			return fmt.Errorf("error creating transfer")
		}
	}

	return nil
}

func (repo *Repository) ListTransfersByID(id string) ([]models.Transfer, error) {
	tranfers := []models.Transfer{}

	err := repo.database.Where("user_id = ?", id).Find(&tranfers).Error
	if err != nil {
		return []models.Transfer{}, fmt.Errorf("error getting card")
	}

	return tranfers, nil
}

func (repo *Repository) ListTransfers() ([]models.TranfersResponse, error) {
	tranfers := []models.Transfer{}

	err := repo.database.Find(&tranfers).Error
	if err != nil {
		return []models.TranfersResponse{}, fmt.Errorf("error getting card")
	}

	tranfersResponse := []models.TranfersResponse{}
	for _, v := range tranfers {
		tr := models.TranfersResponse{
			UserID:   v.UserID.String(),
			FriendID: v.FriendID,
			Value:    v.TotalToTransfer,
			Date:     v.CreatedAt.String(),
			FromCard: v.CardID,
		}

		tranfersResponse = append(tranfersResponse, tr)
	}

	return tranfersResponse, nil
}
