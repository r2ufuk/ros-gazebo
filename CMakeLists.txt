cmake_minimum_required(VERSION 3.0.2)

project(demo)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  gazebo_msgs
  gazebo_ros
)

find_package(gazebo REQUIRED)

include_directories(include ${catkin_INCLUDE_DIRS} ${GAZEBO_INCLUDE_DIRS} ${SDFormat_INCLUDE_DIRS})

catkin_package(
    DEPENDS
      gazebo_ros
    CATKIN_DEPENDS
    INCLUDE_DIRS
    LIBRARIES
)