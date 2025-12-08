# Lab Outline: M2-C5 - Unity Visualization

This document outlines the lab requirements for Module 2, Chapter 5, as required by Task 1.10.3.

## Lab Goal

The user will learn how to use the Unity engine as a high-fidelity visualizer for an existing ROS 2/Gazebo simulation. They will import their robot model, connect Unity to their ROS network, and mirror the robot's state and sensor data in the Unity scene.

## Lab Requirements

1.  **Set Up Unity Project**:
    -   [ ] Install Unity Hub and the recommended Unity Editor version.
    -   [ ] Create a new 3D project.
    -   [ ] Using the Unity Package Manager, install the required robotics packages from the Unity Robotics Hub (e.g., `ROS-TCP-Connector`, `URDF-Importer`).

2.  **Import the Robot**:
    -   [ ] From the Unity menu, use the `URDF-Importer` to import the differential drive robot's URDF file.
    -   [ ] Verify that the importer creates a "prefab" of the robot with the correct hierarchy of links and `ArticulationBody` joints.

3.  **Create the Unity Scene**:
    -   [ ] Create a new scene in Unity.
    -   [ ] Add a simple ground plane and lighting.
    -   [ ] Add the "ROS Connection" prefab to the scene and configure it to connect to the IP address where ROS is running.
    -   [ ] Drag the imported robot prefab into the scene.

4.  **Configure ROS-Side Endpoint**:
    -   [ ] Install the `ros_tcp_endpoint` package for ROS 2.
    -   [ ] Modify the main `gazebo.launch.py` launch file to also start the `default_server_endpoint` node from this package. This node will bridge the topics to Unity.

5.  **Visualize Robot and Sensor Data**:
    -   [ ] In Unity, add a C# script to the robot model that subscribes to `/joint_states` and updates the `ArticulationBody` joint positions accordingly. (The URDF importer may create a default script for this).
    -   [ ] Add a `LaserScan` visualizer component to the scene and configure it to subscribe to the `/scan` topic.

6.  **Run the Full System**:
    -   [ ] Launch the ROS 2 system: `ros2 launch my_robot_bringup gazebo.launch.py`. This should now start Gazebo, the robot, the controllers, the sensor plugins, and the TCP endpoint.
    -   [ ] In a separate terminal, run `teleop_twist_keyboard` to drive the robot.
    -   [ ] Press the "Play" button in the Unity Editor.
    -   [ ] Verify that:
        -   The robot in Unity moves in sync with the robot in Gazebo.
        -   The LIDAR scan from the Gazebo simulation is visualized in the Unity scene.

## Acceptance Criteria

-   The user can successfully set up a Unity project with the required robotics packages.
-   The user can import a URDF and create a controllable robot in the Unity scene.
-   The user can establish a connection between Unity and a running ROS 2 system.
-   The state of the robot and its sensors in a Gazebo simulation are accurately mirrored in the Unity visualization.
