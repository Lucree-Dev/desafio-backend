package domain

import "time"

type Person struct {
	Id        int
	FirstName string
	LastName  string
	Birthday  time.Time
	Password  string
	UserName  string
}

func NewPerson() *Person {
	return &Person{}
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
