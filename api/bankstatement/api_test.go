package bankstatement

import (
	"bytes"
	"encoding/json"
	"net/http"
	"testing"

	"github.com/go-playground/validator"
	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"
)

var (
	TOKEN string
)

func TestRouteBankStatement(t *testing.T) {
	valid := validator.New()

	t.Run("Create Session", func(t0 *testing.T) {
		account := models.Account{
			Username: "Tony",
			Password: "Montana",
		}

		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Fatal(err)
		}

		resp, err := http.Post("http://"+util.Address()+"/session", "application/json", &b)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusCreated {
			t0.Fail()
		}

		var response struct {
			Data string `json:"data"`
		}

		json.NewDecoder(resp.Body).Decode(&response)
		TOKEN = response.Data
	})

	req, err := http.NewRequest("GET", "http://"+util.Address()+"/account/bank-statement", nil)
	if err != nil {
		t.Fatal(err)
	}

	req.Header.Set("Authorization", "Bearer "+TOKEN)
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	defer resp.Body.Close()

	var response struct {
		Message string `json:"message"`
		Data    []struct {
			FromCard string `json:"from_card" validate:"required"`
			UserID   string `json:"user_id" validate:"required"`
			FriendID string `json:"friend_id" validate:"required"`
			Value    int    `json:"value" validate:"required"`
			Date     string `json:"date" validate:"required"`
		} `json:"data"`
	}

	if err = json.NewDecoder(resp.Body).Decode(&response); err != nil {
		t.Fatal(err)
	}

	if resp.StatusCode != http.StatusOK {
		t.Fatal()
	}

	for _, transfer := range response.Data {
		if err := valid.Struct(transfer); err != nil {
			t.Fatal(err)
		}
	}
}
