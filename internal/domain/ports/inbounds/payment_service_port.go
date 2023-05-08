package inbounds

import "account/internal/domain"

type PaymentServicePort interface {
	Create(personId int, payment domain.Payment) (*domain.Payment, error)
	GetAllByPersonId(personId int) ([]domain.Payment, error)
}
