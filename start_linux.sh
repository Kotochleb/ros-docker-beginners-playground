#!/bin/bash

# display simple help
echo "Run this script with nvidia support by assing -n flag"

# give docker access to display
xhost +local:docker

# build and start docker

if [ "$1" == "-n" ]; then
    echo "Starting docker with nvidia support"
    docker-compose -f docker/docker-compose-linux-nvidia.yaml up --build
else
    echo "Starting docker without nvidia support"
    docker-compose -f docker/docker-compose-linux.yaml up --build
fi

# remove dokcer access to display
xhost +local:docker


