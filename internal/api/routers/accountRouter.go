package routers

import (
	"github.com/labstack/echo/v4"

	"github.com/ravilock/desafio-backend-lucree/internal/api/handlers"
)

func NewAccountRouter(echoInstance *echo.Echo) {
	accountGroup := echoInstance.Group("/accounts")
	accountGroup.POST("/person", handlers.CreatePerson)
}
