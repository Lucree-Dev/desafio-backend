package models

type Transfer struct {
	FriendID    string     `json:"friend_id" pg:"friend_id"`
	TotalToPay  string     `json:"total_to_pay" pg:"total_to_pay"`
	BillingCard CreditCard `json:"billing_card" pg:"billing_card"`
}
