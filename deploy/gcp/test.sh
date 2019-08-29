#!/bin/bash

touch .env
echo "FLASK_ENV=test" >> .env
echo "POSTGRES_USER=$POSTGRES_USER" >> .env
echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> .env
echo "POSTGRES_DB=$POSTGRES_DB" >> .env
echo "POSTGRES_HOST=$POSTGRES_HOST" >> .env
echo "JWT_SECRET=$JWT_SECRET" >> .env