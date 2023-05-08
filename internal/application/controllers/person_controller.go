package controllers

import (
	requestDTO "account/internal/application/dtos/request"
	responseDTO "account/internal/application/dtos/response"
	"account/internal/application/response"
	"account/internal/domain"
	"account/internal/domain/services"
	"account/pkg/log"

	"github.com/labstack/echo/v4"
)

func CreatePerson(context echo.Context) error {
	personServicePort := services.NewPersonServicePort()

	log.Info(
		"path",
		"/account/persons",
		"Registering new user",
	)

	requestPerson := requestDTO.NewPerson()
	if err := context.Bind(requestPerson); err != nil {
		return err
	}

	personCreated := personServicePort.Create(
		domain.NewPersonPartial(
			requestPerson.FirstName,
			requestPerson.LastName,
			requestPerson.Password,
			requestPerson.UserName,
			requestPerson.Birthday,
		),
	)

	return response.Created(context,
		responseDTO.NewPerson(
			personCreated.FirstName,
			personCreated.LastName,
			personCreated.UserName,
			personCreated.Birthday,
		),
		personCreated.Id,
	)
}
