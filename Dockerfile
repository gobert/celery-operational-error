FROM python:3.9.5-slim-buster

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install curl build-essential openssh-client

ENV WORKDIR /opt/celery-operational-error
WORKDIR $WORKDIR

RUN groupadd --gid 1000 jumbo
RUN adduser --system jumbo --uid 1000 --gid 1000
RUN chown -R jumbo:jumbo $WORKDIR
USER jumbo

# install & configure poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH="/home/jumbo/.poetry/bin:${PATH}"

COPY pyproject.toml poetry.lock  $WORKDIR/

# poetry install
RUN poetry install

# use Dockerignore
COPY --chown=jumbo:jumbo . $WORKDIR
