package repository

import (
	"fmt"

	"github.com/Lucree-Dev/desafio-backend/internal/models"
)

func (repo *Repository) CreateUser(user *models.User) error {
	err := repo.database.Create(&user).Error
	if err != nil {
		return fmt.Errorf("error creating user")
	}

	return nil
}

func (repo *Repository) Login(req models.LoginRequest) (models.User, error) {
	var user models.User
	if err := repo.database.Where("username = ?", req.Username).First(&user).Error; err != nil {
		return models.User{}, fmt.Errorf("internal error")
	}

	return user, nil
}
