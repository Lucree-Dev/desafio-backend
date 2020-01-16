package models

type Transfer struct {
	UserID      string      `json:"user_id,omitempty" rethinkdb:"user_id"`
	FriendID    string      `json:"friend_id" rethinkdb:"friend_id" validate:"required"`
	TotalToPay  int         `json:"total_to_transfer,omitempty" rethinkdb:"total_to_pay,omitempty" validate:"required"`
	BillingCard *CreditCard `json:"billing_card,omitempty" rethinkdb:"billing_card,omitempty" validate:"required"`
	Value       int         `json:"value,omitempty" rethinkdb:"value,omitempty"`
	Date        string      `json:"date,omitempty" rethinkdb:"date,omitempty"`
	FromCard    string      `json:"from_card,omitempty" rethinkdb:"from_card,omitempty"`
}
