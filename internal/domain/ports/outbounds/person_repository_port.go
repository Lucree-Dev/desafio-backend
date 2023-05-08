package outbounds

import "account/internal/domain"

type PersonRepositoryPort interface {
	Create(person domain.Person) *domain.Person
	Find(id int) *domain.Person
}
