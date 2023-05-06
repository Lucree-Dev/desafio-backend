package config

import (
	"context"

	"github.com/go-pg/pg/v10"
)

func OpenConnection() *pg.DB {

	opt, err := pg.ParseURL("postgres://postgres:admin@localhost:5432/accountDb?sslmode=disable") //TODO Puxar as infos de banco pelo arquivo application.yml
	if err != nil {
		panic(err)
	}

	factory := newPgConnectionFactory(opt)

	conn, err := factory.newConnection()
	if err != nil {
		panic(err)
	}

	ctx := context.Background()

	if err := conn.Ping(ctx); err != nil {
		panic(err)
	}

	return conn
}
