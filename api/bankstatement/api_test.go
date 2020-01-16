package bankstatement

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

func TestRouteBankStatement(t *testing.T) {
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
		TOKEN = response.Data["token"].(string)
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

	if resp.StatusCode != http.StatusOK {
		t.Fatal()
	}
}
