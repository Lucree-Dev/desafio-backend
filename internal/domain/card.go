package domain

import (
	"account/pkg/bcrypt"
	"account/pkg/tokenize"
	"time"
)

type Card struct {
	Id           int
	Title        string
	Pan          string
	ExpireMonth  string
	ExpireYear   string
	SecurityCode string
	Date         time.Time
}

func NewCardFull(id int, title, pan, expireMonth, expireYear, securityCode string, date time.Time) *Card {
	return &Card{
		Id:           id,
		Title:        title,
		Pan:          pan,
		ExpireMonth:  expireMonth,
		ExpireYear:   expireYear,
		SecurityCode: securityCode,
		Date:         date,
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

func (c Card) CardNumber() string {
	return tokenize.TokenizeCardNumber(c.Pan)
}

func (c Card) EncryptSecurityCode() string {
	result, err := bcrypt.Encrypt(c.SecurityCode)
	if err != nil {
		panic(err)
	}
	return result
}
