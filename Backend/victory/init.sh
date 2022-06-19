#!/bin/bash

SERVER_IP=$1

set -e

python3 manage.py makemigrations mainapp
python3 manage.py migrate
python3 manage.py collectstatic

echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@main.ru', 'admin')" | python manage.py shell

# python3 manage.py runserver 0.0.0.0:8000
gunicorn -b ${SERVER_IP}:8000 victory.wsgi:application
