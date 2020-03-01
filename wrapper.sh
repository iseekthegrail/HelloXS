#!/bin/bash
# Container name
container_name="di2020_wojke"
# Stop contianer
docker stop $container_name
sleep 5
# Delete contianer
docker rm -f $container_name
sleep 5
# Build container
docker image build -t $container_name .
# Run container
docker run --rm -ti --name $container_name
# Cleanup
docker system prune -f
