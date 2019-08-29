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

## Deployment

### Google Cloud Platform

1) Create a service account via Google Cloud IAM
2) Create a JSON key for the selected account
3) Put service account in project folder with `service-account.json` name
4) Add service account to the `gcloud` cli utility via `gcloud auth activate-service-account --key-file service-account.json`

For **Google App Engine** config file located in `/deploy/gcp/app.yml`