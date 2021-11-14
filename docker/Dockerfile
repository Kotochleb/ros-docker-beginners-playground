FROM husarion/panther-gazebo:noetic-latest

# Use bash instead of sh
SHELL ["/bin/bash", "-c"]

# Update Ubuntu packages
RUN apt update \
    && apt upgrade -y

# Install Jupyter Notebook and Jupyter ROS
RUN pip3 install --upgrade pip

# Copy demo_package
COPY ./ros_ws /app/demo_ros_ws/src/

# Install requirements
RUN pip3 install -r /app/demo_ros_ws/src/requirements.txt

# Build demo_ros_ws
RUN cd demo_ros_ws \
    && mkdir build \
    && source /opt/ros/$ROS_DISTRO/setup.bash \
    && source /app/ros_ws/devel/setup.bash \
    && rosdep update \
    && rosdep install --from-paths src --ignore-src -r -y \
    && catkin_make install

# For education purpose add sourcing to .bashrc for autofill
RUN echo "source \"/opt/ros/$ROS_DISTRO/setup.bash\"" >> ~/.bashrc \
    && echo "source \"/app/ros_ws/devel/setup.bash\"" >> ~/.bashrc \
    && echo "source \"/app/demo_ros_ws/devel/setup.bash\"" >> ~/.bashrc

# Clear Ubuntu packages
RUN apt clean \
    && rm -rf /var/lib/apt/lists/* 

# Copy ros_entrypoint.sh
COPY ./docker/ros_entrypoint.sh /