package entities

type Person struct {
	Id        int    `pg:"id"`
	FirstName string `pg:"first_name"`
	LastName  string `pg:"last_name"`
	Birthday  string `pg:"birthday"`
	Password  string `pg:"password"`
}
