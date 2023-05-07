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

func NewCardPartial(Title, Pan, ExpireMonth, ExpireYear, SecurityCode string, PersonId int) *Card {
	return &Card{
		Title:        Title,
		Pan:          Pan,
		ExpireMonth:  ExpireMonth,
		ExpireYear:   ExpireYear,
		SecurityCode: SecurityCode,
		CreationDate: time.Now(),
		PersonId:     PersonId,
	}
}
