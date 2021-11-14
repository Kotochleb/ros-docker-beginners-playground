# ROS demo

This is simple demo to make it easier to begin with ROS ecosystem. It was written with respect to tools mostly used in industry in 2021 which is year of writing this demo.

> **CAUTION!** Requirements and installation process for used software can be found in [requirements.md](./requirements.md) 

This demo is based on [ROS Noetic](http://wiki.ros.org/noetic) with [Gazebo](http://gazebosim.org/) simulation environment. Whole system is run from [Docker](https://www.docker.com/) with [docker-compose](https://docs.docker.com/compose/). For writing code there is set up [Jupyter Notebook](https://jupyter.org/) running inside docker. 

# Start simulation
## Linux
``` bash
./start_linux.sh
```
For linux PC with Nvidia graphics card and Nvidia Docker 2 installed.
``` bash
./start_linux.sh -n
```

## Windows
``` bash
docker-compose -f docker/docker-compose-windows.yaml up --build
```

## Usage
At start docker will open two windows. One with Gazebo simulation and one with Rviz. Start of Gazebo might take up to two minutes at first so don't worry it takes lot's of time. Jupyter notebook will accessible at [localhost:8888](https://localhost:8888).
> Since jupyter is running from inside docker it will ask you to login. You acn either find token in terminal after starting docker or find similar URL `http://127.0.0.1:8888/?token=b4ea44ee5588161f9801012254065469c2d3316666a777ae` in terminal. This will login you directly into jupyter.



In order to log in to docker's bash run this command:
``` bash
docker container exec -it ros-demo bash
```