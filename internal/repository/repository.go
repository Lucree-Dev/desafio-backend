package repository

import "github.com/jinzhu/gorm"

type Repository struct {
	database *gorm.DB
}

func NewRepository(database *gorm.DB) *Repository {
	return &Repository{
		database: database,
	}
}
