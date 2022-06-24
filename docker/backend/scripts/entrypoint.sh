#!/bin/sh

python manage.py migrate --no-input
python manage.py wait_for_db --no-input
python manage.py collectstatic --no-input

gunicorn Push_Insights.wsgi:application --bind 0.0.0.0:8000


