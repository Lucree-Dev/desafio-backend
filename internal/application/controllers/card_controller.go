package controllers

import (
	requestDTO "account/internal/application/dtos/request"
	responseDTO "account/internal/application/dtos/response"
	"account/internal/application/response"
	"account/internal/domain"
	"account/internal/domain/services"

	"github.com/labstack/echo/v4"
)

func CreateCard(context echo.Context) error {
	cardServicePort := services.NewCardServicePort()

	requestCard := requestDTO.NewCard()
	if err := context.Bind(requestCard); err != nil {
		return err
	}

	cardCreated := cardServicePort.Create(
		domain.NewCardPartial(
			requestCard.Title,
			requestCard.Pan,
			requestCard.ExpireMonth,
			requestCard.ExpireYear,
			requestCard.SecurityCode,
		),
	)

	return response.Created(context,
		responseDTO.NewCard(
			cardCreated.Title,
			cardCreated.Pan,
			cardCreated.ExpireMonth,
			cardCreated.ExpireYear,
			cardCreated.CreationDate,
		),
		cardCreated.Id,
	)
}
