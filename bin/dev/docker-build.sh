#!/bin/bash
: "${PROJECT_NAME:=celery-operational-error}"

docker build -t $PROJECT_NAME:latest .
