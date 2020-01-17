package models

type Transfer struct {
	UserID      string       `json:"user_id,omitempty" rethinkdb:"user_id"`
	FriendID    string       `json:"friend_id" rethinkdb:"friend_id" validate:"required"`
	TotalToPay  int          `json:"total_to_transfer,omitempty" rethinkdb:"total_to_pay,omitempty"`
	BillingCard *BillingCard `json:"billing_card,omitempty" rethinkdb:"billing_card,omitempty"`
	Value       int          `json:"value" rethinkdb:"value,omitempty"`
	Date        string       `json:"date,omitempty" rethinkdb:"date,omitempty"`
	FromCard    string       `json:"from_card" rethinkdb:"from_card,omitempty"`
}
