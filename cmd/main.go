package main

import (
	"log"
	"net/http"

	"github.com/n0bode/desafio-backend/api"
)

func main() {
	api := api.New()

	log.Println("API listerning at localhost:8080")
	if err := http.ListenAndServe(":8080", api.Route()); err != nil {
		log.Fatal(err)
	}
}
