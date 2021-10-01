package main

import (
	"fmt"
	"log"
	"lucree/src/config"
	"lucree/src/router"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
)

func main() {
	config.LoadEnv()
	r := router.Generate()

	fmt.Printf("server started on port %d", config.Port)
	log.Fatal(http.ListenAndServe(fmt.Sprintf(":%d", config.Port), r))
}
