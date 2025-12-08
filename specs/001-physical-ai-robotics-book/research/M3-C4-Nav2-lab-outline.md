# Lab Outline: M3-C4 - Navigation & Path Planning

This document outlines the lab requirements for Module 3, Chapter 4, as required by Task 1.14.3.

## Lab Goal

The user will configure and run the ROS 2 Navigation Stack (Nav2) in Isaac Sim. They will learn to build a map of a simulated environment using SLAM, localize the robot within that map, and send navigation goals to autonomously drive the robot.

## Lab Requirements

1.  **Prepare the Isaac Sim Environment**:
    -   [ ] Load the robot model (from previous Isaac Sim labs) into Isaac Sim.
    -   [ ] Create a more complex environment than a simple ground plane. Add walls, obstacles (boxes, cylinders), and perhaps some ramps or uneven terrain to simulate a realistic indoor setting.
    -   [ ] Ensure the robot has a LIDAR sensor configured to publish `sensor_msgs/LaserScan` messages on the `/scan` topic, and odometry on `/odom` topic.

2.  **Integrate Nav2 with Isaac Sim (ROS Bridge)**:
    -   [ ] Isaac Sim provides a built-in ROS 2 bridge. Ensure it is configured to publish the robot's odometry, LIDAR data, and TF transforms to ROS 2.
    -   [ ] On the ROS 2 side, prepare a Nav2 configuration package (e.g., `my_robot_nav2`).
    -   [ ] Create a launch file within this package that loads the standard Nav2 stack. This will involve launching nodes like `amcl` (for localization), the global and local planners, and the behavior tree navigator.
    -   [ ] The Nav2 parameters (YAML files) should be configured for the robot's dimensions and sensor characteristics.

3.  **Perform SLAM (Simultaneous Localization and Mapping)**:
    -   [ ] Create a separate launch file to run `slam_toolbox` in Isaac Sim. This will listen to `/scan` and `/odom` topics and build a map.
    -   [ ] Manually drive the robot around the simulated environment using `teleop_twist_keyboard` (or programmatically) to explore and build a complete map.
    -   [ ] Once a satisfactory map is built, save it to a file (e.g., `my_isaac_map.yaml` and `my_isaac_map.pgm`).

4.  **Autonomous Navigation**:
    -   [ ] Modify the Nav2 launch file to load the saved map.
    -   [ ] Ensure `amcl` (or an equivalent localization node) is running to localize the robot within the map.
    -   [ ] Launch the full Nav2 stack.
    -   [ ] In RViz2, set the `fixed_frame` to `map`.
    -   [ ] Use the "2D Pose Estimate" tool in RViz2 to provide an initial estimate of the robot's position on the map.
    -   [ ] Use the "2D Goal Pose" tool in RViz2 to send navigation goals to the robot.
    -   [ ] Observe the robot autonomously navigate to the specified goals, avoiding obstacles in the simulated environment.

## Acceptance Criteria

-   The user can successfully set up a simulated environment in Isaac Sim with a robot and obstacles.
-   The user can build a map of the simulated environment using `slam_toolbox`.
-   The user can launch the full Nav2 stack, load a map, and localize the robot.
-   The user can send navigation goals, and the robot autonomously reaches them in Isaac Sim while avoiding obstacles.
