package response

import "time"

// Compreendendo que a informação do "security_code" é sigilosa, preferi não exibi-la no protocolo mesmo sendo criptografada
type Card struct {
	Title        string    `json:"title"`
	Pan          string    `json:"pan"`
	ExpireMonth  string    `json:"expiry_mm"`
	ExpireYear   string    `json:"expiry_yyyy"`
	CreationDate time.Time `json:"date"`
}

func NewCard(Title, Pan, ExpireMonth, ExpireYear string, CreationDate time.Time) Card {
	return Card{
		Title:        Title,
		Pan:          Pan,
		ExpireMonth:  ExpireMonth,
		ExpireYear:   ExpireYear,
		CreationDate: CreationDate,
	}
}
