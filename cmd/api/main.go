package main

import (
	"log"
	"os"

	"github.com/joho/godotenv"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"

	"github.com/ravilock/desafio-backend-lucree/internal/api/handlers"
	"github.com/ravilock/desafio-backend-lucree/internal/api/routers"
	"github.com/ravilock/desafio-backend-lucree/internal/api/validation"
	"github.com/ravilock/desafio-backend-lucree/internal/config"
)

func main() {
	if err := godotenv.Load(); err != nil {
		log.Println("No .env file found")
	}

	databaseURI := os.Getenv("DATABASE_URI")
	if databaseURI == "" {
		log.Fatal("You must sey your 'DATABASE_URI' environmental variable.")
	}

	config.ConnectDatabase(databaseURI)
	defer config.DisconnectDatabase()
	config.TestDatabase()

	validation.InitValidator()

	echoInstance := echo.New()

	// Middleware
	echoInstance.Use(middleware.Logger())
	echoInstance.Use(middleware.Recover())

	// Healthcheck
	echoInstance.GET("/", handlers.Healthcheck)
	routers.NewAccountRouter(echoInstance)

	echoInstance.Start(os.Getenv("SERVER_ADDRESS"))
}
