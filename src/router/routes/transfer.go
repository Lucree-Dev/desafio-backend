package routes

import (
	"lucree/src/controllers"
	"net/http"
)

var routerTransfer = []Route{
	{
		Url:           "/account/transfer",
		Method:        http.MethodPost,
		Function:      controllers.CreateTransfer,
		LoginRequired: true,
	},
	{
		Url:           "/account/bank-statement",
		Method:        http.MethodGet,
		Function:      controllers.GetAll,
		LoginRequired: true,
	},
	{
		Url:           "/account/bank-statement/{userId}",
		Method:        http.MethodGet,
		Function:      controllers.GetTransferByUser,
		LoginRequired: true,
	},
}
