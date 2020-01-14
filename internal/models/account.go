package models

type Account struct {
	ID        int    `json:"-"`
	FirstName string `json:"first_name" pg:"first_name,notnull"`
	LastName  string `json:"last_name" pg:"last_name,notnull"`
	Birthday  string `json:"birthday" pg:"birthday,notnull"`
	Password  string `json:"password,omitempty" pg:"password,notnull"`
	Username  string `json:"username" pg:"username,notnull"`
	UserID    string `json:"user_id,omitempty" pg:"user_id,notnull"`
}
