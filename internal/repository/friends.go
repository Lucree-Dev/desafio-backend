package repository

import (
	"fmt"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (repo *Repository) GetAllFriends(username string) ([]*models.User, error) {
	var user models.User

	if err := repo.database.Preload("Friends").First(&user, "username = ?", username); err != nil {
		return []*models.User{}, fmt.Errorf("internal error")
	}

	return user.Friends, nil
}
