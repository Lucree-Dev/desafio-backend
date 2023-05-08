FROM golang:1.18-alpine

WORKDIR /app

COPY . .

RUN apk add --no-cache git && \
    go mod download

ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB payment_user

RUN apk add --no-cache postgresql-client && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    go get github.com/golang-migrate/migrate/v4/cmd/migrate && \
    migrate -path migrations -database "postgres://postgres:postgres@db:5432/payment_user?sslmode=disable" up && \
    apk --purge del .build-deps

RUN cd cmd && go build -o main .

EXPOSE 5000

CMD ["./cmd/main"]
