package config

import (
	"database/sql"

	_ "github.com/lib/pq"
)

var DatabaseClient *sql.DB

func ConnectDatabase(databaseURI string) {
	var err error
	DatabaseClient, err = sql.Open("postgres", databaseURI)
	if err != nil {
		panic(err)
	}
}

func DisconnectDatabase() {
	if err := DatabaseClient.Close(); err != nil {
		panic(err)
	}
}

func TestDatabase() {
	if err := DatabaseClient.Ping(); err != nil {
		panic(err)
	}
}
