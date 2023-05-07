package request

type Card struct {
	Title        string `json:"title"`
	Pan          string `json:"pan"`
	ExpireMonth  string `json:"expiry_mm"`
	ExpireYear   string `json:"expiry_yyyy"`
	SecurityCode string `json:"security_code"`
}

func NewCard() *Card {
	return &Card{}
}
