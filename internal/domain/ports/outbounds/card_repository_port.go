package outbounds

import "account/internal/domain"

type CardRepositoryPort interface {
	Create(card domain.Card) *domain.Card
}
