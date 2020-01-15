package models

import "github.com/jinzhu/gorm"

type Transfer struct {
	gorm.Model
	ID            int         `json:"-"`
	UserID        string      `json:"-" pg:"user_id"`
	FriendID      interface{} `json:"friend_id" pg:"friend_id"`
	Friend        *Account    `sql:"fk:friend_id"`
	TotalToPay    string      `json:"total_to_pay" pg:"total_to_pay"`
	BillingCardID string      `json:"-"`
	BillingCard   *CreditCard `json:"billingcard" sql:"fk:billing_card_id"`
}
