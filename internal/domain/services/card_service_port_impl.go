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

func (c *CardServicePortImpl) Create(card domain.Card) *domain.Card {
	return c.CardRepositoryPort.Create(card)
}

func NewCardServicePort() inbounds.CardServicePort {
	return &CardServicePortImpl{CardRepositoryPort: repositories.NewCardRepositoryPort()}
}
