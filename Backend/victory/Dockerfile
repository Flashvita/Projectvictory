FROM python:3.8

ARG ip
ENV IP_ADDR=$ip

COPY . /.

RUN pip3 install -r requirements.txt

ENTRYPOINT bash init.sh ${IP_ADDR}
