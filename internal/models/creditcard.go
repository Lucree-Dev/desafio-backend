package models

type CreditCard struct {
	CardID       string `json:"card_id,omitempty" rethinkdb:"card_id" validate:"required"`
	Title        string `json:"title,omitempty" rethinkdb:"title,omitempty" validate:"required"`
	Pan          string `json:"pan,omitempty" rethinkdb:"pan,omitempty" validate:"required"`
	ExpiryMM     string `json:"expiry_mm,omitempty" rethinkdb:"expiry_mm,omitempty" validate:"required"`
	ExpiryYYYY   string `json:"expiry_yyyy,omitempty" rethinkdb:"expiry_yyyy,omitempty" validate:"required"`
	SecurityCode string `json:"security_code,omitempty" rethinkdb:"security_code,omitempty" validate:"required"`
	Date         string `json:"date,omitempty" rethinkdb:"date,omitempty" validate:"required"`
	UserID       string `json:"-" rethinkdb:"user_id,omitempty"`
}
