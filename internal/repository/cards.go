package repository

import (
	"fmt"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (repo *Repository) CreateCard(cards []models.Card) error {
	for _, card := range cards {
		err := repo.database.Create(&card).Error
		if err != nil {
			return fmt.Errorf("error creating card")
		}
	}

	return nil
}

func (repo *Repository) ListCards(id string) ([]models.Card, error) {
	cards := []models.Card{}

	err := repo.database.Where("user_id = ?", id).Find(&cards).Error
	if err != nil {
		return []models.Card{}, fmt.Errorf("error getting card")
	}

	return cards, nil
}
