#!/bin/bash

: "${CELERY_WORKER_NAME:="celery-worker-"$((1 + $RANDOM % 1000))}"
PYTHONPATH=${PWD}/src poetry run celery -A tasks worker --loglevel=INFO --pool=solo -n $CELERY_WORKER_NAME
