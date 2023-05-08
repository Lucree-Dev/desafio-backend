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

func NewPaymentRepositoryPort() outbounds.PaymentRepositoryPort {
	return &PaymentRepositoryPortImpl{}
}
