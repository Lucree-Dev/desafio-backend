package session

import (
	"bytes"
	"encoding/json"
	"net/http"
	"testing"

	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"
)

var (
	TOKEN string
)

func TestRouteSession(t *testing.T) {
	account := models.Account{
		Username: "VitoCorleone",
		Password: "Corleone",
	}

	t.Run("Create Session", func(t0 *testing.T) {
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

		var response util.Response
		json.NewDecoder(resp.Body).Decode(&response)
		TOKEN = response.Data.(string)
	})

	t.Run("Failed Field", func(t0 *testing.T) {
		//Field small then 6
		account.Password = "none"

		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Fatal(err)
		}

		resp, err := http.Post("http://"+util.Address()+"/session", "application/json", &b)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode == http.StatusCreated {
			t0.Fail()
		}
	})

	t.Run("User doesnt exists", func(t0 *testing.T) {
		account.Password = "123456"

		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Fatal(err)
		}

		resp, err := http.Post("http://"+util.Address()+"/session", "application/json", &b)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode == http.StatusCreated {
			t0.Fail()
		}
	})
}

func TestDeleteSession(t *testing.T) {
	t.Run("Logout", func(t0 *testing.T) {
		req, err := http.NewRequest("DELETE", "http://"+util.Address()+"/session", nil)
		if err != nil {
			t0.Fatal(err)
		}

		req.Header.Set("Authorization", "Bearer "+TOKEN)
		client := &http.Client{}
		resp, err := client.Do(req)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			t0.Fail()
		}
	})

	t.Run("LogoutAgain", func(t0 *testing.T) {
		req, err := http.NewRequest("DELETE", "http://"+util.Address()+"/session", nil)
		if err != nil {
			t0.Fatal(err)
		}

		req.Header.Set("Authorization", "Bearer "+TOKEN)
		client := &http.Client{}
		resp, err := client.Do(req)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusNoContent {
			t0.Fail()
		}
	})

	t.Run("Invalid Token", func(t0 *testing.T) {
		req, err := http.NewRequest("DELETE", "http://"+util.Address()+"/session", nil)
		if err != nil {
			t0.Fatal(err)
		}

		req.Header.Set("Authorization", "Bearer "+TOKEN+"a")
		client := &http.Client{}
		resp, err := client.Do(req)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()
		if resp.StatusCode != http.StatusNonAuthoritativeInfo {
			t0.Fail()
		}
	})
}
