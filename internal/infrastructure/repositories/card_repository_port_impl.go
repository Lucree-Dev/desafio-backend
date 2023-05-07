package repositories

import (
	"account/internal/domain"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories/config"
	"account/internal/infrastructure/repositories/entities"
	"account/pkg/log"
	"strconv"
)

type CardRepositoryPortImpl struct{}

func (c *CardRepositoryPortImpl) Create(card domain.Card) *domain.Card {
	conn := config.OpenConnection()
	defer conn.Close()

	cardEntity := entities.NewCardPartial(
		card.Title,
		card.Pan,
		card.ExpireMonth,
		card.ExpireYear,
		card.SecurityCode,
	)
	_, err := conn.Model(cardEntity).Insert()

	if err != nil {
		panic(err)
	}

	log.Info("ID gerado: " + strconv.Itoa(cardEntity.Id))

	return domain.NewCardFull(
		cardEntity.Id,
		cardEntity.Title,
		cardEntity.Pan,
		cardEntity.ExpireMonth,
		cardEntity.ExpireYear,
		cardEntity.SecurityCode,
		cardEntity.CreationDate,
	)
}

func NewCardRepositoryPort() outbounds.CardRepositoryPort {
	return &CardRepositoryPortImpl{}
}
