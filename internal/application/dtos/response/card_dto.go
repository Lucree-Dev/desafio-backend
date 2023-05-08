package response

import "time"

// Compreendendo que a informação do "security_code" é sigilosa, preferi não exibi-la no protocolo mesmo sendo criptografada
type Card struct {
	Title       string    `json:"title"`
	Pan         string    `json:"pan"`
	ExpireMonth string    `json:"expiry_mm"`
	ExpireYear  string    `json:"expiry_yyyy"`
	Date        time.Time `json:"date"`
}

func NewCard(
	title,
	pan,
	expireMonth,
	expireYear string,
	date time.Time,
) Card {
	return Card{
		Title:       title,
		Pan:         pan,
		ExpireMonth: expireMonth,
		ExpireYear:  expireYear,
		Date:        date,
	}
}
