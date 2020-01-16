package api

import (
	"bytes"
	"encoding/json"
	"io/ioutil"
	"math/rand"
	"net/http"
	"testing"
	"time"

	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"
)

func randWord() (word string) {
	rand.Seed(time.Now().Unix())
	for i := 0; i < 10; i++ {
		word += string(rune(32 + rand.Intn(31)))
	}
	return
}

func TestPostPersonRoute(t *testing.T) {
	account := models.Account{
		UserID:    util.EncodeToSha256(randWord()),
		Password:  "password",
		FirstName: "ForrestGump",
		LastName:  "Gump",
		Birthday:  "2560-00-850",
		Username:  randWord(),
	}

	t.Run("Create", func(t0 *testing.T) {
		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Error(err)
		}

		resp, err := http.Post("http://localhost:8080/account/person", "application/json", &b)
		if err != nil {
			t0.Error(err)
		}

		if resp.StatusCode != http.StatusOK {
			data, _ := ioutil.ReadAll(resp.Body)
			t.Error(string(data))
		}
	})

	t.Run("UserExists", func(t0 *testing.T) {
		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Error(err)
		}

		resp, err := http.Post("http://localhost:8080/account/person", "application/json", &b)
		if err != nil {
			t0.Error(err)
		}

		if resp.StatusCode == http.StatusOK {
			t.Fail()
		}
	})

	t.Run("Missing Field", func(t0 *testing.T) {
		account.Password = ""
		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Error(err)
		}

		resp, err := http.Post("http://localhost:8080/account/person", "application/json", &b)
		if err != nil {
			t0.Error(err)
		}

		if resp.StatusCode == http.StatusOK {
			t.Fail()
		}
	})
}

func TestPostSession(t *testing.T) {
	account := models.Account{
		Username: "Forrest",
		Password: "password",
	}

	var b bytes.Buffer
	if err := json.NewEncoder(&b).Encode(account); err != nil {
		t.Error(err)
	}

	resp, err := http.Post("http://localhost:8080/account/person", "application/json", &b)
	if err != nil {
		t.Error(err)
	}

	if resp.StatusCode != http.StatusOK {
		t.Fail()
	}
}
