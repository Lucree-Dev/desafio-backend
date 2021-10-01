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
func CreatePerson(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)

	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
		return
	}

	var person models.Person

	if err := json.Unmarshal(body, &person); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}
	if err = person.Prepare(); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}

	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	repository := repositories.NewRepositoryPerson(db)
	person.User_id, err = repository.Create(person)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	db.Close()

	response.JSON(w, http.StatusCreated, person)

}

func Friends(w http.ResponseWriter, r *http.Request) {
	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	defer db.Close()

	repository := repositories.NewRepositoryPerson(db)
	person_id, err := service.ExtractUserID(r)
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	friends, err := repository.GetFriends(person_id)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	response.JSON(w, http.StatusOK, friends)
}
