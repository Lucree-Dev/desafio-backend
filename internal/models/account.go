package models

type Account struct {
	FirstName string `json:"first_name" rethinkdb:"first_name" validate:"required"`
	LastName  string `json:"last_name" rethinkdb:"last_name" validate:"required"`
	Birthday  string `json:"birthday" rethinkdb:"birthday" validate:"required"`
	Password  string `json:"password,omitempty" rethinkdb:"password" validate:"required,min=6"`
	Username  string `json:"username" rethinkdb:"username" validate:"required,min=6"`
	UserID    string `json:"user_id" rethinkdb:"user_id" validate:"required"`
}
