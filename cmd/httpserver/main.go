package main

// import "account/internal/application/server"

// func main() {
// 	server.Start()
// }

import (
	"account/internal/domain"
	"account/internal/domain/services"
)

func main() {

	service := services.NewPersonServicePort()
	service.Create(domain.Person{
		FirstName: "João",
		LastName:  "joao@example.com",
		Birthday:  "2023-06-06",
		Password:  "123456",
	})

}
