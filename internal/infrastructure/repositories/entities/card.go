package entities

import "time"

type Card struct {
	Id           int       `pg:"id"`
	Title        string    `pg:"title"`
	Pan          string    `pg:"pan"`
	ExpireMonth  string    `pg:"expiry_mm"`
	ExpireYear   string    `pg:"expiry_yyyy"`
	SecurityCode string    `pg:"security_code"`
	Date         time.Time `pg:"date"`
	PersonId     int       `pg:"people_id"`
}

func NewCardDefault() *Card {
	return &Card{}
}

func NewCard(
	title,
	pan,
	expireMonth,
	expireYear,
	securityCode string,
	personId int,
) *Card {
	return &Card{
		Title:        title,
		Pan:          pan,
		ExpireMonth:  expireMonth,
		ExpireYear:   expireYear,
		SecurityCode: securityCode,
		Date:         time.Now().UTC(),
		PersonId:     personId,
	}
}
