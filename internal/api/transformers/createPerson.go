package transformers

import (
	"errors"
	"strings"
	"time"

	"github.com/go-playground/validator/v10"
	"github.com/ravilock/desafio-backend-lucree/internal/api"
	"github.com/ravilock/desafio-backend-lucree/internal/api/dtos"
	"github.com/ravilock/desafio-backend-lucree/internal/api/validation"
	"github.com/ravilock/desafio-backend-lucree/internal/app/models"
)

func CreatePerson(dto *dtos.CreatePersonDto) (*models.Person, error) {
	if err := validation.Validate.Struct(dto); err != nil {
		if validationErrors := new(validator.ValidationErrors); errors.As(err, validationErrors) {
			for _, validationError := range *validationErrors {
				return nil, api.InvalidFieldError(validationError.Field(), validationError.Value())
			}
		}
		return nil, err
	}
	*dto.FirstName = strings.TrimSpace(*dto.FirstName)
	*dto.LastName = strings.TrimSpace(*dto.LastName)
	*dto.BirthdayString = strings.TrimSpace(*dto.BirthdayString)
	*dto.Password = strings.TrimSpace(*dto.Password)
	*dto.Username = strings.TrimSpace(*dto.Username)
	if err := validation.Validate.Struct(dto); err != nil {
		return nil, err
	}

	birthday, err := time.Parse("2006-01-02", *dto.BirthdayString)
	if err != nil {
		if validationErrors := new(validator.ValidationErrors); errors.As(err, validationErrors) {
			for _, validationError := range *validationErrors {
				return nil, api.InvalidFieldError(validationError.Tag(), validationError.Value())
			}
		}
		return nil, err
	}

	return &models.Person{
		Id:        new(string),
		FirstName: dto.FirstName,
		LastName:  dto.LastName,
		BirthDay:  &birthday,
		Password:  dto.Password,
		Username:  dto.Username,
	}, nil
}
