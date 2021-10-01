package routes

import (
	"lucree/src/controllers"
	"net/http"
)

var routerPersons = []Route{
	{
		Url:           "/account/person",
		Method:        http.MethodPost,
		Function:      controllers.CreatePerson,
		LoginRequired: false,
	},
	{
		Url:           "/account/friends",
		Method:        http.MethodGet,
		Function:      controllers.Friends,
		LoginRequired: true,
	},
}
