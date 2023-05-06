package controllers

import (
	"account/internal/application/response"

	"github.com/labstack/echo/v4"
)

func Hello(context echo.Context) error {
	return response.Ok(context, "Hello, World!")
}
