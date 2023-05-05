package handlers

import (
	"account/pkg/response"

	"github.com/labstack/echo/v4"
)

func Hello(context echo.Context) error {
	return response.Ok(context, "Hello, World!")
}
