package services

import (
	"account/internal/domain"
	"account/internal/domain/ports/inbounds"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories"
)

type CardServicePortImpl struct {
	CardRepositoryPort outbounds.CardRepositoryPort
}

func (c *CardServicePortImpl) Create(personId int, card domain.Card) *domain.Card {
	//TODO Colocar validação para verificar se o usuário existe ou não
	return c.CardRepositoryPort.Create(personId, card)
}

func NewCardServicePort() inbounds.CardServicePort {
	return &CardServicePortImpl{CardRepositoryPort: repositories.NewCardRepositoryPort()}
}
