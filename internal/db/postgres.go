package database

import (
	"context"
	"fmt"
	"log"
	"strconv"

	"github.com/Lucree-Dev/desafio-backend/internal/config"
	"github.com/Lucree-Dev/desafio-backend/internal/models"
	"github.com/go-pg/pg/v10"
	"github.com/jinzhu/gorm"

	_ "github.com/lib/pq"
)

type Database struct {
	DB *pg.DB
}

func NewDatabase(ctx context.Context, connString string) (*Database, error) {
	opt, err := pg.ParseURL(connString)
	if err != nil {
		return nil, err
	}

	db := pg.Connect(opt)
	if err := db.Ping(ctx); err != nil {
		return nil, err
	}

	return &Database{DB: db}, nil
}

func ConnectDB() (*gorm.DB, error) {
	port, err := strconv.ParseUint(config.Config("POSTGRES_PORT"), 10, 32)
	if err != nil {
		return nil, fmt.Errorf("failed to parse port number: %v", err)
	}

	configData := fmt.Sprintf(
		"host=%s port=%d user=%s password=%s dbname=%s sslmode=disable",
		config.Config("POSTGRES_HOST"),
		port,
		config.Config("POSTGRES_USER"),
		config.Config("POSTGRES_PASSWORD"),
		config.Config("POSTGRES_DB"),
	)

	db, err := gorm.Open("postgres", configData)
	if err != nil {
		return nil, fmt.Errorf("failed to open database connection: %v", err)
	}

	err = db.AutoMigrate(&models.User{}, &models.Card{}, &models.Transfer{}).Error
	if err != nil {
		return nil, fmt.Errorf("failed to perform database migrations: %v", err)
	}

	log.Println("Successfully connected to the database")
	return db, nil

}
