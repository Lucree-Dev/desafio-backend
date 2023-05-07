package tokenize

import "unicode"

func TokenizeCardNumber(cardNumber string) string {
	tokenized := ""
	for i, digit := range cardNumber {
		if i < len(cardNumber)-4 && unicode.IsDigit(digit) {
			tokenized += "*"
		} else {
			tokenized += string(digit)
		}
	}
	return tokenized
}
