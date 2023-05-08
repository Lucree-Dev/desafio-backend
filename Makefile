run:
	go run cmd/httpserver/main.go
clean:
	rm -rf out
build: clean
	mkdir -p ./out
	go build -o ./out/account cmd/httpserver/main.go
	cp -r application.yml ./out/
docker-up: clean
	docker-compose up --build
docker-migrate:
	docker exec account-api migrate -path=.docker/migrations -database "postgres://postgres:admin@postgresql:5432/accountDb?sslmode=disable" up