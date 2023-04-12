package api

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

// healthcheck
func (s *server) healthcheck(c echo.Context) error {
	return c.String(http.StatusOK, "OK")
}
