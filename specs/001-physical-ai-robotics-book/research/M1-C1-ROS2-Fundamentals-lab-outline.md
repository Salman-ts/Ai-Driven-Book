# Lab Outline: M1-C1 - ROS 2 Fundamentals

This document outlines the lab requirements for Module 1, Chapter 1, as required by Task 1.1.3.

## Lab Goal

The user will gain hands-on experience with the core command-line tools of ROS 2 by installing it, running a simple simulation, and inspecting the ROS graph.

## Lab Requirements

1.  **Environment Setup**:
    -   [ ] Install ROS 2 Humble Hawksbill on a supported platform (Ubuntu 22.04).
    -   [ ] Source the ROS 2 setup files.
    -   [ ] Verify the installation using the `ros2` command.

2.  **Running a Simulation**:
    -   [ ] Run the `turtlesim_node` to start the TurtleSim simulation window.
    -   [ ] Run the `turtle_teleop_key` node to enable keyboard control of the turtle.
    -   [ ] Use the keyboard to move the turtle around in the simulation window.

3.  **Inspecting the ROS Graph**:
    -   [ ] Use `ros2 node list` to see the running `/turtlesim` and `/teleop_turtle` nodes.
    -   [ ] Use `ros2 topic list` to see available topics, including `/turtle1/cmd_vel`.
    -   [ ] Use `ros2 topic echo /turtle1/cmd_vel` to inspect the velocity commands being published by the teleop node.
    -   [ ] Use `ros2 service list` to see the services offered by the `/turtlesim` node (e.g., `/spawn`, `/kill`).
    -   [ ] Use `ros2 service call /spawn turtlesim/srv/Spawn "{'x': 2, 'y': 2, 'theta': 0.2, 'name': 'my_turtle'}"` to spawn a new turtle.

## Acceptance Criteria

-   The user can successfully install ROS 2.
-   The user can run and control the TurtleSim simulation.
-   The user can use `ros2` command-line tools to inspect the running system and call a service.
