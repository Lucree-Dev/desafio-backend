package main

// import "account/internal/application/server"

// func main() {
// 	server.Start()
// }

import (
	"fmt"

	"account/internal/infrastructure/repositories/config"
	. "account/internal/infrastructure/repositories/entities"
)

func main() {

	conn := config.OpenConnection()
	defer conn.Close()

	person := &Person{
		FirstName: "João",
		LastName:  "joao@example.com",
		Birthday:  "2023-06-06",
		Password:  "123456",
	}
	_, err := conn.Model(person).Insert()
	if err != nil {
		panic(err)
	}

	var persons []Person
	err = conn.Model(&persons).Select()
	if err != nil {
		panic(err)
	}
	fmt.Println(persons)
}
