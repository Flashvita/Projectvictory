#!/bin/bash

CONTAINER_NAME=$1
OUTPUT=$(docker ps | awk '{print $17}')

if [ $OUTPUT == $CONTAINER_NAME ]; then
	docker stop ${CONTAINER_NAME}
else
	echo "контейнер не запущен"
fi