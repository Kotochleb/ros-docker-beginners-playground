cmake_minimum_required(VERSION 2.8.3)
project(demo_package)


catkin_package(
)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

install(DIRECTORY launch
	DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

install(DIRECTORY scripts
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
  USE_SOURCE_PERMISSIONS
)