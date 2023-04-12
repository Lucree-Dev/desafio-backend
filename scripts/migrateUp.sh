#!/bin/bash
docker run -v ./migrations/:/migrations --network host migrate/migrate -path=/migrations/ -database postgres://lucree-challenge:lucree-challenge-pass@localhost:5432/lucree-challenge?sslmode=disable up $1
