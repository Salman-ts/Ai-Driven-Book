# Summary of ROS 2 Launch/Package Concepts

This document synthesizes key concepts for structuring complex ROS 2 applications using advanced launch files and packaging strategies, as required by Task 1.4.2.

## Advanced Launch File Features

Python launch files provide a powerful, programmatic way to define complex application startup.

-   **`LaunchDescription`**: The root object of a launch file. It acts as a container for all other launch elements (nodes, arguments, etc.).

-   **`Node` Action**: Represents a ROS 2 node to be executed. Key parameters include:
    -   `package`: The name of the package containing the node.
    -   `executable`: The name of the node's executable.
    -   `name`: A specific name to give the node instance.
    -   `parameters`: A list of dictionaries or a path to a YAML file to set the node's parameters.
    -   `remappings`: A list of tuples to remap topic, service, or action names.

-   **`IncludeLaunchDescription` Action**: Allows a launch file to include another launch file. This is the primary mechanism for creating modular and reusable launch configurations.

-   **`DeclareLaunchArgument` and `LaunchConfiguration`**: These are used to create parameterized launch files.
    -   `DeclareLaunchArgument` defines an argument that can be passed to the launch file from the command line (e.g., `ros2 launch my_pkg my_launch.py my_arg:=value`).
    -   `LaunchConfiguration('my_arg')` is a placeholder object that gets replaced with the actual value of the argument at launch time. This allows you to pass values from a top-level launch file down to included launch files or to node parameters.

-   **Event Handlers**: Allow you to react to events that occur during the launch process, such as a node starting or stopping. This enables complex startup sequences and fault tolerance.

## Packaging Best Practices

-   **One Package, One Purpose**: Each package should have a single, clear responsibility.
    -   `my_robot_description`: Contains the URDF, meshes, and RViz configs.
    -   `my_robot_bringup`: Contains the main launch files for starting the robot.
    -   `my_robot_control`: Contains the controller nodes.
    -   `my_robot_navigation`: Contains navigation-specific configurations.

-   **Metapackages**: A metapackage (or "variant" package) is an empty package that simply declares dependencies on a group of other packages. For example, a `my_robot` metapackage could depend on `my_robot_description`, `my_robot_bringup`, and `my_robot_control`. This allows a user to install the entire robot's software stack by cloning/installing a single package. This is configured in the `package.xml` using `<exec_depend>` tags and a specific build type.

-   **Directory Structure**: A well-organized package follows a standard directory structure:
    -   `launch/`: For Python launch files.
    -   `urdf/` or `description/`: For URDF/Xacro files.
    -   `rviz/`: For RViz configuration files.
    -   `config/` or `params/`: For node parameter YAML files.
    -   `worlds/`: For simulation world files.
    -   `src/`: For C++ source code.
    -   `(package_name)/`: For Python source code.
