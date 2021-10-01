package service

import "golang.org/x/crypto/bcrypt"

// turns the password into a hash
func Hash(password string) ([]byte, error) {
	return bcrypt.GenerateFromPassword([]byte(password), bcrypt.DefaultCost)
}

func VerifyPassword(passHash, password string) error {
	return bcrypt.CompareHashAndPassword([]byte(passHash), []byte(password))
}
