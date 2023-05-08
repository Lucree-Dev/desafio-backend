package inbounds

import "account/internal/domain"

type PersonServicePort interface {
	Create(person domain.Person) *domain.Person
}
