FROM python:3.11-alpine

WORKDIR /code

COPY . .

RUN apk update && apk add sqlite sqlite-dev

RUN python database/scriptSQL.py

CMD ["python", "main.py"]