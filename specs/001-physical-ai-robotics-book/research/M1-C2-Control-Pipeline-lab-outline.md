# Lab Outline: M1-C2 - Robot Control Pipeline

This document outlines the lab requirements for Module 1, Chapter 2, as required by Task 1.2.3.

## Lab Goal

The user will learn how to create a ROS 2 package and write simple publisher and subscriber nodes in Python using `rclpy`.

## Lab Requirements

1.  **Create a ROS 2 Package**:
    -   [ ] Use `ros2 pkg create` to create a new package named `my_first_package`.
    -   [ ] Specify the build type as `ament_python`.
    -   [ ] Add dependencies on `rclpy` and `std_msgs`.

2.  **Write a Publisher Node**:
    -   [ ] Create a Python file in the package for the publisher node (e.g., `publisher_node.py`).
    -   [ ] Implement a node that publishes a `std_msgs/String` message to a topic named `chatter` every second.
    -   [ ] The message should contain a counter (e.g., "Hello World: 1", "Hello World: 2", ...).

3.  **Write a Subscriber Node**:
    -   [ ] Create a Python file for the subscriber node (e.g., `subscriber_node.py`).
    -   [ ] Implement a node that subscribes to the `chatter` topic.
    -   [ ] The subscriber's callback function should log the received message to the console.

4.  **Configure `setup.py`**:
    -   [ ] Add the publisher and subscriber nodes to the `entry_points` in the `setup.py` file so they become runnable executables.

5.  **Build and Run**:
    -   [ ] Build the package using `colcon build`.
    -   [ ] Source the `install/setup.bash` file.
    -   [ ] Run the publisher node using `ros2 run my_first_package publisher_node`.
    -   [ ] Run the subscriber node using `ros2 run my_first_package subscriber_node`.
    -   [ ] Verify that the subscriber node prints the messages from the publisher.

## Acceptance Criteria

-   The user can successfully create a new ROS 2 Python package.
-   The user can write and build a functional publisher and subscriber node.
-   The user can run the nodes and observe the communication between them.
