# Lab Outline: M2-C3 - URDF → Gazebo Pipeline

This document outlines the lab requirements for Module 2, Chapter 3, as required by Task 1.8.3.

## Lab Goal

The user will learn how to control a simulated robot in Gazebo using the `ros2_control` framework. They will configure a differential drive robot, launch the necessary controllers, and drive it using keyboard commands.

## Lab Requirements

1.  **Create a Drivable Robot URDF**:
    -   [ ] Create a new robot model or modify the existing one to represent a simple two-wheeled differential drive robot (e.g., a body with two wheels).
    -   [ ] Ensure the wheels use `continuous` joints.

2.  **Add `ros2_control` Tags to URDF**:
    -   [ ] Add a `<ros2_control>` tag to the URDF.
    -   [ ] Inside this tag, define the `system` interface for Gazebo.
    -   [ ] Define the `joint` interfaces for the two wheel joints, exposing `velocity` commands and `position`/`velocity` states.
    -   [ ] Add the `<plugin>` tag to load the `gazebo_ros2_control` system.

3.  **Create Controller Configuration**:
    -   [ ] In the `my_robot_bringup` package, create a `config` directory.
    -   [ ] Create a YAML file (e.g., `controllers.yaml`) inside this directory.
    -   [ ] The YAML file must define the `controller_manager` node and configure two controllers:
        -   `joint_state_broadcaster`: To publish the state of all joints.
        -   `diff_drive_controller`: To control the two wheel joints. Specify the names of the left and right wheel joints and the command topic (`/cmd_vel`).

4.  **Update the Launch File**:
    -   [ ] Modify the `gazebo.launch.py` file to set up the full control pipeline.
    -   [ ] It must now launch:
        -   Gazebo.
        -   The `robot_state_publisher`.
        -   The `spawn_entity` node to add the robot to Gazebo.
        -   A `node` for the `controller_manager` (though this is often handled automatically by the Gazebo plugin).
        -   A `spawner` node to load and start the `joint_state_broadcaster`.
        -   A `spawner` node to load and start the `diff_drive_controller`.

5.  **Build and Launch**:
    -   [ ] Update `setup.py` to install the new `config` directory.
    -   [ ] Build the workspace with `colcon build`.
    -   [ ] Launch the system with `ros2 launch my_robot_bringup gazebo.launch.py`.

6.  **Drive the Robot**:
    -   [ ] In a new terminal, run the `teleop_twist_keyboard` node: `ros2 run teleop_twist_keyboard teleop_twist_keyboard`.
    -   [ ] Use the keyboard to send `Twist` commands on `/cmd_vel`.
    -   [ ] Verify that the robot moves correctly in the Gazebo simulation.

## Acceptance Criteria

-   The user can successfully add `ros2_control` tags to a URDF for a differential drive robot.
-   The user can create a YAML file to configure the necessary controllers.
-   The user can create a launch file that loads the Gazebo plugin and starts the controllers.
-   The simulated robot in Gazebo can be driven by publishing velocity commands to the `/cmd_vel` topic.
