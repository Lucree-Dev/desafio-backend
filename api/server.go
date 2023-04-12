package api

import (
	"database/sql"
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"

	"github.com/ravilock/desafio-backend-lucree/database"
)

type Server interface {
	http.Handler
	Start(serverAddress string)
}

type server struct {
	*echo.Echo
	db *sql.DB
}

func (s *server) Start(serverAddress string) {
	s.Echo.Start(serverAddress)
}

func NewServer(mongoURI string) (Server, error) {
	databaseClient, err := database.ConnectDatabase(mongoURI)
	if err != nil {
		panic(err)
	}
	defer database.DisconnectDatabase(databaseClient)
	database.TestDatabase(databaseClient)

	return serverFromDatabase(databaseClient)
}

func serverFromDatabase(databaseClient *sql.DB) (Server, error) {
	echoInstance := echo.New()

	server := &server{
		Echo: echoInstance,
		db:   databaseClient,
	}

	// Middleware
	server.Echo.Use(middleware.Logger())
	server.Echo.Use(middleware.Recover())

	// Routes
	server.Echo.GET("/", server.healthcheck)

	return server, nil
}
