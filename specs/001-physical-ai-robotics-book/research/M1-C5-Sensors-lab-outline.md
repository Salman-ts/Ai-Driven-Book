# Lab Outline: M1-C5 - Sensor Ecosystem

This document outlines the lab requirements for Module 1, Chapter 5, as required by Task 1.5.3.

## Lab Goal

The user will learn how to integrate a simulated sensor into a ROS 2 system, subscribe to its data, and visualize it in RViz2. This lab will focus on using a simulated 2D LIDAR.

## Lab Requirements

1.  **Simulate a Sensor**:
    -   [ ] This lab will use a pre-existing ROS 2 package that simulates a LIDAR and publishes `sensor_msgs/msg/LaserScan` messages. The `laser_scan_publisher` from the [`ros2_examples`](https://github.com/ros-real-time/ros2-real-time-examples/tree/master/ros2_real_time_demo/laser_scan_publisher) repository can be used as a reference or provided directly.
    -   Alternatively, a simple node that manually constructs and publishes a `LaserScan` message can be created.

2.  **Update the Launch File**:
    -   [ ] Modify the top-level launch file (`robot.launch.py` from Chapter 4) to start the simulated LIDAR node.
    -   [ ] Ensure the LIDAR node publishes on a topic named `/scan`.

3.  **Create a Sensor Subscriber**:
    -   [ ] In the `my_first_package`, create a new Python node named `sensor_subscriber.py`.
    -   [ ] This node should subscribe to the `/scan` topic (`sensor_msgs/msg/LaserScan`).
    -   [ ] The callback function should process the `ranges` array. For this lab, it can simply find and print the minimum range value detected in the scan.
    -   [ ] Add the new node to the `setup.py` file.
    -   [ ] Add the new node to the top-level launch file.

4.  **Visualize in RViz2**:
    -   [ ] Update the RViz2 configuration file (`display.rviz`) to include a `LaserScan` display.
    -   [ ] Configure the display to subscribe to the `/scan` topic.
    -   [ ] Ensure the `Global Options` -> `Fixed Frame` in RViz2 is set to the `frame_id` specified in the simulated `LaserScan` messages (e.g., `laser_frame`).

5.  **Provide Static Transform**:
    -   [ ] The LIDAR sensor has its own coordinate frame (`laser_frame`). To relate this to the robot's base, a static transform is needed.
    -   [ ] Add a `static_transform_publisher` node to the launch file. This node will publish a fixed transform between `base_link` and `laser_frame`.

6.  **Build and Launch**:
    -   [ ] Build the workspace with `colcon build`.
    -   [ ] Launch the system with `ros2 launch my_robot_bringup robot.launch.py`.
    -   [ ] Verify that:
        -   The `sensor_subscriber` node prints the minimum range.
        -   The `LaserScan` data appears correctly in RViz2, positioned relative to the robot model.

## Acceptance Criteria

-   The user can launch a node that publishes `LaserScan` data.
-   The user can write a subscriber node to process the sensor data.
-   The user can configure RViz2 to display the `LaserScan` data.
-   The user can add a static transform to correctly position the sensor data in the 3D scene.
