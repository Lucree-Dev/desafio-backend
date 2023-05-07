package outbounds

import "account/internal/domain"

type CardRepositoryPort interface {
	Create(personId int, card domain.Card) *domain.Card
	Update(personId, id int, card domain.Card) *domain.Card
}
