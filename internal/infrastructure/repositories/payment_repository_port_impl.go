package repositories

import (
	"account/internal/domain"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories/config"
	"account/internal/infrastructure/repositories/entities"
	"account/pkg/log"
)

type PaymentRepositoryPortImpl struct{}

func (p *PaymentRepositoryPortImpl) Create(personId int, payment domain.Payment) *domain.Payment {
	conn := config.OpenConnection()
	defer conn.Close()

	paymentEntity := entities.NewPayment(
		payment.FriendId,
		payment.CardId,
		personId,
		payment.Value,
	)

	log.Info(
		"entity",
		paymentEntity,
		"Information before being persisted",
	)

	_, err := conn.Model(paymentEntity).Insert()

	if err != nil {
		panic(err)
	}

	log.Info(
		"id",
		paymentEntity.Id,
		"Id that was generated after recording in the database",
	)

	return domain.NewPaymentFull(
		paymentEntity.Id,
		paymentEntity.FriendId,
		paymentEntity.CardId,
		paymentEntity.PersonId,
		paymentEntity.Value,
		paymentEntity.Date,
	)
}

func (p *PaymentRepositoryPortImpl) FindAllByPersonId(personId int) []domain.Payment {
	conn := config.OpenConnection()
	defer conn.Close()

	var paymentEntities []entities.Payment
	err := conn.Model(&paymentEntities).Where("people_id = ?", personId).Select()
	if err != nil {
		panic(err)
	}

	log.Info(
		"query",
		"where people_id = ?",
		"Searching by people_id",
	)

	var paymentDomains []domain.Payment
	for _, paymentEntity := range paymentEntities {
		paymentDomains = append(
			paymentDomains,
			domain.NewPayment(
				paymentEntity.Id,
				paymentEntity.FriendId,
				paymentEntity.CardId,
				paymentEntity.PersonId,
				paymentEntity.Value,
				paymentEntity.Date,
			),
		)
	}
	return paymentDomains
}

func (p *PaymentRepositoryPortImpl) FindAll() []domain.Payment {
	conn := config.OpenConnection()
	defer conn.Close()

	var paymentEntities []entities.Payment
	err := conn.Model(&paymentEntities).Select()
	if err != nil {
		panic(err)
	}

	var paymentDomains []domain.Payment
	for _, paymentEntity := range paymentEntities {
		paymentDomains = append(
			paymentDomains,
			domain.NewPayment(
				paymentEntity.Id,
				paymentEntity.FriendId,
				paymentEntity.CardId,
				paymentEntity.PersonId,
				paymentEntity.Value,
				paymentEntity.Date,
			),
		)
	}
	return paymentDomains
}

func NewPaymentRepositoryPort() outbounds.PaymentRepositoryPort {
	return &PaymentRepositoryPortImpl{}
}
