package models

type Account struct {
	FirstName string `json:"first_name" rethinkdb:"first_name"`
	LastName  string `json:"last_name" rethinkdb:"last_name"`
	Birthday  string `json:"birthday" rethinkdb:"birthday"`
	Password  string `json:"password,omitempty" rethinkdb:"password"`
	Username  string `json:"username" rethinkdb:"username"`
	UserID    string `json:"user_id" rethinkdb:"user_id"`
}
