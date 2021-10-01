package models

import (
	"errors"
)

type Transfer struct {
	Transfer_id  int64        `json:"transfer_id ,omitempty"`
	User_id      int64        `json:"user_id ,omitempty"`
	Friend_id    uint64       `json:"friend_id,omitempty"`
	Value        float64      `json:"value,omitempty"`
	Date         string       `json:"date,omitempty"`
	FromCard     uint64       `json:"from_card,omitempty"`
	Total_to_pay float32      `json:"total_to_pay,omitempty"`
	BillingCard  Billing_card `json:"BillingCard,omitempty"`
}

type Billing_card struct {
	Card_id uint64 `json:"card_id,omitempty"`
}

func (transfer *Transfer) Prepare() error {
	if err := transfer.validate(); err != nil {
		return err
	}

	return nil
}
func (transfer *Transfer) validate() error {
	if transfer.Friend_id < 1 || transfer.Total_to_pay == 0 || transfer.BillingCard.Card_id < 1 {
		return errors.New("All fields must be required")
	}

	return nil
}
