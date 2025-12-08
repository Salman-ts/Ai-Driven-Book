# Authoritative Sources for ROS 2 Sensor Messages and Visualization

This document lists primary sources for understanding common ROS 2 sensor messages and their visualization in RViz2, as required by Task 1.5.1.

## Primary Sources (Official Documentation)

1.  **`sensor_msgs` Package**: The official documentation for the standard ROS 2 package containing common sensor message definitions.
    -   URL: [https://docs.ros.org/en/humble/p/sensor_msgs/index.html](https://docs.ros.org/en/humble/p/sensor_msgs/index.html)

2.  **Common `sensor_msgs` Types**:
    -   **`sensor_msgs/msg/LaserScan`**: For 2D laser scanners (LIDAR).
        -   URL: [https://docs.ros.org/en/humble/p/sensor_msgs/msg/LaserScan.html](https://docs.ros.org/en/humble/p/sensor_msgs/msg/LaserScan.html)
    -   **`sensor_msgs/msg/Image`**: For camera images.
        -   URL: [https://docs.ros.org/en/humble/p/sensor_msgs/msg/Image.html](https://docs.ros.org/en/humble/p/sensor_msgs/msg/Image.html)
    -   **`sensor_msgs/msg/PointCloud2`**: For 3D point cloud data from LIDAR or depth cameras.
        -   URL: [https://docs.ros.org/en/humble/p/sensor_msgs/msg/PointCloud2.html](https://docs.ros.org/en/humble/p/sensor_msgs/msg/PointCloud2.html)
    -   **`sensor_msgs/msg/Imu`**: For Inertial Measurement Unit data (orientation, angular velocity, linear acceleration).
        -   URL: [https://docs.ros.org/en/humble/p/sensor_msgs/msg/Imu.html](https://docs.ros.org/en/humble/p/sensor_msgs/msg/Imu.html)

3.  **RViz2 Display Types**: The RViz2 documentation and user guide describe the various display plugins used to visualize this data.
    -   **LaserScan Display**: For `sensor_msgs/msg/LaserScan`.
    -   **Image Display**: For `sensor_msgs/msg/Image`.
    -   **PointCloud2 Display**: For `sensor_msgs/msg/PointCloud2`.
    -   (General RViz2 User Guide): [https://docs.ros.org/en/humble/Tutorials/Intermediate/Rviz.html](https://docs.ros.org/en/humble/Tutorials/Intermediate/Rviz.html)

## Secondary Sources (Tutorials)

1.  **Simulating a Lidar**: A Gazebo tutorial that demonstrates how to generate simulated `LaserScan` messages.
    -   URL: [https://classic.gazebosim.org/tutorials?tut=ros2_lidar](https://classic.gazebosim.org/tutorials?tut=ros2_lidar)

2.  **Image Transport**: A guide to efficiently transporting images in ROS 2, which is important for camera data.
    -   URL: [https://docs.ros.org/en/humble/Tutorials/Advanced/Working-with-QC-images/Working-with-QC-images.html](https://docs.ros.org/en/humble/Tutorials/Advanced/Working-with-QC-images/Working-with-QC-images.html)
