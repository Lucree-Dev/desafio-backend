package models

import (
	"errors"
	"lucree/src/service"
)

type Person struct {
	First_name string `json:"first_name,omitempty"`
	Last_name  string `json:"last_name,omitempty"`
	Birthday   string `json:"birthday,omitempty"`
	Password   string `json:"password,omitempty"`
	Username   string `json:"username,omitempty"`
	User_id    int64  `json:"user_id,omitempty"`
}

func (person *Person) Prepare() error {
	if err := person.validate(); err != nil {
		return err
	}

	passHash, err := service.Hash(person.Password)

	if err != nil {
		return err
	}

	person.Password = string(passHash)
	return nil
}
func (person *Person) validate() error {
	if person.First_name == "" || person.Last_name == "" || person.Birthday == "" || person.Password == "" || person.Username == "" {
		return errors.New("All fields must be required")
	}

	return nil
}
