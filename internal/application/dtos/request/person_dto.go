package request

type Person struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Birthday  string `json:"birthday"`
	Password  string `json:"password"`
}

func NewPerson() *Person {
	return &Person{}
}
