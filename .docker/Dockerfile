FROM golang:1.20

# Install Golang-migrate with PostgreSQL support
# RUN go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@v4.15.2

# Set the working directory to /app
WORKDIR /app

COPY . .

# RUN migrate -path=.docker/migrations -database "postgres://postgres:admin@postgresql:5432/accountDb?sslmode=disable" up

RUN go build -o account cmd/httpserver/main.go

EXPOSE 8080

CMD ["./account"]