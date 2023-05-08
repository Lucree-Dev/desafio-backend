package domain

import (
	"time"

	"github.com/shopspring/decimal"
)

type Payment struct {
	Id       int
	FriendId int
	CardId   int
	PersonId int
	Value    decimal.Decimal
	Date     time.Time
}

func NewPaymentFull(
	id,
	friendId,
	cardId,
	personId int,
	value decimal.Decimal,
	date time.Time,
) *Payment {
	return &Payment{
		Id:       id,
		FriendId: friendId,
		CardId:   cardId,
		PersonId: personId,
		Value:    value,
		Date:     date,
	}
}

func NewPayment(
	friendId,
	cardId,
	personId int,
	value decimal.Decimal,
) Payment {
	return Payment{
		FriendId: friendId,
		CardId:   cardId,
		PersonId: personId,
		Value:    value,
	}
}
