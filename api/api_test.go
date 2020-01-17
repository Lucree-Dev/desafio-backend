package api

import (
	"bytes"
	"encoding/json"
	"math/rand"
	"net/http"
	"testing"
	"time"
	"unsafe"

	"github.com/go-playground/validator"

	"github.com/n0bode/desafio-backend/internal/models"
	"github.com/n0bode/desafio-backend/internal/util"
)

var (
	TOKEN   string
	FRIENDS []models.Account
	CARDS   []models.CreditCard
	VALID   *validator.Validate
)

func randWord() (word string) {
	rand.Seed(time.Now().Unix())
	for i := 0; i < 10; i++ {
		word += string(rune(32 + rand.Intn(31)))
	}
	return
}

func init() {
	VALID = validator.New()
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

		response := make(map[string]interface{})
		json.NewDecoder(resp.Body).Decode(&response)
		TOKEN = response["data"].(string)
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

	var response struct {
		Message string `json:"message"`
		Data    []struct {
			FirstName string `json:"first_name" validate:"required"`
			LastName  string `json:"last_name"  validate:"required"`
			Birthday  string `json:"birthday"   validate:"required"`
			Username  string `json:"username"   validate:"required"`
			UserID    string `json:"user_id"    validate:"required"`
		} `json:"data"`
	}

	if err = json.NewDecoder(resp.Body).Decode(&response); err != nil {
		t.Fatal(err)
	}

	for _, friend := range response.Data {
		if err = VALID.Struct(friend); err != nil {
			t.Fatal(err)
		}
		FRIENDS = append(FRIENDS, *(*models.Account)(unsafe.Pointer(&friend)))
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
	if resp.StatusCode != http.StatusCreated {
		t.Fail()
	}
}

func TestRouteGetCard(t *testing.T) {

	req, err := http.NewRequest("GET", "http://"+util.Address()+"/account/cards", nil)
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

	if resp.StatusCode != http.StatusOK {
		t.Fail()
	}

	var response struct {
		Message string              `json:"message"`
		Data    []models.CreditCard `json:"data"`
	}

	if err = json.NewDecoder(resp.Body).Decode(&response); err != nil {
		t.Fatal(err)
	}

	for _, card := range response.Data {
		if err = VALID.Struct(card); err != nil {
			t.Fatal(err)
		}
	}
	CARDS = response.Data
}

func TestRoutePostTransfer(t *testing.T) {
	var body bytes.Buffer
	if err := json.NewEncoder(&body).Encode(models.Transfer{
		FriendID:   FRIENDS[len(FRIENDS)-1].UserID,
		TotalToPay: 8080,
		BillingCard: &models.BillingCard{
			CardID: CARDS[len(CARDS)-1].CardID,
		},
	}); err != nil {
		t.Error(err)
	}

	req, err := http.NewRequest("POST", "http://"+util.Address()+"/account/transfer", &body)
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

	if resp.StatusCode != http.StatusCreated {
		t.Fail()
	}
}
