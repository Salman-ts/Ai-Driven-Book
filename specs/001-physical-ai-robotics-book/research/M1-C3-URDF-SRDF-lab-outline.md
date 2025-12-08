# Lab Outline: M1-C3 - URDF/SRDF Robot Description

This document outlines the lab requirements for Module 1, Chapter 3, as required by Task 1.3.3.

## Lab Goal

The user will learn to write a basic URDF file for a simple robot arm and visualize it in RViz2, controlling the joint angles with a GUI.

## Lab Requirements

1.  **Create a Description Package**:
    -   [ ] Create a new ROS 2 package named `my_robot_description` of type `ament_python`.
    -   [ ] Create a `urdf` directory inside the package to hold the robot model files.

2.  **Write the URDF File**:
    -   [ ] Create a file named `my_robot.urdf` inside the `urdf` directory.
    -   [ ] Define a `base_link` as the foundation of the robot.
    -   [ ] Create a two-link arm connected by revolute joints:
        -   `base_link` -> `joint1` -> `link1`
        -   `link1` -> `joint2` -> `link2`
    -   [ ] Define simple geometric shapes (e.g., boxes or cylinders) for the `<visual>` tags of each link.
    -   [ ] Ensure all joints, links, and the root `<robot>` element are correctly defined.

3.  **Create a Launch File**:
    -   [ ] Create a `launch` directory in the package.
    -   [ ] Create a Python launch file (e.g., `display.launch.py`).
    -   [ ] The launch file must:
        -   Find and load the `my_robot.urdf` file.
        -   Start the `robot_state_publisher` node, passing the URDF content to it.
        -   Start the `joint_state_publisher_gui` node.
        -   Start `rviz2` and load a pre-configured RViz2 configuration file.

4.  **Create an RViz2 Configuration**:
    -   [ ] Create an `rviz` directory in the package.
    -   [ ] Launch RViz2 manually, add the "RobotModel" and "TF" displays.
    -   [ ] Save the configuration to a file named `display.rviz` inside the `rviz` directory.

5.  **Build and Launch**:
    -   [ ] Add logic to `setup.py` to install the `urdf`, `launch`, and `rviz` directories.
    -   [ ] Build the package with `colcon build`.
    -   [ ] Source the workspace (`install/setup.bash`).
    -   [ ] Launch the display using `ros2 launch my_robot_description display.launch.py`.
    -   [ ] Use the `joint_state_publisher_gui` sliders to move the robot arm in RViz2.

## Acceptance Criteria

-   The user can successfully create a package to hold a robot description.
-   The user can write a valid URDF for a simple robot arm.
-   The user can create a launch file to bring up the robot model in RViz2.
-   The robot model appears correctly in RViz2 and can be articulated using the GUI sliders.
