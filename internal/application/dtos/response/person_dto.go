package response

type Person struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Birthday  string `json:"birthday"`
}

func NewPerson(FirstName, LastName, Birthday string) Person {
	return Person{
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
	}
}
