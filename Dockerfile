FROM python:3.11-alpine

WORKDIR /code

RUN apk update && apk add sqlite sqlite-dev

COPY . .

RUN python database/scriptSQL.py

CMD ["python", "main.py"]