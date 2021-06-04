#!/bin/bash

: "${PROJECT_NAME:=celery-operational-error}"

docker exec -i -t $PROJECT_NAME `echo "${@:1}"`
