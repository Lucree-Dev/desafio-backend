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

// authenticate the user

func Login(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)

	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
		return
	}

	var person models.Person
	if err = json.Unmarshal(body, &person); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}

	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	defer db.Close()

	repository := repositories.NewRepositoryPerson(db)
	personByUsername, err := repository.PersonByUsername(person.Username)
	if err != nil {
		response.Erro(w, http.StatusNotFound, err)
		return
	}

	if err = service.VerifyPassword(personByUsername.Password, person.Password); err != nil {
		response.Erro(w, http.StatusUnauthorized, err)
		return
	}

	token, err := service.CreateToken(uint64(personByUsername.User_id))

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	w.Write([]byte(token))
}
