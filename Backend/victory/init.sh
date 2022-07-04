#!/bin/bash

SERVER_IP=$1

set -e

python3 manage.py makemigrations mainapp
python3 manage.py migrate
echo yes | python3 manage.py collectstatic

default_admin=$("from django.contrib.auth import get_user_model; User = get_user_model(); admin=User.objects.get(username='admin'); print(admin)" | python manage.py shell)

if [ $default_admin=='admin' ]; then
    echo 'admin is exsist'
else
    echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@main.ru', 'admin')" | python manage.py shell
fi

gunicorn -b ${SERVER_IP}:8000 victory.wsgi:application
