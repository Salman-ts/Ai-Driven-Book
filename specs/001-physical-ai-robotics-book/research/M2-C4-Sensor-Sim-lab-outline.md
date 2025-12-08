# Lab Outline: M2-C4 - Sensor Simulation

This document outlines the lab requirements for Module 2, Chapter 4, as required by Task 1.9.3.

## Lab Goal

The user will learn how to add a simulated 2D LIDAR and a camera to their robot's URDF, visualize the sensor data in RViz2, and see the sensor's output in Gazebo.

## Lab Requirements

1.  **Update the URDF with Sensors**:
    -   [ ] In the differential drive robot URDF from the previous chapter, add a new link for a LIDAR sensor (e.g., `laser_link`).
    -   [ ] Add a `fixed` joint to mount the `laser_link` to the `base_link`.
    -   [ ] Add a `<gazebo reference="laser_link">` tag to define the LIDAR sensor and the `gazebo_ros_ray_sensor` plugin. Configure it to publish a `sensor_msgs/LaserScan` on the `/scan` topic.
    -   [ ] Add another new link for a camera (e.g., `camera_link`).
    -   [ ] Add a `fixed` joint to mount the `camera_link` to the `base_link`.
    -   [ ] Add a `<gazebo reference="camera_link">` tag to define the camera sensor and the `gazebo_ros_camera` plugin. Configure it to publish a `sensor_msgs/Image` on the `/image_raw` topic.

2.  **Update RViz2 Configuration**:
    -   [ ] Open the `display.rviz` configuration file.
    -   [ ] Add a `LaserScan` display and configure it to listen to the `/scan` topic.
    -   [ ] Add an `Image` display and configure it to listen to the `/image_raw` topic.

3.  **Update Launch File**:
    -   [ ] No major changes are needed to `gazebo.launch.py`, as Gazebo will automatically load and run the sensor plugins defined in the URDF.
    -   [ ] However, it's good practice to also launch RViz2 with the updated configuration. Add a node to the launch file to start `rviz2` with the `display.rviz` config file.

4.  **Build and Launch**:
    -   [ ] Build the workspace with `colcon build`.
    -   [ ] Launch the system using `ros2 launch my_robot_bringup gazebo.launch.py`.

5.  **Verify Sensor Output**:
    -   [ ] In Gazebo, check the "View" menu and enable "Collisions" and "Contacts" to see the invisible laser rays.
    -   [ ] Place a simple object (e.g., a box) in front of the robot in the Gazebo world.
    -   [ ] In RViz2, verify that the `LaserScan` display shows the object.
    -   [ ] In RViz2, verify that the `Image` display shows the view from the robot's camera, including the object.
    -   [ ] Use `ros2 topic echo /scan` and `ros2 topic echo /image_raw` to inspect the raw data being published.

## Acceptance Criteria

-   The user can successfully add LIDAR and camera sensor plugins to a URDF.
-   The plugins load correctly when the model is spawned in Gazebo.
-   The sensor plugins publish data to the correct ROS 2 topics.
-   The sensor data can be visualized correctly in RViz2.
