FROM husarion/panther-gazebo:noetic-latest

# Use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update Ubuntu packages
RUN apt update \
    && apt upgrade -y

# Install Jupyter Notebook
RUN pip3 install jupyterlab

# Copy demo_package and build it
COPY ./demo_package /app/ros_ws/src/demo_package
RUN cd ros_ws \
    && source /app/ros_ws/devel/setup.bash \
    && catkin_make install

# Clear Ubuntu packages
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* 

# Copy ros_entrypoint.sh
COPY ./docker/ros_entrypoint.sh /