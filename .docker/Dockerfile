FROM golang:1.20

RUN go install -tags 'postgres' github.com/golang-migrate/migrate/v4/cmd/migrate@v4.15.2

WORKDIR /app

COPY . .

RUN go build -o account cmd/httpserver/main.go

EXPOSE 8080

CMD ["./account"]