# Lab Outline: M2-C2 - Gazebo Physics Overview

This document outlines the lab requirements for Module 2, Chapter 2, as required by Task 1.7.3.

## Lab Goal

The user will learn how to add physical properties (mass, inertia, collision, and friction) to their URDF model from Chapter 3 and spawn it in a basic Gazebo world.

## Lab Requirements

1.  **Update the URDF for Physics**:
    -   [ ] In the `my_robot.urdf` file, add an `<inertial>` tag to each `<link>`.
        -   For simple shapes, calculate and add plausible mass and inertia tensor values.
    -   [ ] Add a `<collision>` tag to each `<link>`.
        -   For this lab, the collision geometry can be identical to the visual geometry.

2.  **Add Gazebo-Specific Tags**:
    -   [ ] In the URDF file, add `<gazebo>` tags for each link to define surface properties.
    -   [ ] Set the friction coefficients (`mu1`, `mu2`) for the base link to a high value to prevent it from sliding easily.
    -   [ ] Assign a different Gazebo material (color) to each link for better visualization (e.g., `Gazebo/Red`, `Gazebo/Green`).

3.  **Create a Gazebo World File**:
    -   [ ] In the `my_robot_bringup` package, create a `worlds` directory.
    -   [ ] Create a simple SDF world file (e.g., `empty.world`) that contains a ground plane and a light source.

4.  **Update the Launch File for Gazebo**:
    -   [ ] Create a new launch file, `gazebo.launch.py`, in the `my_robot_bringup` package.
    -   [ ] The launch file must:
        -   Start the Gazebo simulator with the `empty.world` file.
        -   Start the `robot_state_publisher` node (as in the previous chapter).
        -   Start a `spawn_entity.py` node. This is a standard ROS 2 node that calls the `/spawn_entity` service in Gazebo to add the robot model to the running simulation. The robot description (URDF content) must be passed to this node as a parameter.

5.  **Build and Launch**:
    -   [ ] Update `setup.py` to install the new `worlds` directory.
    -   [ ] Build the workspace with `colcon build`.
    -   [ ] Source the workspace.
    -   [ ] Launch the system using `ros2 launch my_robot_bringup gazebo.launch.py`.
    -   [ ] Verify that Gazebo opens, the robot is spawned on the ground plane, and it does not fall through the floor. The links should be colored as specified.

## Acceptance Criteria

-   The user can successfully add `<inertial>` and `<collision>` tags to their URDF.
-   The user can use the `<gazebo>` tag to set friction and material properties.
-   The user can create a launch file to start Gazebo and spawn a robot from a URDF.
-   The robot model appears correctly in the Gazebo simulation and interacts physically with the world (i.e., rests on the ground plane).
