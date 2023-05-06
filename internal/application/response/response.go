package response

import (
	"net/http"
	"strconv"

	"github.com/labstack/echo/v4"
)

func success(context echo.Context, status int, i interface{}) error {
	return context.JSON(status, i)
}

func err(context echo.Context, code int, message string) error {
	return context.JSON(code, Error{
		Code:    code,
		Message: message,
	})
}

type Error struct {
	Code    int    `json:"code"`
	Message string `json:"message"`
}

func NotFound(context echo.Context, msg string) error {
	return err(context, http.StatusNotFound, msg)
}

func BadGateway(context echo.Context, msg string) error {
	return err(context, http.StatusBadGateway, msg)
}

func InternalServerError(context echo.Context, msg string) error {
	return err(context, http.StatusInternalServerError, msg)
}

func UnprocessableEntity(context echo.Context, msg string) error {
	return err(context, http.StatusUnprocessableEntity, msg)
}

func Ok(context echo.Context, i interface{}) error {
	return success(context, http.StatusOK, i)
}

func Created(context echo.Context, i interface{}, id int) error {
	context.Response().Header().Set("Location", strconv.Itoa(id))
	return success(context, http.StatusCreated, i)
}

func Conflict(context echo.Context, msg string) error {
	return err(context, http.StatusConflict, msg)
}

func NoContent(context echo.Context) error {
	return context.NoContent(http.StatusNoContent)
}
