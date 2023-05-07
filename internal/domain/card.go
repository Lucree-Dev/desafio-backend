package domain

import "time"

type Card struct {
	Id           int
	Title        string
	Pan          string
	ExpireMonth  string
	ExpireYear   string
	SecurityCode string
	CreationDate time.Time
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

func NewCardPartial(title, pan, expireMonth, expireYear, securityCode string) Card {
	return Card{
		Title:        title,
		Pan:          pan,
		ExpireMonth:  expireMonth,
		ExpireYear:   expireYear,
		SecurityCode: securityCode,
	}
}
