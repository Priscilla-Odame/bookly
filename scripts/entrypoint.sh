#!/bin/sh

set -e

# uwsgi --socket :8000 --master --enable-threads --module Push_Insights.wsgi

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

# python manage.py collectstatic --clear
# # python manage.py flush --no-input
# # python manage.py migrate

exec "$@"