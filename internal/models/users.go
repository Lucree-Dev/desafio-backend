package models

import (
	"errors"
	"fmt"
	"regexp"
	"time"
)

type User struct {
	Base

	FirstName   string `json:"first_name"`
	LastName    string `json:"last_name"`
	Birthday    string `json:"birthday"`
	Password    string `json:"password"`
	Username    string `json:"username" gorm:"uniqueIndex"`
	Friends     []*User
	CreditCards []Card `gorm:"foreignkey:UserID;association_foreignkey:UserID"`
}

var (
	uppercaseRegex   = regexp.MustCompile(`[A-Z]`)
	lowercaseRegex   = regexp.MustCompile(`[a-z]`)
	numberRegex      = regexp.MustCompile(`[0-9]`)
	specialCharRegex = regexp.MustCompile(`[!@#%&*_+=-]`)
)

func (u *User) Validate() error {
	if err := valideNames(u); err != nil {
		return err
	}

	if err := checkPass(u.Password); err != nil {
		return err
	}

	if err := validateBirthday(u.Birthday); err != nil {
		return err
	}

	return nil
}

func valideNames(u *User) error {
	if u.FirstName == "" {
		return fmt.Errorf("first name cannot be empty")
	}

	if u.LastName == "" {
		return fmt.Errorf("last name cannot be empty")
	}

	if u.Username == "" {
		return fmt.Errorf("username name cannot be empty")
	}
	return nil
}

func validateBirthday(birthday string) error {
	date, err := time.Parse("2006-01-02", birthday)
	if err != nil {
		return errors.New("invalid date format")
	}

	minAge := time.Now().AddDate(-18, 0, 0)
	if date.After(minAge) {
		return errors.New("must be at least 18 years old")
	}

	return nil
}

func checkPass(p string) error {
	if len(p) < 8 {
		return fmt.Errorf("password must be at least 8 characters long")
	}

	if !uppercaseRegex.MatchString(p) {
		return fmt.Errorf("password must contain at least one uppercase letter")
	}

	if !lowercaseRegex.MatchString(p) {
		return fmt.Errorf("password must contain at least one lowercase letter")
	}

	if !numberRegex.MatchString(p) {
		return fmt.Errorf("password must contain at least one number")
	}

	if !specialCharRegex.MatchString(p) {
		return fmt.Errorf("password must contain at least one special character")
	}
	return nil
}
