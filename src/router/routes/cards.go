package routes

import (
	"lucree/src/controllers"
	"net/http"
)

var routerCards = []Route{
	{
		Url:           "/account/card",
		Method:        http.MethodPost,
		Function:      controllers.CreateCard,
		LoginRequired: true,
	},

	{
		Url:           "/account/cards",
		Method:        http.MethodGet,
		Function:      controllers.GetCards,
		LoginRequired: true,
	},
}
