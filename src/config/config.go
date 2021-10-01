package config

import (
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/joho/godotenv"
)

var (
	Conn = ""
	Port = 0
	Key  []byte
)

func LoadEnv() {

	var err error

	if err = godotenv.Load(); err != nil {
		log.Fatal(err)
	}

	Port, _ = strconv.Atoi(os.Getenv("API_PORT"))

	Conn = fmt.Sprintf("%s:%s@/%s?loc=Local",
		os.Getenv("DB_USER"),
		os.Getenv("DB_PASSWORD"),
		os.Getenv("DB_DATABASE"),
	)

	Key = []byte(os.Getenv("TOKEN_KEY"))
}
