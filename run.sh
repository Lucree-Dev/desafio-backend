#!/bin/bash
echo "Up Containers - Postgres"
docker-compose up -d db
echo "=================================="
echo "Up Containers - Rest-API"
docker-compose up djangoapp
echo "=================================="