package models

type User struct {
	FirstName string `json:"first_name"`
	LastName  string `json:"last_name"`
	Birthday  string `json:"birthday"`
	Password  string `json:"password"`
	Username  string `json:"username"`
	UserID    string `json:"user_id"`
}
