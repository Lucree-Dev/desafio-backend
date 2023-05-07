package inbounds

import "account/internal/domain"

type CardServicePort interface {
	Create(card domain.Card) *domain.Card
}
