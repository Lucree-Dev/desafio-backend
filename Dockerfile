FROM python:3

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

CMD [ "uvicorn", "main:server" ]