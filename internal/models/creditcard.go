package models

import "github.com/jinzhu/gorm"

type CreditCard struct {
	gorm.Model
	tableName  struct{} `pg:"creditcards"`
	CardID     string   `json:"card_id,omintempty" rethinkdb:"card_id"`
	Title      string   `json:"title,omintempty" rethinkdb:"title"`
	Pan        string   `json:"pan,omintempty" rethinkdb:"pan"`
	ExpiryMM   string   `json:"expiry_mm,omintempty" rethinkdb:"expiry_mm"`
	ExpiryYYY  string   `json:"expiry_yyy,omintempty" rethinkdb:"expiry_yyy"`
	SecuryCode string   `json:"securycode,omintempty" rethinkdb:"securycode"`
	Date       string   `json:"date,omintempty" rethinkdb:"date"`
	UserID     string   `json:"-" rethinkdb:"user_id"`
}
