package server

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func RegisterEndPoints() *echo.Echo {
	e := echo.New()

	e.GET("", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})

	return e
}
