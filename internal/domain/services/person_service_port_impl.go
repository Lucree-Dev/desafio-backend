package services

import (
	"account/internal/domain"
	"account/internal/domain/ports/inbounds"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories"
)

type PersonServicePortImpl struct {
	PersonRepositoryPort outbounds.PersonRepositoryPort
}

func (p *PersonServicePortImpl) Create(person domain.Person) *domain.Person {
	return p.PersonRepositoryPort.Create(person)
}

func NewPersonServicePort() inbounds.PersonServicePort {
	return &PersonServicePortImpl{
		PersonRepositoryPort: repositories.NewPersonRepositoryPort(),
	}
}
