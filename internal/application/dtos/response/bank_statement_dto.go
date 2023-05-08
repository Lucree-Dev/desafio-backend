package response

import (
	"time"

	"github.com/shopspring/decimal"
)

type BankStatement struct {
	PersonId int             `json:"user_id"`
	FriendId int             `json:"friend_id"`
	CardId   int             `json:"from_card"`
	Value    decimal.Decimal `json:"value"`
	Date     time.Time       `json:"date"`
}

func NewBankStatement(
	personId,
	friendId,
	cardId int,
	value decimal.Decimal,
	date time.Time,
) BankStatement {
	return BankStatement{
		PersonId: personId,
		FriendId: friendId,
		CardId:   cardId,
		Value:    value,
		Date:     date,
	}
}
