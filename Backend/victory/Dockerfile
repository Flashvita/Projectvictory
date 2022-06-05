FROM python:3.9

COPY . /server

WORKDIR /server

RUN pip3 install -r requirements

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

ENTRYPOINT python3 manage.py runserver 0.0.0.0:8000
