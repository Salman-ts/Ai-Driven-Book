## Chapter 2: Gazebo Physics — Making it Real-ish

A digital twin is more than just a pretty 3D model; it's a physics simulation. To make our simulation behave realistically, we need to describe the physical properties of our robot.

This chapter will teach you how to add mass, inertia, and collision properties to your URDF model so that it can interact with the **Gazebo** simulator, a powerful and widely-used physics engine in the ROS ecosystem.

### Core Concepts: Describing Physicality

For a simulation to be meaningful, Gazebo's physics engine needs to know about your robot's physical attributes.

-   **`<inertial>`**: This tag defines the mass and inertia tensor of a link.
    -   **Mass**: Determines how the link reacts to forces.
    -   **Inertia Tensor**: A 3x3 matrix describing how the link's mass is distributed. This is critical for realistic rotational motion.

:::danger
An incorrect inertia tensor is a common source of bizarre and unrealistic simulation behavior. Tools like Blender or SolidWorks can help calculate this accurately for complex shapes.
:::
 An incorrect inertia tensor is a common source of bizarre simulation behavior.

-   **`<collision>`**: This tag defines the shape of the link for physics calculations. It's often a simpler version of the visual model to ensure fast and stable collision detection.

-   **`<surface>`**: This tag, nested within `<collision>`, defines how two objects interact when they touch.
    -   **Friction**: The force resisting sliding motion.
    -   **Restitution**: The "bounciness" of a collision.

Since URDF is a general format, we need a way to add Gazebo-specific information. We do this with a special `<gazebo>` tag. This tag is used to set surface properties (like friction), assign colors, and attach sensor or controller plugins.

### System Diagram

```ascii
+-----------------------------+
|        URDF File            |
| (+ <gazebo> extensions)     |
+-----------------------------+
              |
              | Parsed by...
              v
+-----------------------------+      +---------------------------+
|    Gazebo Simulator         |<---->|   ROS 2 Control Plugin    |
| (Spawns robot, runs physics)|      | (Reads joints, writes cmds) |
+-----------------------------+      +---------------------------+
              ^
              |
              | Receives velocity commands
              |
+-----------------------------+
|  /cmd_vel (Twist message)   |
+-----------------------------+
```

### System Diagram

```ascii
+-----------------------------+
|        URDF File            |
| (+ <gazebo> extensions)     |
+-----------------------------+
              |
              | Parsed by...
              v
+-----------------------------+      +---------------------------+
|    Gazebo Simulator         |<---->|   ROS 2 Control Plugin    |
| (Spawns robot, runs physics)|      | (Reads joints, writes cmds) |
+-----------------------------+      +---------------------------+
              ^
              |
              | Receives velocity commands
              |
+-----------------------------+
|  /cmd_vel (Twist message)   |
+-----------------------------+
```

---

## Lab: Spawning Your Robot in Gazebo

In this lab, you'll give your robot physical properties and spawn it in a Gazebo world.

### 1. Update the URDF for Physics

We need to add `<inertial>` and `<collision>` tags to the `my_robot.urdf` file from Module 1. For simple shapes, we can approximate the values.

```xml
<!-- Add this inside each <link> element in your URDF -->
<collision>
  <origin xyz="0 0 0" rpy="0 0 0"/>
  <geometry>
    <box size="0.5 0.05 0.05"/> <!-- Should match the visual geometry for this lab -->
  </geometry>
</collision>
<inertial>
  <mass value="1.0"/>
  <inertia ixx="0.002" ixy="0.0" ixz="0.0" iyy="0.002" iyz="0.0" izz="0.002"/>
</inertial>
```
*Note: You need to add appropriate `<collision>` and `<inertial>` tags to **all** links (`base_link`, `arm_link`, `hand_link`).*

### 2. Add Gazebo-Specific Tags

Now, let's add some Gazebo-specific properties. At the end of your URDF file, add these `<gazebo>` tags. This sets the color of the links within the Gazebo simulator.

```xml
<gazebo reference="arm_link">
  <material>Gazebo/Blue</material>
</gazebo>

<gazebo reference="hand_link">
  <material>Gazebo/Red</material>
</gazebo>
```

### 3. Create a Gazebo World

In your `my_robot_bringup` package, create a `worlds` directory. Inside, create `empty.world` with the following:

```xml
<?xml version="1.0" ?>
<sdf version="1.6">
  <world name="default">
    <include>
      <uri>model://ground_plane</uri>
    </include>
    <include>
      <uri>model://sun</uri>
    </include>
  </world>
</sdf>
```
This simple world just contains a ground plane and a light source.

### 4. Update the Launch File for Gazebo

Create a new launch file, `gazebo.launch.py`, in `my_robot_bringup/launch`. This file will start Gazebo and spawn our robot into the simulation.

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():
    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')
    pkg_my_robot_description = get_package_share_directory('my_robot_description')
    
    # Gazebo launch
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_gazebo_ros, 'launch', 'gazebo.launch.py'),
        )
    )

    # Robot State Publisher
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': open(os.path.join(pkg_my_robot_description, 'urdf', 'my_robot.urdf')).read()}]
    )

    # Spawn Entity
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-topic', 'robot_description', '-entity', 'my_robot'],
        output='screen'
    )

    return LaunchDescription([
        gazebo,
        robot_state_publisher,
        spawn_entity
    ])
```

### 5. Build and Launch

Update `setup.py` in `my_robot_bringup` to install the new `worlds` directory. Then build and source your workspace.

```bash
colcon build
source install/setup.bash
```

Finally, launch the Gazebo simulation:
```bash
ros2 launch my_robot_bringup gazebo.launch.py
```

### Verification

- [X] The Gazebo simulator should launch.
- [X] Your robot arm should appear, resting on the ground plane (not falling through it).
- [X] The arm and hand links should be colored blue and red, respectively, as defined in the `<gazebo>` tags.

You have successfully given your robot a physical presence in a simulated world!