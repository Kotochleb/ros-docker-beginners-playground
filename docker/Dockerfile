FROM husarion/panther-gazebo:noetic-latest

# Use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update Ubuntu packages
RUN apt update \
    && apt upgrade -y

# Install Jupyter Notebook and Jupyter ROS
RUN pip3 install --upgrade pip \
    && pip3 install jupyterlab jupyros

# Copy demo_package
COPY ./demo_package /app/ros_ws/src/demo_package

# Install requirements
RUN pip3 install -r /app/ros_ws/src/demo_package/requirements.txt

# Build demo_package
RUN cd ros_ws \
    && source /app/ros_ws/devel/setup.bash \
    && rosdep install --from-paths src --ignore-src -r -y \
    && catkin_make install

# Clear Ubuntu packages
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* 

# Copy ros_entrypoint.sh
COPY ./docker/ros_entrypoint.sh /