## Chapter 5: The Sensor Ecosystem — Giving Your Robot Senses

A robot is only as good as its senses. To operate in the real world, a robot needs sensors to perceive its environment. In ROS 2, sensor data is shared using a set of standard message types, primarily from the `sensor_msgs` package.

This chapter will introduce you to the most common sensor messages and show you how to integrate a simulated 2D LIDAR into your robot, visualize its data, and use that data in a node.

### Core Concepts: Standard Sensor Messages

Using standard message types is crucial for interoperability. It allows you to use a LIDAR from one manufacturer, a mapping algorithm from another, and a visualization tool from a third, and have them all work together seamlessly.

-   **`sensor_msgs/msg/LaserScan`**: The message for 2D LIDARs. It's essentially an array of distances, telling you how far away obstacles are in a 2D plane around the robot.
-   **`sensor_msgs/msg/PointCloud2`**: The message for 3D sensors like depth cameras and 3D LIDARs. It's a highly flexible message that represents a cloud of points in 3D space.
-   **`sensor_msgs/msg/Image`**: The standard message for camera images.
-   **`sensor_msgs/msg/Imu`**: For Inertial Measurement Units, providing acceleration and angular velocity.

A key part of every sensor message is the `header`, which contains a `timestamp` and a `frame_id`. The `frame_id` is critical, as it tells the system which coordinate frame the sensor data is relative to (e.g., `base_link`, `laser_frame`).

### System Diagram

```ascii
+--------------------------+
|  /simulated_lidar_node   |
+--------------------------+
           |
           | Publishes LaserScan messages
           |
     [ /scan ] (Topic)
           |
           +-----> +-----------------------+
           |       | /sensor_subscriber_node |
           |       +-----------------------+
           |
           +-----> +-----------------------+
                   |         RViz2         |
                   +-----------------------+
```

### System Diagram

```ascii
+--------------------------+
|  /simulated_lidar_node   |
+--------------------------+
           |
           | Publishes LaserScan messages
           |
     [ /scan ] (Topic)
           |
           +-----> +-----------------------+
           |       | /sensor_subscriber_node |
           |       +-----------------------+
           |
           +-----> +-----------------------+
                   |         RViz2         |
                   +-----------------------+
```

---

## Lab: Adding a LIDAR to Your Robot

In this lab, you'll add a simulated LIDAR to your robot, create a node to process its data, and visualize the output in RViz2.

### 1. Simulate a Sensor

For this lab, we'll create a simple Python node that fakes `LaserScan` data. In a real project, this would be your sensor's driver.

In your `my_first_package`, create `lidar_simulator_node.py`:
```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
import math

class LidarSimulator(Node):
    def __init__(self):
        super().__init__('lidar_simulator')
        self.publisher_ = self.create_publisher(LaserScan, 'scan', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = LaserScan()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.header.frame_id = 'laser_frame'
        msg.angle_min = -math.pi
        msg.angle_max = math.pi
        msg.angle_increment = math.pi / 180.0
        msg.range_min = 0.1
        msg.range_max = 10.0
        # Simulate a wall in front of the robot
        num_readings = int((msg.angle_max - msg.angle_min) / msg.angle_increment)
        msg.ranges = [1.0] * num_readings
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    lidar_simulator = LidarSimulator()
    rclpy.spin(lidar_simulator)
    lidar_simulator.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```
Don't forget to add this new node to the `entry_points` in your `setup.py`!

### 2. Provide a Static Transform

Our new LIDAR publishes data relative to a `laser_frame`, but ROS doesn't know where `laser_frame` is. We need to publish a **static transform** to define its position relative to our robot's `base_link`.

:::note
A static transform is a transform that does not change over time. It is crucial for defining the fixed relationship between different parts of your robot or between sensors and the robot's base.
:::


Update your `robot.launch.py` in `my_robot_bringup` to include a `static_transform_publisher`:
```python
# In robot.launch.py
# ... other imports
from launch_ros.actions import Node

def generate_launch_description():
    # ... other launch description code ...
    return LaunchDescription([
        # ... other nodes ...
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='static_transform_publisher_laser',
            arguments=['0.1', '0', '0.2', '0', '0', '0', 'base_link', 'laser_frame']
        ),
        Node(
            package='my_first_package',
            executable='lidar_simulator_node',
            name='lidar_simulator'
        ),
    ])
```
This command tells `tf2_ros` to publish a constant transform from `base_link` to `laser_frame` with a small offset.

### 3. Visualize in RViz2

-   Launch RViz2 (`ros2 run rviz2 rviz2`) and open your saved `display.rviz` configuration.
-   Click "Add" and choose the `LaserScan` display.
-   Set its "Topic" to `/scan`.
-   Save the configuration.

Now when you run your main launch file, RViz2 will automatically be configured to show the LIDAR data.

### 4. Build and Launch

Build your workspace and launch the main launch file:
```bash
colcon build
source install/setup.bash
ros2 launch my_robot_bringup robot.launch.py
```
### Verification

- [X] In RViz2, you should now see a red line or dots appear around your robot, representing the simulated LIDAR scan.
- [X] The scan should be positioned correctly relative to the robot model, thanks to the static transform.

You have now given your robot the sense of sight! This is a fundamental step toward enabling a robot to navigate its environment.