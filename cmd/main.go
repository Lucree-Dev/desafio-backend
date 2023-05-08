package main

import (
	"log"
	"net/http"

	db "github.com/Lucree-Dev/desafio-backend/internal/db"
	httpRouter "github.com/Lucree-Dev/desafio-backend/internal/http"
	"github.com/gorilla/mux"
	"github.com/rs/cors"
)

func main() {
	r := mux.NewRouter()
	c := cors.New(cors.Options{
		AllowedOrigins: []string{"*"},
		AllowedMethods: []string{"GET", "POST", "PUT", "DELETE", "OPTIONS"},
	})
	r.Use(c.Handler)

	db, err := db.ConnectDB()
	if err != nil {
		log.Fatalf("Error connecting to database: %v", err)
	}
	defer db.Close()

	httpRouter.Register(r, db)

	log.Print("Starting server on port 5000...")
	if err := http.ListenAndServe(":5000", r); err != nil {
		log.Fatalf("Error starting server: %v", err)
	}
}
