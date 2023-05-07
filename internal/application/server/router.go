package server

import (
	. "account/internal/application/controllers"

	"github.com/labstack/echo/v4"
)

func RegisterEndPoints() *echo.Echo {
	basePath := "/account"
	e := echo.New()

	e.POST(basePath+"/persons", CreatePerson)
	e.POST(basePath+"/persons/:personId/cards", CreateCard)

	return e
}
