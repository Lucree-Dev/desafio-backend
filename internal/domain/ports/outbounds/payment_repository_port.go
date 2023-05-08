package outbounds

import "account/internal/domain"

type PaymentRepositoryPort interface {
	Create(personId int, payment domain.Payment) *domain.Payment
	FindAllByPersonId(personId int) []domain.Payment
}
