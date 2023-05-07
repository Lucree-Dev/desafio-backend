package request

import "time"

type Person struct {
	FirstName string    `json:"first_name"`
	LastName  string    `json:"last_name"`
	Birthday  time.Time `json:"birthday"`
	Password  string    `json:"password"`
	UserName  string    `json:"username"`
}

func NewPerson() *Person {
	return &Person{}
}
