FROM python:3.12-alpine3.17

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1



RUN apk update && apk add libpq
RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

WORKDIR /usr/src/app

COPY ./requirements.txt ./

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .


RUN python django_backend/manage.py

EXPOSE 8000

#RUN adduser --disable-password backend-user

#USER backend-user
CMD ["sh", "-c", "python django_backend/manage.py makemigrations && python django_backend/manage.py migrate && python django_backend/manage.py runserver 0.0.0.0:8000"]