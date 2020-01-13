FROM golang
WORKDIR /go/src/github.com/n0bode/desafio-backend
COPY . .
ENV TERM=xterm-256color
RUN chmod 777 run.sh
RUN bash setup.sh
CMD bash run.sh
