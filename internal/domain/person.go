package domain

type Person struct {
	Id        int
	FirstName string
	LastName  string
	Birthday  string
	Password  string
}

func NewPerson() *Person {
	return &Person{}
}

func NewPersonFull(Id int, FirstName, LastName, Birthday, Password string) *Person {
	return &Person{
		Id:        Id,
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		Password:  Password,
	}
}

func NewPersonPartial(FirstName, LastName, Birthday, Password string) Person {
	return Person{
		FirstName: FirstName,
		LastName:  LastName,
		Birthday:  Birthday,
		Password:  Password,
	}
}
