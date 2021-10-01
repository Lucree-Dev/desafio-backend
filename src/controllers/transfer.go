package controllers

import (
	"encoding/json"
	"io/ioutil"
	"lucree/src/database"
	"lucree/src/models"
	"lucree/src/repositories"
	"lucree/src/response"
	"net/http"
)

//Create a new user
func CreateTransfer(w http.ResponseWriter, r *http.Request) {
	body, err := ioutil.ReadAll(r.Body)

	if err != nil {
		response.Erro(w, http.StatusUnprocessableEntity, err)
		return
	}

	var transfer models.Transfer

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	if err := json.Unmarshal([]byte(body), &transfer); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}
	if err = transfer.Prepare(); err != nil {
		response.Erro(w, http.StatusBadRequest, err)
		return
	}

	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	repository := repositories.NewRepositoryTransfer(db)
	transfer.Transfer_id, err = repository.Create(transfer)

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	db.Close()

	response.JSON(w, http.StatusCreated, transfer)

}

func GetAll(w http.ResponseWriter, r *http.Request) {
	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	defer db.Close()

	repository := repositories.NewRepositoryTransfer(db)
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	transfers, err := repository.GetAll()

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	response.JSON(w, http.StatusOK, transfers)
}

func GetTransferByUser(w http.ResponseWriter, r *http.Request) {
	db, err := database.Connect()
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	defer db.Close()

	repository := repositories.NewRepositoryTransfer(db)
	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}
	transfers, err := repository.GetAll()

	if err != nil {
		response.Erro(w, http.StatusInternalServerError, err)
		return
	}

	response.JSON(w, http.StatusOK, transfers)
}
