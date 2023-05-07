package inbounds

import "account/internal/domain"

type CardServicePort interface {
	Create(personId int, card domain.Card) (*domain.Card, error)
	Update(personId, id int, card domain.Card) (*domain.Card, error)
}
