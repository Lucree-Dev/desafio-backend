package entities

import (
	"time"

	"github.com/shopspring/decimal"
)

type Payment struct {
	Id       int             `pg:"id"`
	FriendId int             `pg:"friend_id"`
	CardId   int             `pg:"card_id"`
	PersonId int             `pg:"people_id"`
	Value    decimal.Decimal `pg:"value"`
	Date     time.Time       `pg:"date"`
}

func NewPayment(
	friendId,
	cardId,
	personId int,
	value decimal.Decimal,
) *Payment {
	return &Payment{
		FriendId: friendId,
		CardId:   cardId,
		PersonId: personId,
		Value:    value,
		Date:     time.Now().UTC(),
	}
}
