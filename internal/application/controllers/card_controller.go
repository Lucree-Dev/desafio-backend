package controllers

import (
	requestDTO "account/internal/application/dtos/request"
	responseDTO "account/internal/application/dtos/response"
	"account/internal/application/response"
	"account/internal/domain"
	"account/internal/domain/services"
	"account/pkg/log"
	"strconv"

	"github.com/labstack/echo/v4"
)

func CreateCard(context echo.Context) error {
	cardServicePort := services.NewCardServicePort()

	requestCard := requestDTO.NewCard()
	if err := context.Bind(requestCard); err != nil {
		return err
	}

	log.Info(
		"path",
		"/account/persons/"+context.Param("personId")+"/cards",
		"Registering a new user card",
	)

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	cardCreated, err := cardServicePort.Create(
		personId,
		domain.NewCardPartial(
			requestCard.Title,
			requestCard.Pan,
			requestCard.ExpireMonth,
			requestCard.ExpireYear,
			requestCard.SecurityCode,
		),
	)

	if err != nil {
		return response.NotFound(context, err.Error())
	}

	return response.Created(context,
		responseDTO.NewCard(
			cardCreated.Title,
			cardCreated.Pan,
			cardCreated.ExpireMonth,
			cardCreated.ExpireYear,
			cardCreated.Date,
		),
		cardCreated.Id,
	)
}

func UpdateCard(context echo.Context) error {
	cardServicePort := services.NewCardServicePort()

	requestCard := requestDTO.NewCard()
	if err := context.Bind(requestCard); err != nil {
		return err
	}

	log.Info(
		"path",
		"/account/persons/"+context.Param("personId")+"/cards/"+context.Param("id"),
		"Changing a User's Card Details",
	)

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	id, err := strconv.Atoi(context.Param("id"))
	if err != nil {
		return err
	}

	cardUpdated, err := cardServicePort.Update(
		personId,
		id,
		domain.NewCardPartial(
			requestCard.Title,
			requestCard.Pan,
			requestCard.ExpireMonth,
			requestCard.ExpireYear,
			requestCard.SecurityCode,
		),
	)

	if err != nil {
		return response.NotFound(context, err.Error())
	}

	return response.Ok(context,
		responseDTO.NewCard(
			cardUpdated.Title,
			cardUpdated.Pan,
			cardUpdated.ExpireMonth,
			cardUpdated.ExpireYear,
			cardUpdated.Date,
		),
	)
}

func DeleteCard(context echo.Context) error {
	cardServicePort := services.NewCardServicePort()

	log.Info(
		"path",
		"/account/persons/"+context.Param("personId")+"/cards/"+context.Param("id"),
		"Deleting a User's Card",
	)

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	id, err := strconv.Atoi(context.Param("id"))
	if err != nil {
		return err
	}

	err = cardServicePort.Delete(personId, id)

	if err != nil {
		return response.NotFound(context, err.Error())
	}

	return response.NoContent(context)
}

func GetCards(context echo.Context) error {
	cardServicePort := services.NewCardServicePort()

	log.Info(
		"path",
		"/account/persons/"+context.Param("personId")+"/cards",
		"Listing all user cards",
	)

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	cardDomains, err := cardServicePort.GetAllByPersonId(personId)

	if err != nil {
		return response.NotFound(context, err.Error())
	}

	if cardDomains == nil {
		return response.Ok(context, []responseDTO.Card{})
	}

	var cardDtos []responseDTO.Card
	for _, cardDomain := range cardDomains {
		cardDtos = append(
			cardDtos,
			responseDTO.NewCard(
				cardDomain.Title,
				cardDomain.Pan,
				cardDomain.ExpireMonth,
				cardDomain.ExpireYear,
				cardDomain.Date,
			),
		)
	}

	return response.Ok(context, cardDtos)
}
