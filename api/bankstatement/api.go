package bankstatement

import (
	"log"
	"net/http"

	"github.com/n0bode/desafio-backend/internal/util"

	"github.com/n0bode/desafio-backend/internal/models"

	re "gopkg.in/rethinkdb/rethinkdb-go.v6"

	"github.com/go-chi/render"

	"github.com/go-chi/chi"
	"github.com/n0bode/desafio-backend/auth"
)

type Api struct {
	auth *auth.TokenAuth
	db   *re.Session
}

func (api *Api) routeGetBankStatement(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)
	util.SetHeaderJson(w)

	claims := api.auth.ClaimsFromContext(r.Context())

	//This reql transform total_to_pay to value
	//And billing_card.card_id from transfer to from_card
	cursor, err := re.Table("transfers").Filter(
		re.Row.Field("user_id").Eq(claims["user_id"]).Or(
			re.Row.Field("friend_id").Eq(claims["user_id"]),
		),
	).Map(func(row re.Term) interface{} {
		return row.Merge(map[string]interface{}{
			"from_card": row.Field("billing_card").Field("card_id"),
			"value":     row.Field("total_to_pay"),
		})
	}).Without("billing_card", "id", "total_to_pay").Run(api.db)

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	transfers := make([]models.Transfer, 0)
	cursor.All(&transfers)

	//Return StatusCreated and Token(JWT)
	resp["message"] = "Success"
	w.WriteHeader(http.StatusOK)
	resp["data"] = transfers
}

func (api *Api) routeGetBankStatementUserID(w http.ResponseWriter, r *http.Request) {
	resp := make(map[string]interface{})
	defer r.Body.Close()
	defer render.JSON(w, r, resp)
	util.SetHeaderJson(w)

	var userID string = chi.URLParam(r, "userId")

	//This reql transform total_to_pay to value
	//And billing_card.card_id from transfer to from_card
	cursor, err := re.Table("transfers").Filter(
		re.Row.Field("user_id").Eq(userID).Or(
			re.Row.Field("friend_id").Eq(userID),
		),
	).Map(func(row re.Term) interface{} {
		return row.Merge(map[string]interface{}{
			"from_card": row.Field("billing_card").Field("card_id"),
			"value":     row.Field("total_to_pay"),
		})
	}).Without("billing_card", "id", "total_to_pay").Run(api.db)

	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		log.Println(err)
		resp["message"] = "Internal Error"
		return
	}

	transfers := make([]models.Transfer, 0)
	cursor.All(&transfers)

	//Return StatusCreated and Token(JWT)
	resp["message"] = "Success"
	w.WriteHeader(http.StatusOK)
	resp["data"] = transfers
}

func (api *Api) Route() (route *chi.Mux) {
	route = chi.NewRouter()

	route.Get("/", api.routeGetBankStatement)
	route.Get("/{userId}", api.routeGetBankStatementUserID)
	return
}

func New(auth *auth.TokenAuth, db *re.Session) (api *Api) {
	return &Api{
		auth: auth,
		db:   db,
	}
}
