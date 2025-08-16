FROM python:3.11-alpine

WORKDIR /code

COPY . .

RUN apk update && apk add sqlite sqlite-dev

CMD ["/bin/sh", "-c", "python scriptSQL.py && python main.py"]