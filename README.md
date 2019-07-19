## Authorization360

[![CircleCI](https://circleci.com/gh/vsokoltsov/Authorization360-Server.svg?style=svg)](https://circleci.com/gh/vsokoltsov/Authorization360-Server)

Authorization service for teamcircle projects

## Setup

* `docker-compose build`
* `make up`

## Test

* `make test`

## Run migrations

* `make alembic ARGS="upgrade head"`
* `make alembic ARGS="revision -m <revision name>"`

## Compile dependencies

* `make pip_compile`