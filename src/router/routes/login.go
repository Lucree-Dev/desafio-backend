package routes

import (
	"lucree/src/controllers"
	"net/http"
)

var routerLogin = Route{
	Url:           "/account/login",
	Method:        http.MethodPost,
	Function:      controllers.Login,
	LoginRequired: false,
}
