package models

import (
	"github.com/jinzhu/gorm"
	uuid "github.com/satori/go.uuid"
)

type Transfer struct {
	gorm.Model

	BillingCard     `json:"billing_card"`
	FriendID        string    `json:"friend_id"`
	TotalToTransfer int       `json:"total_to_transfer"`
	UserID          uuid.UUID `json:"user_id" gorm:"embedded"`
}

type BillingCard struct {
	CardID string `json:"card_id"`
}

type TranfersResponse struct {
	UserID   string `json:"user_id"`
	FriendID string `json:"friend_id"`
	Value    int    `json:"value"`
	Date     string `json:"date"`
	FromCard string `json:"from_card"`
}
