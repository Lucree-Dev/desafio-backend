package controllers

import (
	requestDTO "account/internal/application/dtos/request"
	responseDTO "account/internal/application/dtos/response"
	"account/internal/application/response"
	"account/internal/domain"
	"account/internal/domain/services"
	"strconv"

	"github.com/labstack/echo/v4"
)

func CreatePerson(context echo.Context) error {
	personServicePort := services.NewPersonServicePort()

	person := requestDTO.NewPerson()
	if err := context.Bind(person); err != nil {
		return err
	}

	personCreated := personServicePort.Create(
		domain.NewPersonPartial(
			person.FirstName,
			person.LastName,
			person.Password,
			person.Birthday,
		),
	)

	context.Response().Header().Set("Location", strconv.Itoa(personCreated.Id))
	return response.Created(context,
		responseDTO.NewPerson(
			personCreated.FirstName,
			personCreated.LastName,
			personCreated.Birthday,
		),
	)
}
