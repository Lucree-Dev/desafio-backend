package dtos

type CreatePersonDto struct {
	FirstName      *string `json:"first_name" validate:"required,min=1,max=100"`
	LastName       *string `json:"last_name" validate:"required,min=1,max=100"`
	BirthdayString *string `json:"birthday" validate:"required,len=10"`
	Password       *string `json:"password" validate:"required,min=1,max=255"`
	Username       *string `json:"username" validate:"required,min=1,max=100"`
}
