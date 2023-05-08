package entities

import "time"

type Person struct {
	Id        int       `pg:"id"`
	FirstName string    `pg:"first_name"`
	LastName  string    `pg:"last_name"`
	Birthday  time.Time `pg:"birthday"`
	Password  string    `pg:"password"`
	UserName  string    `pg:"username"`
}

func NewPerson() *Person {
	return &Person{}
}

func NewPersonFull(
	firstName,
	lastName,
	password,
	userName string,
	birthday time.Time,
) *Person {
	return &Person{
		FirstName: firstName,
		LastName:  lastName,
		Birthday:  birthday,
		Password:  password,
		UserName:  userName,
	}
}
