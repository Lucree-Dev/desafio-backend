package models

type BillingCard struct {
	CardID string `json:"card_id" rethinkdb:"card_id" validate:"required"`
}
