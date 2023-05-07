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

func NewPersonFull(Id int, FirstName, LastName, Password, UserName string, Birthday time.Time) *Person {
	return &Person{
		Id:        Id,
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		Password:  Password,
		UserName:  UserName,
	}
}

func NewPersonPartial(FirstName, LastName, Password, UserName string, Birthday time.Time) Person {
	return Person{
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		Password:  Password,
		UserName:  UserName,
	}
}

func (p Person) EncryptPassword() string {
	result, err := bcrypt.EncryptPassword(p.Password)
	if err != nil {
		panic(err)
	}
	return result
}
