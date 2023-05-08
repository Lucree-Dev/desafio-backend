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

func (p *PaymentServicePortImpl) Create(personId int, payment domain.Payment) (*domain.Payment, error) {
	person := p.PersonRepositoryPort.Find(personId)
	if person == nil {
		return nil, fmt.Errorf("person not found")
	}
	friend := p.PersonRepositoryPort.Find(payment.FriendId)
	if friend == nil {
		return nil, fmt.Errorf("friend not found")
	}
	card := p.CardRepositoryPort.FindById(payment.CardId)
	if card == nil {
		return nil, fmt.Errorf("card not found")
	}
	cardBelongsToUser := p.CardRepositoryPort.ExistsByPersonIdAndId(personId, payment.CardId)
	if !cardBelongsToUser {
		return nil, fmt.Errorf("transfer not allowed for the informed card")
	}
	return p.PaymentRepositoryPort.Create(personId, payment), nil
}

func (p *PaymentServicePortImpl) GetAllByPersonId(personId int) ([]domain.Payment, error) {
	person := p.PersonRepositoryPort.Find(personId)
	if person == nil {
		return nil, fmt.Errorf("person not found")
	}
	return p.PaymentRepositoryPort.FindAllByPersonId(personId), nil
}

func NewPaymentServicePort() inbounds.PaymentServicePort {
	return &PaymentServicePortImpl{
		CardRepositoryPort:    repositories.NewCardRepositoryPort(),
		PersonRepositoryPort:  repositories.NewPersonRepositoryPort(),
		PaymentRepositoryPort: repositories.NewPaymentRepositoryPort(),
	}
}
