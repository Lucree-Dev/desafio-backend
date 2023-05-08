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

func CreatePayment(context echo.Context) error {
	paymentServicePort := services.NewPaymentServicePort()

	requestPayment := requestDTO.NewPaymentDefault()
	if err := context.Bind(requestPayment); err != nil {
		return err
	}

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	paymentCreated, err := paymentServicePort.Create(
		personId,
		domain.NewPayment(
			requestPayment.FriendId,
			requestPayment.BillingCard.CardId,
			personId,
			requestPayment.Value,
		),
	)

	if err != nil {
		return response.NotFound(context, err.Error())
	}

	return response.Created(context,
		responseDTO.NewPayment(
			paymentCreated.FriendId,
			paymentCreated.CardId,
			paymentCreated.Value,
		),
		paymentCreated.Id,
	)
}
