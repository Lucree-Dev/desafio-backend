package models

type Account struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Birthday  string `json:"birthday"`
	Password  string `json:"password,omitempty"`
	Username  string `json:"username"`
	UserID    string `json:"user_id,omitempty"`
}
