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

	query := conn.Model(cardEntity).Where("id = ?", id)

	_, err := query.Update()

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

func (c *CardRepositoryPortImpl) ExistsByPersonIdAndId(personId, id int) bool {
	conn := config.OpenConnection()
	defer conn.Close()

	cardEntity := entities.NewCardDefault()
	query := conn.Model(cardEntity).
		Where("id = ?", id).
		Where("people_id = ?", personId)

	foundCard, err := query.Exists()

	if err != nil {
		panic(err)
	}
	return foundCard
}

func (c *CardRepositoryPortImpl) FindById(id int) *domain.Card {
	conn := config.OpenConnection()
	defer conn.Close()

	var cardEntity entities.Card
	query := conn.Model(&cardEntity).Where("id = ?", id)

	foundCard, err := query.Exists()

	if err != nil {
		panic(err)
	}
	if !foundCard {
		return nil
	}

	err = query.Select()
	if err != nil {
		panic(err)
	}

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
