FROM python:3.12-alpine3.17

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1


RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev


RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /usr/src/app

RUN apk del .build-deps

COPY . .

