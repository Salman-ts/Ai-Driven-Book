# Lab Outline: M3-C5 - Sim-to-Real Concepts

This document outlines the lab requirements for Module 3, Chapter 5, as required by Task 1.15.3.

## Lab Goal

The user will learn to deploy a navigation stack developed in Isaac Sim onto a physical robot. This lab will focus on verifying that SLAM and autonomous navigation work effectively on real hardware, and tuning parameters to bridge the sim-to-real gap.

## Lab Requirements

1.  **Physical Robot Setup**:
    -   [ ] Ensure the physical robot (e.g., Unitree Go2 or G1 with a differential drive setup) is powered on and its base drivers are running.
    -   [ ] Verify that the robot is publishing its odometry (`/odom`) and has a physical LIDAR sensor publishing `sensor_msgs/LaserScan` messages on the `/scan` topic, similar to the simulated setup.
    -   [ ] Ensure the `robot_state_publisher` is running on the physical robot, broadcasting the correct TF tree.

2.  **Deploy Nav2 to Physical Robot**:
    -   [ ] Transfer the Nav2 configuration package (`my_robot_nav2`) and the saved map (from M3-C4) to the physical robot (or a connected workstation).
    -   [ ] Modify the Nav2 launch file (`nav2_bringup.launch.py` or similar) to match the physical robot's sensor topics and coordinate frames.
    -   [ ] Launch the full Nav2 stack on the physical robot.

3.  **Perform SLAM (if new environment or for verification)**:
    -   [ ] If the physical environment is different from the one the map was created in, or for verification purposes, run `slam_toolbox` on the physical robot.
    -   [ ] Manually drive the robot around to build a map of the real-world environment.
    -   [ ] Save the generated map. Compare it with the simulated map to observe differences.

4.  **Autonomous Navigation on Physical Robot**:
    -   [ ] Load the appropriate map (either the simulated one if the environments are similar, or a newly generated real-world map).
    -   [ ] In RViz2 (running on a workstation connected to the robot's ROS network), set the `fixed_frame` to `map`.
    -   [ ] Provide an initial pose estimate using the "2D Pose Estimate" tool.
    -   [ ] Send navigation goals using the "2D Goal Pose" tool.
    -   [ ] Observe the physical robot navigating autonomously in the real environment.

5.  **Sim-to-Real Tuning and Parameter Adjustment**:
    -   [ ] Identify any discrepancies in behavior between simulation and reality (e.g., robot overshoots turns, bumps into obstacles).
    -   [ ] Adjust Nav2 parameters (e.g., local planner parameters like `max_vel_x`, `acc_lim_x`, `yaw_goal_tolerance`) to improve the robot's navigation performance in the real world.
    -   [ ] Discuss strategies for systematic parameter tuning and the role of system identification.

## Acceptance Criteria

-   The user can successfully bring up the necessary ROS 2 nodes on a physical robot.
-   The user can deploy and launch the Nav2 stack on real hardware.
-   The user can perform SLAM and/or autonomous navigation on a physical robot in a real-world environment.
-   The user can identify and adjust Nav2 parameters to improve the physical robot's navigation performance, demonstrating an understanding of practical sim-to-real challenges.
