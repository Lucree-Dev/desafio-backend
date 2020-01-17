package cmd

import (
	"fmt"
	"log"
	"net/http"

	"github.com/n0bode/desafio-backend/api"
	"github.com/n0bode/desafio-backend/internal/util"
)

func Run() (err error) {
	log.Println("Starting API")
	api := api.New()
	route := api.Route()

	host := util.GetEnv("API_HOST", "")
	port := util.GetEnv("API_PORT", "8080")

	address := fmt.Sprintf("%s:%s", host, port)
	log.Println("Listerning on localhost:8080")
	if err = http.ListenAndServe(address, route); err != nil {
		log.Fatal(err)
	}
	return
}
