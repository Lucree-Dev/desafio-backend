package main

import (
	"log"
	"os"

	"github.com/joho/godotenv"

	"github.com/ravilock/desafio-backend-lucree/api"
)

func main() {
	if err := godotenv.Load(); err != nil {
		log.Println("No .env file found")
	}

	databaseURI := os.Getenv("DATABASE_URI")
	if databaseURI == "" {
		log.Fatal("You must sey your 'DATABASE_URI' environmental variable.")
	}

	server, err := api.NewServer(databaseURI)
	if err != nil {
		panic(err)
	}

	server.Start(os.Getenv("SERVER_ADDRESS"))
}
