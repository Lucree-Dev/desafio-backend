package models

type Card struct {
	CardID     string `json:"cardID" pg:"cardID"`
	Title      string `json:"title" pg:"title"`
	Pan        string `json:"pan" pg:"pan"`
	ExpiryMM   string `json:"expiry_mm" pg:"expiry_mm"`
	ExpiryYYY  string `json:"expiry_yyy" pg:"expiry_yyy"`
	SecureCode string `json:"securecode" pg:"securecode"`
	Date       string `json:"date" pg:"date"`
}
