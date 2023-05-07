package repositories

import (
	"account/internal/domain"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories/config"
	"account/internal/infrastructure/repositories/entities"
	"account/pkg/log"
	"strconv"
)

type PersonRepositoryPortImpl struct{}

func (p *PersonRepositoryPortImpl) Create(person domain.Person) *domain.Person {
	conn := config.OpenConnection()
	defer conn.Close()

	personEntity := entities.NewPersonFull(
		person.FirstName,
		person.LastName,
		person.EncryptPassword(),
		person.UserName,
		person.Birthday,
	)
	_, err := conn.Model(personEntity).Insert()

	if err != nil {
		panic(err)
	}

	personDomain := domain.NewPersonFull(
		personEntity.Id,
		personEntity.FirstName,
		personEntity.LastName,
		personEntity.Password,
		person.UserName,
		personEntity.Birthday,
	)

	log.Info("ID gerado: " + strconv.Itoa(personEntity.Id))

	return personDomain
}

func NewPersonRepositoryPort() outbounds.PersonRepositoryPort {
	return &PersonRepositoryPortImpl{}
}
