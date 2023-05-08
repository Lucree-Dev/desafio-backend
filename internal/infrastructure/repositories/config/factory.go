package config

import (
	"github.com/go-pg/pg/v10"
)

type Factory interface {
	newConnection() (*pg.DB, error)
}

type PgConnectionFactory struct {
	Options *pg.Options
}

func (factory *PgConnectionFactory) newConnection() (*pg.DB, error) {
	return pg.Connect(factory.Options), nil
}

func newPgConnectionFactory(options *pg.Options) *PgConnectionFactory {
	return &PgConnectionFactory{Options: options}
}
