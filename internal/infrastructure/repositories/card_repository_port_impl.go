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

func (c *CardRepositoryPortImpl) Create(personId int, card domain.Card) *domain.Card {
	conn := config.OpenConnection()
	defer conn.Close()

	cardEntity := entities.NewCard(
		card.Title,
		card.CardNumber(),
		card.ExpireMonth,
		card.ExpireYear,
		card.EncryptSecurityCode(),
		personId,
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
		cardEntity.Date,
	)
}

func (c *CardRepositoryPortImpl) Update(personId, id int, card domain.Card) *domain.Card {
	conn := config.OpenConnection()
	defer conn.Close()

	cardEntity := entities.NewCard(
		card.Title,
		card.CardNumber(),
		card.ExpireMonth,
		card.ExpireYear,
		card.EncryptSecurityCode(),
		personId,
	)
	_, err := conn.Model(cardEntity).Where("id = ?", id).Update()

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
		cardEntity.Date,
	)
}

func NewCardRepositoryPort() outbounds.CardRepositoryPort {
	return &CardRepositoryPortImpl{}
}
