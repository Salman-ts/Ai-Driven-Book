# Authoritative Sources for Gazebo Sensor Plugins

This document lists primary sources for understanding how to add and configure sensor plugins in Gazebo, as required by Task 1.9.1.

## Primary Sources (Gazebo and SDF Documentation)

1.  **Gazebo Plugins Overview**: A general introduction to the plugin system in Gazebo.
    -   URL: [https://classic.gazebosim.org/tutorials?tut=plugins_hello_world](https://classic.gazebosim.org/tutorials?tut=plugins_hello_world)

2.  **SDF `<sensor>` Tag**: The SDF specification for the `<sensor>` element, which is the container for all sensor properties and plugins.
    -   URL: [http://sdformat.org/spec?ver=1.7&elem=sensor](http://sdformat.org/spec?ver=1.7&elem=sensor)

3.  **Sensor Types**: The SDF specification lists the different types of sensors that can be simulated.
    -   **`camera`**: [http://sdformat.org/spec?ver=1.7&elem=camera](http://sdformat.org/spec?ver=1.7&elem=camera)
    -   **`ray` (for LIDAR/laser)**: [http://sdformat.org/spec?ver=1.7&elem=ray](http://sdformat.org/spec?ver=1.7&elem=ray)
    -   **`imu`**: [http://sdformat.org/spec?ver=1.7&elem=imu](http://sdformat.org/spec?ver=1.7&elem=imu)

4.  **`gazebo_plugins` Repository**: This repository contains the source code for the standard ROS-enabled Gazebo plugins. Examining the source and documentation here is crucial.
    -   URL: [https://github.com/ros-simulation/gazebo_ros_pkgs/tree/humble/gazebo_plugins](https://github.com/ros-simulation/gazebo_ros_pkgs/tree/humble/gazebo_plugins)

5.  **Specific Plugin Details (from `gazebo_plugins`)**:
    -   **GazeboRosCamera**: Simulates a camera and publishes `sensor_msgs/Image` and `sensor_msgs/CameraInfo`.
    -   **GazeboRosLidar**: Simulates a LIDAR and publishes `sensor_msgs/LaserScan`.
    -   **GazeboRosImuSensor**: Simulates an IMU and publishes `sensor_msgs/Imu`.

## Secondary Sources (Tutorials)

1.  **Using Gazebo plugins with ROS**: A ROS 1 tutorial, but the concepts of adding a `<plugin>` tag to the URDF are identical in ROS 2.
    -   URL: [http://wiki.ros.org/gazebo/Tutorials/UsingGazeboPluginsWithROS](http://wiki.ros.org/gazebo/Tutorials/UsingGazeboPluginsWithROS)

2.  **ROS 2 Lidar Tutorial**: A Gazebo tutorial specifically for adding a LIDAR sensor to a robot for ROS 2.
    -   URL: [https://classic.gazebosim.org/tutorials?tut=ros2_lidar](https://classic.gazebosim.org/tutorials?tut=ros2_lidar)

3.  **ROS 2 Camera Tutorial**: A Gazebo tutorial for adding a camera sensor.
    -   URL: [https://classic.gazebosim.org/tutorials?tut=ros2_camera](https://classic.gazebosim.org/tutorials?tut=ros2_camera)
