package test

import (
	"bytes"
	"encoding/json"
	"net/http"
	"testing"

	"github.com/n0bode/desafio-backend/internal/models"
)

func TestRouteAccountPerson(t *testing.T) {
	account := models.Account{
		FirstName: "Forrest",
		LastName:  "Gump",
		Birthday:  "1944-06-06",
		Password:  "Bubba Gump",
		Username:  "ForrestRun",
		UserID:    "70c881d4a26984ddce795f6f71817c9cf4480e79",
	}

	t.Run("Create Account", func(t0 *testing.T) {
		var buffer bytes.Buffer
		if err := json.NewEncoder(&buffer).Encode(&account); err != nil {
			t.Error(err)
		}

		resp, err := http.Post("http://localhost:8080/account/person", "application/json", &buffer)
		if err != nil {
			t.Error(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusCreated {
			t.Error("Cannot create Account")
		}
	})

	t.Run("Force Fail", func(t0 *testing.T) {

	})
}
