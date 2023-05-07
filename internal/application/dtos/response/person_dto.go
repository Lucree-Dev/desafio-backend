package response

import "time"

// Compreendendo que a senha mesma criptografada é uma informação sigilosa, preferi ser mais cauteloso e não exibi-la no protocolo
type Person struct {
	FirstName string    `json:"first_name"`
	LastName  string    `json:"last_name"`
	Birthday  time.Time `json:"birthday"`
	UserName  string    `json:"username"`
}

func NewPerson(FirstName, LastName, UserName string, Birthday time.Time) Person {
	return Person{
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		UserName:  UserName,
	}
}
