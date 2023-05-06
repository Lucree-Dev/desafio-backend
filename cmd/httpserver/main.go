package main

// import "account/internal/application/server"

// func main() {
// 	server.Start()
// }

import (
	"context"
	"fmt"

	"github.com/go-pg/pg/v10"
)

type Person struct {
	Id        int    `pg:"id"`
	FirstName string `pg:"first_name"`
	LastName  string `pg:"last_name"`
	Birthday  string `pg:"birthday"`
	Password  string `pg:"password"`
}

func main() {
	opt, err := pg.ParseURL("postgres://postgres:admin@localhost:5432/accountDb?sslmode=disable") //TODO Puxar as infos de banco pelo arquivo application.yml
	if err != nil {
		panic(err)
	}

	db := pg.Connect(opt)

	defer db.Close()

	ctx := context.Background()

	if err := db.Ping(ctx); err != nil {
		panic(err)
	}

	person := &Person{
		FirstName: "João",
		LastName:  "joao@example.com",
		Birthday:  "06/05/2023",
		Password:  "123456",
	}
	_, err = db.Model(person).Insert()
	if err != nil {
		panic(err)
	}

	var persons []Person
	err = db.Model(&persons).Select()
	if err != nil {
		panic(err)
	}
	fmt.Println(persons)
}
