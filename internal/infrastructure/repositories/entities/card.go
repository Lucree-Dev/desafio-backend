package entities

import "time"

type Card struct {
	Id           int       `pg:"id"`
	Title        string    `pg:"title"`
	Pan          string    `pg:"pan"`
	ExpireMonth  string    `pg:"expiry_mm"`
	ExpireYear   string    `pg:"expiry_yyyy"`
	SecurityCode string    `pg:"security_code"`
	CreationDate time.Time `pg:"creation_date"`
	PersonId     int       `pg:"people_id"`
}

func NewCardFull(id int, title, pan, expireMonth, expireYear, securityCode string, creationDate time.Time) *Card {
	return &Card{
		Id:           id,
		Title:        title,
		Pan:          pan,
		ExpireMonth:  expireMonth,
		ExpireYear:   expireYear,
		SecurityCode: securityCode,
		CreationDate: creationDate,
	}
}

func NewCardPartial(title, pan, expireMonth, expireYear, securityCode string, personId int) *Card {
	return &Card{
		Title:        title,
		Pan:          pan,
		ExpireMonth:  expireMonth,
		ExpireYear:   expireYear,
		SecurityCode: securityCode,
		CreationDate: time.Now().UTC(),
		PersonId:     personId,
	}
}
