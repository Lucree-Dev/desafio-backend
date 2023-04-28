#!/bin/bash
echo "Down all Containers - Postgres"
docker-compose stop
echo "=================================="
echo "Remove all volumes - Rest-API"
docker-compose down -v
echo "=================================="