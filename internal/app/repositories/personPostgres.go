package repositories

import (
	"context"
	"database/sql"
	"errors"
	"log"

	"github.com/lib/pq"
	"github.com/ravilock/desafio-backend-lucree/internal/api"
	"github.com/ravilock/desafio-backend-lucree/internal/app/models"
)

const usernameUniqueConstraint = "unique_username"

func CreatePerson(context context.Context, person *models.Person, tx *sql.Tx) error {
	err := tx.QueryRowContext(context,
		`INSERT INTO people
    (first_name, last_name, birthday, password, username)
    VALUES ($1, $2, $3, $4, $5)
    RETURNING id`,
		person.FirstName, person.LastName,
		person.BirthDay, person.Password, person.Username).Scan(person.Id)
	if err != nil {
		log.Println(err)
		if pqErr := new(pq.Error); errors.As(err, &pqErr) {
			if pqErr.Code.Name() == "unique_violation" {
				return api.UsernameAlreadyUsedError
			}
		}
		return api.InternalServerError
	}
	return nil
}
