## Authorization360

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