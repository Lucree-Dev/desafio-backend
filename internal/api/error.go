package api

import (
	"fmt"
	"net/http"

	"github.com/labstack/echo/v4"
)

var UsernameAlreadyUsedError = &echo.HTTPError{
	Code:    http.StatusBadRequest,
	Message: "Username Already Used",
}

var InternalServerError = &echo.HTTPError{
	Code:    http.StatusInternalServerError,
	Message: "An Internal Server Error Ocured",
}

func InvalidFieldError(field string, value any) *echo.HTTPError {
	return &echo.HTTPError{
		Code:    http.StatusBadRequest,
		Message: fmt.Sprintf("%v Is Not Valid For Field %s", value, field),
	}
}
