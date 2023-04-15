package models

import "time"

type Person struct {
	Id        *string    `json:"user_id" binding:"required"`
	FirstName *string    `json:"first_name" binding:"required"`
	LastName  *string    `json:"last_name" binding:"required"`
	BirthDay  *time.Time `json:"birthday" binding:"required"`
	Password  *string    `json:"password" binding:"required"`
	Username  *string    `json:"username" binding:"required"`
}
