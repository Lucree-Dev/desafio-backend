package models

import (
	"time"

	"github.com/jinzhu/gorm"
	uuid "github.com/satori/go.uuid"
)

type Card struct {
	gorm.Model

	CardID       string    `json:"card_id" gorm:"primaryKey"`
	Date         time.Time `json:"date"`
	ExpiryMM     string    `json:"expiry_mm"`
	ExpiryYYYY   string    `json:"expiry_yyyy"`
	PAN          string    `json:"pan"`
	SecurityCode string    `json:"security_code"`
	Title        string    `json:"title"`
	UserID       uuid.UUID
}
