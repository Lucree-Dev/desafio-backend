package server

import (
	. "account/internal/application/controllers"

	"github.com/labstack/echo/v4"
)

func RegisterEndPoints() *echo.Echo {
	e := echo.New()

	e.POST("/account/persons", CreatePerson)

	return e
}
