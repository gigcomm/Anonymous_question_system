FROM python:3.12-alpine

# Устанавливаем зависимости системы, необходимые для сборки некоторых Python пакетов
RUN apk update && apk add --no-cache \
    build-base \
    libpq-dev \
    postgresql-dev

WORKDIR /usr/src/app

COPY requirements_celery.txt ./
RUN pip install --no-cache-dir -r requirements_celery.txt

COPY . .
CMD ["sh", "-c", "if [ \"$CELERY_BEAT\" = \"true\" ]; then celery -A celery_app beat --loglevel=info; else celery -A celery_app worker --loglevel=info; fi"]