package domain

import (
	"account/pkg/bcrypt"
	"time"
)

type Person struct {
	Id        int
	FirstName string
	LastName  string
	Birthday  time.Time
	Password  string
	UserName  string
}

func NewPersonFull(
	id int,
	firstName,
	lastName,
	password,
	userName string,
	birthday time.Time,
) *Person {
	return &Person{
		Id:        id,
		FirstName: firstName,
		LastName:  lastName,
		Birthday:  birthday,
		Password:  password,
		UserName:  userName,
	}
}

func NewPersonPartial(
	firstName,
	lastName,
	password,
	userName string,
	birthday time.Time,
) Person {
	return Person{
		FirstName: firstName,
		LastName:  lastName,
		Birthday:  birthday,
		Password:  password,
		UserName:  userName,
	}
}

func (p Person) EncryptPassword() string {
	result, err := bcrypt.Encrypt(p.Password)
	if err != nil {
		panic(err)
	}
	return result
}
