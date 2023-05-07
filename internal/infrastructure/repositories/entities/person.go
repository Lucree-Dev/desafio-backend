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

func NewPersonFull(FirstName, LastName, Password, UserName string, Birthday time.Time) *Person {
	return &Person{
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		Password:  Password,
		UserName:  UserName,
	}
}
