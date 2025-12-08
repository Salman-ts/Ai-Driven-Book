# Authoritative Sources for `ros2_control` and Gazebo Plugins

This document lists primary sources for understanding the `ros2_control` framework and its integration with Gazebo, as required by Task 1.8.1.

## Primary Sources (Official Documentation)

1.  **`ros2_control` Documentation**: The official documentation for the ROS 2 control framework. It provides concepts, architecture, and tutorials.
    -   URL: [https://control.ros.org/master/index.html](https://control.ros.org/master/index.html)

2.  **`gazebo_ros2_control` Plugin**: The documentation for the specific Gazebo plugin that acts as the bridge between Gazebo and `ros2_control`.
    -   URL: [https://control.ros.org/master/doc/gazebo_ros2_control/doc/index.html](https://control.ros.org/master/doc/gazebo_ros2_control/doc/index.html)

3.  **`ros2_controllers` Package**: Documentation for the standard set of controllers available in ROS 2, such as `joint_state_broadcaster` and `diff_drive_controller`.
    -   URL: [https://control.ros.org/master/doc/ros2_controllers/doc/index.html](https://control.ros.org/master/doc/ros2_controllers/doc/index.html)

4.  **URDF for `ros2_control`**: Specific guide on how to format the `<ros2_control>` tag in a URDF for use with the framework.
    -   URL: [https://control.ros.org/master/doc/getting_started/getting_started/doc/userdoc.html#urdf-changes](https://control.ros.org/master/doc/getting_started/getting_started/doc/userdoc.html#urdf-changes)

## Secondary Sources (Tutorials)

1.  **Gazebo `ros2_control` Tutorial**: A step-by-step tutorial from the `ros-simulation` working group that shows how to set up `ros2_control` for a wheeled robot in Gazebo.
    -   URL: [https://gazebosim.org/docs/harmonic/ros2_integration_rolling](https://gazebosim.org/docs/harmonic/ros2_integration_rolling) (Note: Link points to general integration, but the `ros2_control` examples are the standard.)

2.  **Ignition Gazebo `ros2_control` Demo**: A repository showing a complete example of a cart with `ros2_control`. (Ignition is the new name for Gazebo).
    -   URL: [https://github.com/ros-simulation/gazebo_ros2_control_demos](https://github.com/ros-simulation/gazebo_ros2_control_demos)
