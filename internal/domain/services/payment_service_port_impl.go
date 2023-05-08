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
	friend := c.PersonRepositoryPort.Find(payment.FriendId)
	if friend == nil {
		return nil, fmt.Errorf("friend not found")
	}
	card := c.CardRepositoryPort.FindById(payment.CardId)
	if card == nil {
		return nil, fmt.Errorf("card not found")
	}
	cardBelongsToUser := c.CardRepositoryPort.ExistsByPersonIdAndId(personId, payment.CardId)
	if !cardBelongsToUser {
		return nil, fmt.Errorf("transfer not allowed for the informed card")
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
