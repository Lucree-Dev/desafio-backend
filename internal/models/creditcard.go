package models

type CreditCard struct {
	CardID string `json:"credit_id" pg:"card_id"`
}
