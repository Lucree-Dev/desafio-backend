package database

import (
	"database/sql"
	"lucree/src/config"

	_ "github.com/go-sql-driver/mysql"
)

//Connect to the database
func Connect() (*sql.DB, error) {

	db, err := sql.Open("mysql", config.Conn)
	if err != nil {
		return nil, err
	}

	if err = db.Ping(); err != nil {
		db.Close()
		return nil, err
	}

	return db, nil

}
