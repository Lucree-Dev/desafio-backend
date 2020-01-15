package database

import (
	"github.com/n0bode/desafio-backend/database/migration"
	"github.com/spf13/viper"
	re "gopkg.in/rethinkdb/rethinkdb-go.v6"
)

func New() (db *re.Session) {
	var err error
	db, err = re.Connect(re.ConnectOpts{
		Address:  viper.GetString("database.address"),
		Password: viper.GetString("database.password"),
		Username: viper.GetString("database.user"),
		Database: viper.GetString("database.dbname"),
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
