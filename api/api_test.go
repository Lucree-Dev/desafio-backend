package api

import (
	"bytes"
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"testing"
	"time"

	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"
)

var (
	TOKEN string
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
		FirstName: "Forrest",
		LastName:  "Gump",
		Birthday:  "2560-00-850",
		Username:  randWord(),
	}
	result := make(map[string]interface{})

	t.Run("Create", func(t0 *testing.T) {
		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Error(err)
		}

		resp, err := http.Post("http://"+util.Address()+"/account/person", "application/json", &b)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if err = json.NewDecoder(resp.Body).Decode(&result); err != nil {
			t0.Fatal(err)
		}

		if resp.StatusCode != http.StatusCreated {
			t0.Fatal(result["message"])
		}
	})

	t.Run("UserExists", func(t0 *testing.T) {
		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Error(err)
		}

		resp, err := http.Post("http://"+util.Address()+"/account/person", "application/json", &b)
		if err != nil {
			t0.Fatal(err)
		}
		defer resp.Body.Close()

		if err = json.NewDecoder(resp.Body).Decode(&result); err != nil {
			t0.Fatal(err)
		}

		if resp.StatusCode == http.StatusOK {
			t.Fail()
		}
	})

	t.Run("Missing Field", func(t0 *testing.T) {
		account.Password = ""
		var b bytes.Buffer
		if err := json.NewEncoder(&b).Encode(account); err != nil {
			t0.Fatal(err)
		}

		resp, err := http.Post("http://"+util.Address()+"/account/person", "application/json", &b)
		if err != nil {
			t0.Fatal(err)
		}

		if resp.StatusCode == http.StatusOK {
			t.Fail()
		}
	})
}

func TestRouteFriends(t *testing.T) {
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

		var response util.Response
		json.NewDecoder(resp.Body).Decode(&response)
		TOKEN = response.Data.(string)
	})

	req, err := http.NewRequest("GET", "http://"+util.Address()+"/account/friends", nil)
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

	if resp.StatusCode != http.StatusOK {
		t.Fail()
	}

	var response util.Response
	if err = json.NewDecoder(resp.Body).Decode(&response); err != nil {
		t.Fatal(err)
	}

	if len(response.Data.([]interface{})) == 0 {
		t.Fail()
	}
}

func TestRoutePostCard(t *testing.T) {
	var body bytes.Buffer
	if err := json.NewEncoder(&body).Encode(models.CreditCard{
		CardID:       util.EncodeToSha256(randWord()),
		Title:        "Card Test",
		Pan:          util.EncodeToSha256(randWord()),
		ExpiryYYYY:   "2049",
		ExpiryMM:     "03",
		SecurityCode: "595",
		Date:         "2049",
	}); err != nil {
		t.Error(err)
	}

	req, err := http.NewRequest("POST", "http://"+util.Address()+"/account/card", &body)
	if err != nil {
		t.Fatal(err)
	}

	//Set token to header
	req.Header.Set("Authorization", "Bearer "+TOKEN)
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		t.Fatal(err)
	}
	defer resp.Body.Close()
	fmt.Println(resp.StatusCode)
	if resp.StatusCode != http.StatusCreated {
		t.Fail()
	}
}
