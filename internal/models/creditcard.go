package models

import "github.com/jinzhu/gorm"

type CreditCard struct {
	gorm.Model
	tableName  struct{} `pg:"creditcards"`
	CardID     string   `json:"card_id,omintempty" pg:"card_id,pk"`
	Title      string   `json:"title,omintempty" pg:"title,notnull"`
	Pan        string   `json:"pan,omintempty" pg:"pan,notnull"`
	ExpiryMM   string   `json:"expiry_mm,omintempty" pg:"expiry_mm,notnull"`
	ExpiryYYY  string   `json:"expiry_yyy,omintempty" pg:"expiry_yyy,notnull"`
	SecuryCode string   `json:"securycode,omintempty" pg:"securycode,notnull"`
	Date       string   `json:"date,omintempty" pg:"date,notnull"`
	UserID     string   `json:"-" pg:"user_id"`
	User       *Account `sql:"fk:user_id"`
}
