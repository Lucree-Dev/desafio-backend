package services

import (
	"account/internal/domain"
	"account/internal/domain/ports/inbounds"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories"
	"fmt"
)

type CardServicePortImpl struct {
	CardRepositoryPort   outbounds.CardRepositoryPort
	PersonRepositoryPort outbounds.PersonRepositoryPort
}

func (c *CardServicePortImpl) Create(personId int, card domain.Card) (*domain.Card, error) {
	person := c.PersonRepositoryPort.Find(personId)
	if person == nil {
		return nil, fmt.Errorf("person not found")
	}
	return c.CardRepositoryPort.Create(personId, card), nil
}

func (c *CardServicePortImpl) Update(personId, id int, card domain.Card) (*domain.Card, error) {
	foundPerson := c.PersonRepositoryPort.Find(personId)
	if foundPerson == nil {
		return nil, fmt.Errorf("person not found")
	}
	foundCard := c.CardRepositoryPort.FindById(id)
	if foundCard == nil {
		return nil, fmt.Errorf("card not found")
	}
	cardBelongsToUser := c.CardRepositoryPort.ExistsByPersonIdAndId(personId, id)
	if cardBelongsToUser {
		return c.CardRepositoryPort.Update(personId, id, card), nil
	}
	return nil, fmt.Errorf("change not allowed for the informed card")
}

func NewCardServicePort() inbounds.CardServicePort {
	return &CardServicePortImpl{
		CardRepositoryPort:   repositories.NewCardRepositoryPort(),
		PersonRepositoryPort: repositories.NewPersonRepositoryPort(),
	}
}
