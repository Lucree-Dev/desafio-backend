package models

type Transfer struct {
	UserID        string     `json:"-" rethinkdb:"user_id"`
	FriendID      string     `json:"friend_id" rethinkdb:"friend_id"`
	TotalToPay    string     `json:"total_to_pay" rethinkdb:"total_to_pay"`
	BillingCardID string     `json:"-" rethinkdb:"billingcard_id"`
	BillingCard   CreditCard `json:"billingcard" rethinkdb:"-"`
}
