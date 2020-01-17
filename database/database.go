package database

import (
	"github.com/n0bode/desafio-backend/database/migration"
	"github.com/n0bode/desafio-backend/internal/util"
	re "gopkg.in/rethinkdb/rethinkdb-go.v6"
)

func New() (db *re.Session) {
	var err error
	db, err = re.Connect(re.ConnectOpts{
		Address:  util.GetEnv("DATABASE_ADDRESS", "localhost:28015"),
		Password: util.GetEnv("DATABASE_PASSWORD", ""),
		Username: util.GetEnv("DATABASE_USER", ""),
		Database: util.GetEnv("DATABASE_NAME", "lucree"),
	})
	if err != nil {
		panic(err)
	}
	migration.MakeMigration(db)
	return
}

func Mock() (mock *re.Mock) {
	return
}
