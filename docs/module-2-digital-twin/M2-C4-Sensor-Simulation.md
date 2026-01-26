## Chapter 4: Sensor Simulation in Gazebo

A robot that can't sense its environment is blind. To build autonomous robots, we need to simulate sensors that provide data about the world. Gazebo has a rich ecosystem of plugins that can simulate a wide variety of sensors, from cameras to LIDARs to IMUs.

This chapter will teach you how to add a simulated 2D LIDAR and a camera to your robot's URDF, enabling it to "see" its environment in the Gazebo simulation.

### Core Concepts: Gazebo Sensor Plugins

Gazebo simulates sensors by attaching a `<sensor>` description to a link in a URDF or SDF model. This description defines the sensor's properties (e.g., camera resolution, LIDAR range) and a **plugin** that handles the data generation and publishing to ROS 2.

:::tip
Always refer to the official Gazebo plugin documentation for the most up-to-date configuration options and parameters for each sensor type.
:::


The process involves two main parts:
1.  **Defining the Sensor**: Using a `<sensor>` tag within a `<gazebo>` block to describe the sensor's hardware parameters.
2.  **Attaching a ROS Plugin**: Using a `<plugin>` tag to load a shared library (e.g., `libgazebo_ros_camera.so`) that reads the simulated sensor data and publishes it on a ROS 2 topic.

This is typically done by creating a new link for the sensor (e.g., `laser_link`) and attaching it to the robot's `base_link` with a `fixed` joint.

### System Diagram

```ascii
+-----------------------------+
|    Gazebo Simulator         |
| +-------------------------+ |
| |   Sensor Plugins        | |
| | (LIDAR, Camera)         | |
| +-------------------------+ |
+-----------------------------+
    |           |
    | Publishes | Publishes
    | LaserScan | Image
    v           v
[ /scan ]   [ /image_raw ] (Topics)
    |           |
    |           |
    +-----> +----------------+
            |     RViz2      |
            +----------------+
```

---

## Lab: Adding a LIDAR and Camera

In this lab, you'll add a simulated LIDAR and camera to your differential drive robot from the previous chapter and visualize their data in RViz2.

### 1. Update the URDF with Sensors

We'll add two new links and joints to our `diff_drive.urdf`, along with the corresponding `<gazebo>` tags to define the sensors and their plugins.

**A. Add the LIDAR:**
```xml
<!-- LIDAR Link and Joint -->
<link name="laser_link"></link>
<joint name="laser_joint" type="fixed">
  <parent link="base_link"/>
  <child link="laser_link"/>
  <origin xyz="0.1 0 0.2" rpy="0 0 0"/>
</joint>

<!-- Gazebo LIDAR Sensor -->
<gazebo reference="laser_link">
  <sensor type="ray" name="lidar_sensor">
    <update_rate>10</update_rate>
    <ray>
      <scan>
        <horizontal>
          <samples>360</samples>
          <resolution>1</resolution>
          <min_angle>-3.14</min_angle>
          <max_angle>3.14</max_angle>
        </horizontal>
      </scan>
      <range>
        <min>0.1</min>
        <max>12.0</max>
      </range>
    </ray>
    <plugin name="gazebo_ros_lidar" filename="libgazebo_ros_ray_sensor.so">
      <ros>
        <output_type>sensor_msgs/LaserScan</output_type>
        <topic_name>scan</topic_name>
      </ros>
    </plugin>
  </sensor>
</gazebo>
```

**B. Add the Camera:**
```xml
<!-- Camera Link and Joint -->
<link name="camera_link"></link>
<joint name="camera_joint" type="fixed">
  <parent link="base_link"/>
  <child link="camera_link"/>
  <origin xyz="0.2 0 0.1" rpy="0 0 0"/>
</joint>

<!-- Gazebo Camera Sensor -->
<gazebo reference="camera_link">
  <sensor type="camera" name="camera_sensor">
    <update_rate>30.0</update_rate>
    <camera name="head">
      <horizontal_fov>1.3962634</horizontal_fov>
      <image>
        <width>800</width>
        <height>800</height>
        <format>R8G8B8</format>
      </image>
      <clip>
        <near>0.02</near>
        <far>300</far>
      </clip>
    </camera>
    <plugin name="camera_controller" filename="libgazebo_ros_camera.so">
      <ros>
        <camera_name>my_camera</camera_name>
        <image_topic_name>image_raw</image_topic_name>
        <camera_info_topic_name>camera_info</camera_info_topic_name>
      </ros>
    </plugin>
  </sensor>
</gazebo>
```

### 2. Update RViz2 and Launch Files

Your `gazebo.launch.py` file doesn't need any changes, as Gazebo automatically loads the plugins from the URDF.

However, you should update your `display.rviz` configuration:
-   Launch RViz2 (`ros2 run rviz2 rviz2`).
-   Add a `LaserScan` display and set its topic to `/scan`.
-   Add an `Image` display and set its topic to `/my_camera/image_raw`.
-   Save the configuration over your old `display.rviz` file.
-   Add a node to your main launch file to start RViz2 with this config.

### 3. Build and Launch

Build and source your workspace, then launch the simulation:
```bash
colcon build
source install/setup.bash
ros2 launch my_robot_bringup gazebo.launch.py
```

### Verification

- [X] In Gazebo, place an object (like a cube) in front of your robot.
- [X] In RViz2, you should see the `LaserScan` display showing the object as a series of red dots.
- [X] The `Image` display in RViz2 should show the view from your robot's camera, including the object.
- [X] You can use `ros2 topic echo /scan` and `ros2 topic echo /my_camera/image_raw` to inspect the raw data being published.

Your robot can now see the world! This is the foundation for all perception-based tasks, from simple obstacle avoidance to complex object recognition.