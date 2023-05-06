package server

import (
	. "account/internal/application/handlers"

	"github.com/labstack/echo/v4"
)

func RegisterEndPoints() *echo.Echo {
	e := echo.New()

	e.GET("", Hello)

	return e
}
