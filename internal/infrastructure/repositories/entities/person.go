package entities

import "time"

type Person struct {
	Id        int       `pg:"id"`
	FirstName string    `pg:"first_name"`
	LastName  string    `pg:"last_name"`
	Birthday  time.Time `pg:"birthday"`
	Password  string    `pg:"password"`
}

func NewPerson() *Person {
	return &Person{}
}

func NewPersonFull(FirstName, LastName, Password string, Birthday time.Time) *Person {
	return &Person{
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		Password:  Password,
	}
}
