run:
	go run cmd/httpserver/main.go
clean:
	rm -rf out
build: clean
	mkdir -p ./out
	go build -o ./out/account cmd/httpserver/main.go
	cp -r application.yml ./out/
build-linux: clean
	mkdir -p ./out
	env GOOS=linux GOARCH=amd64 go build -o ./out/account cmd/httpserver/main.go
	cp -r application.yml ./out/
docker-up: clean
	docker-compose up --build