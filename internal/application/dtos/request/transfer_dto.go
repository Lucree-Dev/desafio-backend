package request

import "github.com/shopspring/decimal"

type Payment struct {
	FriendId    int             `json:"friend_id"`
	Value       decimal.Decimal `json:"total_to_transfer"`
	BillingCard BillingCard     `json:"billing_card"`
}

type BillingCard struct {
	CardId int `json:"card_id"`
}

func NewPaymentDefault() *Payment {
	return &Payment{}
}

func NewPayment(friendId, cardId int, value decimal.Decimal) *Payment {
	return &Payment{
		FriendId: friendId,
		Value:    value,
		BillingCard: BillingCard{
			CardId: cardId,
		},
	}
}
