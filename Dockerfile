FROM python:3.10
ENV PYTHONUNBUFFERED 1
RUN mkdir /desafio-backend
WORKDIR /desafio-backend
COPY . /desafio-backend/
RUN pip install -r requirements.txt