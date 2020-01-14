package models

type Transfer struct {
	ID            int
	FriendID      string      `json:"friend_id" pg:"friend_id"`
	TotalToPay    string      `json:"total_to_pay" pg:"total_to_pay"`
	BillingCard   *CreditCard `json:"billing_card" pg:"fk:billing_card_id"`
	BillingCardID int         `json:"-"`
}
