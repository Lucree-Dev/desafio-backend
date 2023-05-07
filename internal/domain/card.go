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

func NewCardFull(Id int, Title, Pan, ExpireMonth, ExpireYear, SecurityCode string, CreationDate time.Time) *Card {
	return &Card{
		Id:           Id,
		Title:        Title,
		Pan:          Pan,
		ExpireMonth:  ExpireMonth,
		ExpireYear:   ExpireYear,
		SecurityCode: SecurityCode,
		CreationDate: CreationDate,
	}
}

func NewCardPartial(Title, Pan, ExpireMonth, ExpireYear, SecurityCode string) Card {
	return Card{
		Title:        Title,
		Pan:          Pan,
		ExpireMonth:  ExpireMonth,
		ExpireYear:   ExpireYear,
		SecurityCode: SecurityCode,
	}
}
