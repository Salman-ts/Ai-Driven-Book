# Summary of Gazebo Sensor Simulation Concepts

This document synthesizes key concepts for adding simulated sensors to a robot model in Gazebo, as required by Task 1.9.2.

## How Sensor Simulation Works in Gazebo

Gazebo simulates sensors by attaching a "sensor" description to a link in a robot model (URDF or SDF). This description defines the sensor's properties (e.g., camera resolution, LIDAR range) and a **plugin** that handles the actual data generation and publishing to ROS 2.

The process involves two main parts:
1.  **Defining the Sensor**: Using an SDF `<sensor>` tag (or a `<gazebo>` tag in URDF) to describe the sensor's hardware parameters.
2.  **Attaching a ROS Plugin**: Using a `<plugin>` tag to load a shared library (e.g., `libgazebo_ros_camera.so`) that reads the simulated sensor data and publishes it on a ROS 2 topic.

## Adding Sensors via URDF

Since URDF is the common format, the standard method is to use the `<gazebo>` tag. A sensor is attached to a specific link, and a joint is used to position it correctly relative to that link.

The structure is typically:
1.  **A new `_sensor_link`**: A link representing the physical sensor hardware.
2.  **A `_sensor_joint`**: A `fixed` joint attaching the sensor link to the part of the robot where it is mounted.
3.  **A `<gazebo reference="sensor_link">` tag**: This is where the sensor and its plugin are defined.

### Example: Adding a LIDAR Sensor

```xml
<!-- Sensor Link and Joint -->
<link name="laser_link"></link>
<joint name="laser_joint" type="fixed">
  <parent link="base_link"/>
  <child link="laser_link"/>
  <origin xyz="0.1 0 0.2" rpy="0 0 0"/>
</joint>

<!-- Gazebo Sensor and Plugin Definition -->
<gazebo reference="laser_link">
  <sensor type="ray" name="lidar_sensor">
    <pose>0 0 0 0 0 0</pose>
    <visualize>true</visualize>
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
        <resolution>0.01</resolution>
      </range>
    </ray>
    <plugin name="gazebo_ros_lidar" filename="libgazebo_ros_ray_sensor.so">
      <ros>
        <namespace>/</namespace>
        <output_type>sensor_msgs/LaserScan</output_type>
        <topic>scan</topic>
      </ros>
    </plugin>
  </sensor>
</gazebo>
```

### Breakdown of the `<gazebo>` Tag Content:

-   **`<sensor type="ray" name="...">`**: Defines a sensor. The `type` attribute specifies the kind of sensor (e.g., `ray` for LIDAR, `camera` for a camera).
-   **`<update_rate>`**: How often the sensor generates new data (in Hz).
-   **`<ray>` or `<camera>` section**: This block defines the sensor's intrinsic parameters. For a LIDAR (`ray`), this includes the horizontal scan properties (number of samples, resolution, angles) and range limits. For a camera, it would include image `width`, `height`, and `format`.
-   **`<plugin name="..." filename="...">`**: This is the most important part for ROS integration.
    -   `filename`: The name of the shared library file for the plugin (e.g., `libgazebo_ros_ray_sensor.so` for a LIDAR).
    -   `name`: A unique name for this plugin instance.
    -   **`<ros>` block**: This block within the plugin contains ROS-specific parameters.
        -   `<topic>` or `<output_topic>`: The name of the ROS 2 topic where the sensor data will be published.
        -   `<output_type>`: The ROS 2 message type to use.
        -   `<frame_name>`: (Optional) Overrides the coordinate frame ID for the published messages. If not set, it defaults to the link the sensor is attached to (`laser_link` in this case).
