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

func CreatePayment(context echo.Context) error {
	paymentServicePort := services.NewPaymentServicePort()

	requestPayment := requestDTO.NewPaymentDefault()
	if err := context.Bind(requestPayment); err != nil {
		return err
	}

	log.Info(
		"path",
		"/account/persons/"+context.Param("personId")+"/transfers",
		"Transferring to a friend",
	)

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	paymentCreated, err := paymentServicePort.Create(
		personId,
		domain.NewPaymentPartial(
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

func GetPaymentsByPerson(context echo.Context) error {
	paymentServicePort := services.NewPaymentServicePort()

	log.Info(
		"path",
		"/account/persons/"+context.Param("personId")+"/bank-statements",
		"Listing all user transfers",
	)

	personId, err := strconv.Atoi(context.Param("personId"))
	if err != nil {
		return err
	}

	paymentDomains, err := paymentServicePort.GetAllByPersonId(personId)

	if err != nil {
		return response.NotFound(context, err.Error())
	}

	if paymentDomains == nil {
		return response.Ok(context, []responseDTO.BankStatement{})
	}

	var paymentDtos []responseDTO.BankStatement
	for _, paymentDomain := range paymentDomains {
		paymentDtos = append(
			paymentDtos,
			responseDTO.NewBankStatement(
				paymentDomain.PersonId,
				paymentDomain.FriendId,
				paymentDomain.CardId,
				paymentDomain.Value,
				paymentDomain.Date,
			),
		)
	}

	return response.Ok(context, paymentDtos)
}

func GetPayments(context echo.Context) error {
	paymentServicePort := services.NewPaymentServicePort()

	log.Info(
		"path",
		"/account/bank-statements",
		"Listing all app downloads",
	)

	paymentDomains := paymentServicePort.GetAll()

	if paymentDomains == nil {
		return response.Ok(context, []responseDTO.BankStatement{})
	}

	var paymentDtos []responseDTO.BankStatement
	for _, paymentDomain := range paymentDomains {
		paymentDtos = append(
			paymentDtos,
			responseDTO.NewBankStatement(
				paymentDomain.PersonId,
				paymentDomain.FriendId,
				paymentDomain.CardId,
				paymentDomain.Value,
				paymentDomain.Date,
			),
		)
	}

	return response.Ok(context, paymentDtos)
}
