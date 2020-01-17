FROM golang
WORKDIR /go/src/github.com/n0bode/desafio-backend
COPY setup.sh .
ENV TERM=xterm-256color
RUN chmod 777 setup.sh
RUN /bin/bash setup.sh
CMD go run .