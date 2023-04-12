package database

import (
	"database/sql"

	_ "github.com/lib/pq"
)

func ConnectDatabase(databaseURI string) (*sql.DB, error) {
	return sql.Open("postgres", databaseURI)
}

func DisconnectDatabase(client *sql.DB) {
	if err := client.Close(); err != nil {
		panic(err)
	}
}

func TestDatabase(client *sql.DB) {
	if err := client.Ping(); err != nil {
		panic(err)
	}
}
