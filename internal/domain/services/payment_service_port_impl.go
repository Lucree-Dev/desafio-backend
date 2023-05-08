package services

import (
	"account/internal/domain"
	"account/internal/domain/ports/inbounds"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories"
	"fmt"
)

type PaymentServicePortImpl struct {
	CardRepositoryPort    outbounds.CardRepositoryPort
	PersonRepositoryPort  outbounds.PersonRepositoryPort
	PaymentRepositoryPort outbounds.PaymentRepositoryPort
}

func (c *PaymentServicePortImpl) Create(personId int, payment domain.Payment) (*domain.Payment, error) {
	person := c.PersonRepositoryPort.Find(personId)
	if person == nil {
		return nil, fmt.Errorf("person not found")
	}
	return c.PaymentRepositoryPort.Create(personId, payment), nil
}

func NewPaymentServicePort() inbounds.PaymentServicePort {
	return &PaymentServicePortImpl{
		CardRepositoryPort:    repositories.NewCardRepositoryPort(),
		PersonRepositoryPort:  repositories.NewPersonRepositoryPort(),
		PaymentRepositoryPort: repositories.NewPaymentRepositoryPort(),
	}
}
