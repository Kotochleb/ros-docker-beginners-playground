#!/bin/bash

source "/opt/ros/$ROS_DISTRO/setup.bash"
source "/app/ros_ws/devel/setup.bash"

jupyter notebook /app/ros_ws/src/demo_package/scripts \
    --port 8888 \
    --allow-root \
    --no-browser \
    --ip=0.0.0.0