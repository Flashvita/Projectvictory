FROM python:3.8

COPY . /server

WORKDIR /server

RUN pip3 install -r requirements

ENTRYPOINT bash init.sh
