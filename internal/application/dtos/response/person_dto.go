package response

import "time"

// Compreendendo que a senha mesma criptografada é uma informação sigilosa, preferi ser mais cauteloso e não exibi-la no protocolo
type Person struct {
	FirstName string    `json:"first_name"`
	LastName  string    `json:"last_name"`
	Birthday  time.Time `json:"birthday"`
	UserName  string    `json:"username"`
}

func NewPerson(
	firstName,
	lastName,
	userName string,
	birthday time.Time,
) Person {
	return Person{
		FirstName: firstName,
		LastName:  lastName,
		Birthday:  birthday,
		UserName:  userName,
	}
}
