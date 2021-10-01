package controllers

import (
	"encoding/json"
	"io/ioutil"
	"lucree/src/database"
	"lucree/src/models"
	"lucree/src/repositories"
	"lucree/src/response"
	"lucree/src/service"
	"net/http"
)

//Create a new user
func CreateCard(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)

	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
		return
	}

	var card models.Card
	card.Person_ID, err = service.ExtractUserID(r)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	if err := json.Unmarshal(body, &card); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}
	if err = card.Prepare(); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}

	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	repository := repositories.NewRepositoryCard(db)
	card.Card_ID, err = repository.Create(card)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	db.Close()

	card.Person_ID = 0
	response.JSON(w, http.StatusCreated, card)

}

func GetCards(w http.ResponseWriter, r *http.Request) {
	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	defer db.Close()

	repository := repositories.NewRepositoryCard(db)
	person_id, err := service.ExtractUserID(r)
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	cards, err := repository.GetAll(person_id)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	response.JSON(w, http.StatusOK, cards)

}
