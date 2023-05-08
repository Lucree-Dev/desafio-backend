package bcrypt

import (
	"golang.org/x/crypto/bcrypt"
)

func Encrypt(password string) (string, error) {
	passwordBytes := []byte(password)
	result, err := bcrypt.GenerateFromPassword(passwordBytes, bcrypt.DefaultCost)
	if err != nil {
		return "", err
	}
	return string(result), nil
}

func Verify(encryptedPassword string, password string) error {
	passwordBytes := []byte(password)
	encryptedPasswordBytes := []byte(encryptedPassword)
	return bcrypt.CompareHashAndPassword(encryptedPasswordBytes, passwordBytes)
}
