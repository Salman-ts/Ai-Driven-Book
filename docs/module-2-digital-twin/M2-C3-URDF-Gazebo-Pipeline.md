## Chapter 3: The URDF → Gazebo Pipeline — Closing the Loop

Your robot has a body and a world, but it can't move. To control a robot in simulation, we need a way to send commands to its joints. This is handled by the `ros2_control` framework and a special Gazebo plugin.

This chapter will teach you how to set up this pipeline, allowing you to send velocity commands from a ROS 2 node and see your robot move in Gazebo, creating a closed-loop control system.

### Core Concepts: `ros2_control` in Simulation

The `ros2_control` framework is designed to separate generic controllers (e.g., a "differential drive controller") from the specific hardware interface that reads sensor data and sends motor commands. In simulation, the `gazebo_ros2_control` plugin pretends to be the robot's hardware.

Here's the architecture:
1.  **Hardware Interface (Gazebo Plugin)**: The `gazebo_ros2_control` plugin pretends to be the robot's hardware.

:::note
The `gazebo_ros2_control` plugin is essential for bridging the gap between the Gazebo physics engine and the `ros2_control` framework. It enables you to control simulated joints using the same ROS 2 interfaces you would use for a real robot.
:::

2.  **Controller Manager**: A ROS 2 node that loads, starts, and stops controllers.
3.  **Controllers**: Algorithms that perform control. For this chapter, we'll use:
    -   `joint_state_broadcaster`: Reads all the joint states from the hardware interface (the Gazebo plugin) and publishes them on the `/joint_states` topic for `robot_state_publisher` to use.
    -   `diff_drive_controller`: Subscribes to a `/cmd_vel` topic for velocity commands (`Twist` messages) and converts them into wheel velocity commands for the hardware interface.

### System Diagram

```ascii
+------------------------+
| teleop_twist_keyboard  |
+------------------------+
           |
           | Publishes Twist messages
           |
     [ /cmd_vel ] (Topic)
           |
           v
+------------------------+      +------------------------+
| diff_drive_controller  |----->| gazebo_ros2_control    |
+------------------------+      | (Plugin)               |
           ^                      +------------------------+
           |                             |         ^
           | Reads joint states          | Reads   | Writes
           |                             v         |
+------------------------+      +------------------------+
| joint_state_broadcaster|----->|     Simulated Joints   |
+------------------------+      +------------------------+
```

### System Diagram

```ascii
+------------------------+
| teleop_twist_keyboard  |
+------------------------+
           |
           | Publishes Twist messages
           |
     [ /cmd_vel ] (Topic)
           |
           v
+------------------------+      +------------------------+
| diff_drive_controller  |----->| gazebo_ros2_control    |
+------------------------+      | (Plugin)               |
           ^                      +------------------------+
           |                             |         ^
           | Reads joint states          | Reads   | Writes
           |                             v         |
+------------------------+      +------------------------+
| joint_state_broadcaster|----->|     Simulated Joints   |
+------------------------+      +------------------------+
```

---

## Lab: Driving Your Robot in Gazebo

In this lab, you'll create a simple differential drive robot, configure it for `ros2_control`, and drive it around in Gazebo using your keyboard.

### 1. Create a Drivable Robot URDF

First, create a new URDF file (`diff_drive.urdf`) for a simple two-wheeled robot. It should have a `base_link`, two wheel links (`left_wheel_link`, `right_wheel_link`), and the corresponding `continuous` joints.

### 2. Add `ros2_control` Tags to URDF

To make this URDF work with `ros2_control`, you need to add a special `<ros2_control>` tag at the end of the file. This tells the framework which joints are available for control.

```xml
<ros2_control name="GazeboSystem" type="system">
  <hardware>
    <plugin>gazebo_ros2_control/GazeboSystem</plugin>
  </hardware>
  <joint name="left_wheel_joint">
    <command_interface name="velocity">
      <param name="min">-10</param>
      <param name="max">10</param>
    </command_interface>
    <state_interface name="velocity"/>
    <state_interface name="position"/>
  </joint>
  <joint name="right_wheel_joint">
    <command_interface name="velocity">
      <param name="min">-10</param>
      <param name="max">10</param>
    </command_interface>
    <state_interface name="velocity"/>
    <state_interface name="position"/>
  </joint>
</ros2_control>
```
You also need to add the Gazebo plugin itself to the URDF:
```xml
<gazebo>
  <plugin name="gazebo_ros2_control" filename="libgazebo_ros2_control.so">
    <parameters>$(find my_robot_bringup)/config/controllers.yaml</parameters>
  </plugin>
</gazebo>
```

### 3. Create Controller Configuration

In your `my_robot_bringup` package, create a `config` directory. Inside, create `controllers.yaml`:
```yaml
controller_manager:
  ros__parameters:
    update_rate: 100

    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster

    diff_drive_controller:
      type: diff_drive_controller/DiffDriveController

diff_drive_controller:
  ros__parameters:
    left_wheel_names: ["left_wheel_joint"]
    right_wheel_names: ["right_wheel_joint"]
    wheel_separation: 0.4
    wheel_radius: 0.1
    publish_rate: 50.0
```

### 4. Update the Launch File

Your `gazebo.launch.py` now needs to load the controllers. The `gazebo_ros2_control` plugin will start the `controller_manager` automatically. We just need to use a `spawner` node to load our specific controllers.

```python
# In gazebo.launch.py

# ... imports ...
from launch_ros.actions import Node

def generate_launch_description():
    # ... Gazebo, robot_state_publisher, spawn_entity nodes ...

    # Spawner nodes
    joint_state_broadcaster_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster", "--controller-manager", "/controller_manager"],
    )

    diff_drive_spawner = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_drive_controller", "--controller-manager", "/controller_manager"],
    )

    return LaunchDescription([
        # ... other nodes ...
        joint_state_broadcaster_spawner,
        diff_drive_spawner
    ])
```

### 5. Build, Launch, and Drive

- Update `setup.py` to install the new `config` directory.
- Build and source your workspace (`colcon build`, `source install/setup.bash`).
- Launch the simulation: `ros2 launch my_robot_bringup gazebo.launch.py`.
- In a new terminal, run the keyboard teleop node: `ros2 run teleop_twist_keyboard teleop_twist_keyboard`.

### Verification

- [X] The robot should spawn in Gazebo.
- [X] Using the arrow keys in the teleop terminal should make the robot drive around in the simulation.
- [X] You can echo the `/joint_states` topic to see the wheel positions changing.

You have now created a complete, closed-loop control system for a simulated robot, a fundamental skill for any roboticist.