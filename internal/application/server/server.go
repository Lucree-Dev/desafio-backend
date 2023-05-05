package server

import (
	"github.com/labstack/echo/v4"
)

func Start() {
	e := echo.New()

	RegisterEndPoints(e)

	e.Start(":8080") //TODO pegar a porta definida no arquivo application
}
