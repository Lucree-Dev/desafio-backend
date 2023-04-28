#!/bin/bash
echo "Build Postgresql"
docker-compose up -d db
echo "=================================="
echo "Build Application"
docker-compose build
