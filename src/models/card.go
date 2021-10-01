package models

import (
	"errors"
)

type Card struct {
	Card_ID       int64  `json:"card_id,omitempty"`
	Person_ID     uint64 `json:"person_id,omitempty"`
	Title         string `json:"title,omitempty"`
	Pan           string `json:"pan,omitempty"`
	Expiry_mm     string `json:"expiry_mm,omitempty"`
	Expiry_yyy    string `json:"expiry_yyy,omitempty"`
	Security_code string `json:"security_code,omitempty"`
	Date          string `json:"date,omitempty"`
}

func (card *Card) Prepare() error {
	if err := card.validate(); err != nil {
		return err
	}

	return nil
}
func (card *Card) validate() error {
	if card.Title == "" || card.Person_ID < 1 || card.Pan == "" || card.Expiry_mm == "" || card.Expiry_yyy == "" || card.Security_code == "" || card.Date == "" {
		return errors.New("All fields must be required")
	}

	return nil
}
