package repositories

import (
	"account/internal/domain"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories/config"
	"account/internal/infrastructure/repositories/entities"
	"account/pkg/log"
	"strconv"
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
	_, err := conn.Model(paymentEntity).Insert()

	if err != nil {
		panic(err)
	}

	log.Info("ID gerado: " + strconv.Itoa(paymentEntity.Id))

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
