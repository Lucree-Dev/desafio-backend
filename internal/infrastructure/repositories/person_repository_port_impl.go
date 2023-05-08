package repositories

import (
	"account/internal/domain"
	"account/internal/domain/ports/outbounds"
	"account/internal/infrastructure/repositories/config"
	"account/internal/infrastructure/repositories/entities"
	"account/pkg/log"
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

	log.Info(
		"entity",
		personEntity,
		"Information before being persisted",
	)

	_, err := conn.Model(personEntity).Insert()

	if err != nil {
		panic(err)
	}

	log.Info(
		"id",
		personEntity.Id,
		"Id that was generated after recording in the database",
	)

	return domain.NewPersonFull(
		personEntity.Id,
		personEntity.FirstName,
		personEntity.LastName,
		personEntity.Password,
		personEntity.UserName,
		personEntity.Birthday,
	)
}

func (p *PersonRepositoryPortImpl) Find(id int) *domain.Person {
	conn := config.OpenConnection()
	defer conn.Close()

	var personEntity entities.Person
	query := conn.Model(&personEntity).Where("id = ?", id)

	log.Info(
		"query",
		"where id = ?",
		"Searching by id",
	)

	foundPerson, err := query.Exists()

	if err != nil {
		panic(err)
	}
	if !foundPerson {
		return nil
	}

	err = query.Select()
	if err != nil {
		panic(err)
	}

	return domain.NewPersonFull(
		personEntity.Id,
		personEntity.FirstName,
		personEntity.LastName,
		personEntity.Password,
		personEntity.UserName,
		personEntity.Birthday,
	)
}

func NewPersonRepositoryPort() outbounds.PersonRepositoryPort {
	return &PersonRepositoryPortImpl{}
}
