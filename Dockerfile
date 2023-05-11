FROM python:3.9.11-slim-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


RUN apt-get update && apt-get install -y --no-install-recommends gcc python3-dev musl-dev build-essential libpq-dev

RUN mkdir /desafio
WORKDIR /desafio
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' entrypoint.sh
RUN chmod +x ./entrypoint.sh
COPY . .
EXPOSE 8000
#CMD python manage.py makemigrations && python manage.py migrate
