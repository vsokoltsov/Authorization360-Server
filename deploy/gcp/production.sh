#!/bin/bash

touch .env.production
echo "POSTGRES_USER=$POSTGRES_GCP_USER" >> .env.production
echo "POSTGRES_PASSWORD=$POSTGRES_GCP_PASSWORD" >> .env.production
echo "POSTGRES_DB=$POSTGRES_GCP_DB" >> .env.production
echo "POSTGRES_HOST=$POSTGRES_GCP_HOST" >> .env.production
echo "JWT_SECRET=$JWT_GCP_SECRET" >> .env.production