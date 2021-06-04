#!/bin/bash
: "${PROJECT_NAME:=celery-operational-error}"

if  docker ps | grep " $PROJECT_NAME$"; then
    echo "Container already started. Do nothing"
elif docker ps -a |grep " $PROJECT_NAME$" ; then
    docker start $PROJECT_NAME
else
  docker run -i -d \
            -v `pwd`:/opt/$PROJECT_NAME \
            --add-host=host.docker.internal:host-gateway \
            --name $PROJECT_NAME \
            -t $PROJECT_NAME:latest \
            /bin/bash
  docker exec -i -t $PROJECT_NAME poetry install
fi
