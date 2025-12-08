# Lab Outline: M1-C4 - Packages & Launch Architecture

This document outlines the lab requirements for Module 1, Chapter 4, as required by Task 1.4.3.

## Lab Goal

The user will refactor their existing ROS 2 application into a well-structured set of packages and create a top-level launch file to manage the system, demonstrating best practices for large projects.

## Lab Requirements

1.  **Refactor Packages**:
    -   [ ] Create a new package named `my_robot_bringup` (type `ament_python`).
    -   [ ] Move the `display.launch.py` file from `my_robot_description` to `my_robot_bringup/launch`.
    -   [ ] Modify the launch file to correctly locate the URDF and RViz files, which are now in a different package. Use `get_package_share_directory` for this.

2.  **Create a Top-Level Launch File**:
    -   [ ] Inside `my_robot_bringup`, create a new top-level launch file named `robot.launch.py`.
    -   [ ] This launch file should use `IncludeLaunchDescription` to include the `display.launch.py` file.
    -   [ ] It should also launch the publisher and subscriber nodes from the `my_first_package` created in Chapter 2.

3.  **Use Launch Arguments and Parameters**:
    -   [ ] Modify `display.launch.py` to accept a launch argument, `use_sim_time`, which defaults to `'true'`.
    -   [ ] Pass this argument to the `robot_state_publisher` node.
    -   [ ] From the top-level `robot.launch.py`, pass a value for `use_sim_time` to the included launch description.
    -   [ ] Create a `config/chatter_params.yaml` file in `my_first_package` to configure the `chatter` topic name.
    -   [ ] Modify the publisher/subscriber nodes to declare and use this parameter.
    -   [ ] Update the launch file to load and pass this parameter file to the nodes.

4.  **Create a Metapackage**:
    -   [ ] Create a new package named `my_robot` (type `ament_cmake`).
    -   [ ] Modify its `package.xml` to have `<exec_depend>` tags for `my_robot_description`, `my_robot_bringup`, and `my_first_package`.
    -   [ ] Modify its `CMakeLists.txt` to be a pure metapackage.

5.  **Build and Launch**:
    -   [ ] Build the entire workspace with `colcon build`.
    -   [ ] Source the workspace.
    -   [ ] Launch the entire system using the top-level launch file: `ros2 launch my_robot_bringup robot.launch.py`.
    -   [ ] Verify that RViz2, the robot model, the GUI, and the chatter pub/sub nodes all start correctly.

## Acceptance Criteria

-   The user can successfully refactor their code into multiple, single-purpose packages.
-   The user can create and use a top-level launch file to manage a multi-node system.
-   The user can pass arguments between launch files and load parameters from a YAML file.
-   The user can create a metapackage to group a set of related packages.
