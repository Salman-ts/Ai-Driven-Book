## Chapter 3: URDF — Describing Your Robot's Body

Every robot needs a body. In ROS 2, we describe that body using the **Unified Robot Description Format (URDF)**. URDF is an XML-based format that allows us to create a digital model of our robot, defining its parts and how they connect.

This chapter will teach you how to build a simple robot arm in URDF and visualize it in RViz2, the standard ROS 2 visualization tool.

### Core Concepts: Links and Joints

A URDF model represents a robot as a tree of **links** connected by **joints**.

-   **Links**: A link is a rigid body part of the robot (e.g., a forearm, a wheel, a torso). Each link has its own coordinate frame and can have three key properties:
    -   **`<visual>`**: How the link looks. This can be a simple geometric shape (box, cylinder, sphere) or a 3D mesh file.
    -   **`<collision>`**: The link's physical shape for collision detection. This is often simpler than the visual model to speed up physics calculations.
    -   **`<inertial>`**: The link's dynamic properties, like its mass and inertia tensor, which are crucial for realistic physics simulation.

-   **Joints**: A joint connects two links and defines their relative motion.
    -   **`type`**: The most important attribute. Common types are `revolute` (a hinge), `continuous` (a wheel), `prismatic` (a slider), and `fixed` (a rigid connection).
    -   **`<parent>` & `<child>`**: These tags define the tree structure, connecting a parent link to a child link.
    -   **`<origin>`**: Defines the transform (position and orientation) from the parent's coordinate frame to the child's.
    
    :::note
    For more complex robots, URDF files can become very long and repetitive. The `xacro` (XML Macros) tool is commonly used to simplify URDF files by allowing macros, variables, and mathematical expressions. We will use plain URDF for now for clarity.
    :::
    
### System Diagram

```ascii
+---------------------------+      +---------------------------+
| joint_state_publisher_gui |----->|   robot_state_publisher   |
+---------------------------+      +---------------------------+
             |                                  |
             | Publishes joint angles           | Publishes coordinate transforms
             |                                  |
   [ /joint_states ] (Topic)          [ /tf ] & [ /robot_description ] (Topics)
             |                                  |
             +----------------------------------+
                               |
                               v
                       +----------------+
                       |     RViz2      |
                       +----------------+
```
The `joint_state_publisher_gui` lets you move sliders. The `robot_state_publisher` reads the URDF and the joint angles, calculates the 3D pose of each link, and publishes this information as coordinate transforms. RViz2 then uses these transforms and the URDF's visual tags to draw the robot.

---

## Lab: Building a Robot Arm in URDF

In this lab, you'll create a package for your robot's description, write a URDF for a simple two-link arm, and visualize it in RViz2.

### 1. Create a Description Package

In your workspace's `src` directory, create a new package:
```bash
ros2 pkg create --build-type ament_python my_robot_description
```
Inside this package, create three new directories: `urdf`, `launch`, and `rviz`.

### 2. Write the URDF File

Inside the `urdf` directory, create a file named `my_robot.urdf` and add the following content. This defines a base, an arm link, and a hand link, connected by two revolute joints.

```xml
<?xml version="1.0"?>
<robot name="my_robot">
  <link name="base_link">
    <visual>
      <geometry>
        <cylinder length="0.05" radius="0.1"/>
      </geometry>
      <material name="grey">
        <color rgba="0.5 0.5 0.5 1"/>
      </material>
    </visual>
  </link>

  <joint name="arm_joint" type="revolute">
    <parent link="base_link"/>
    <child link="arm_link"/>
    <origin xyz="0 0 0.025" rpy="0 0 0"/>
    <axis xyz="0 1 0"/>
    <limit lower="-1.57" upper="1.57" effort="10" velocity="1"/>
  </joint>

  <link name="arm_link">
    <visual>
      <geometry>
        <box size="0.5 0.05 0.05"/>
      </geometry>
      <origin xyz="0.25 0 0" rpy="0 0 0"/>
      <material name="blue">
        <color rgba="0 0 1 1"/>
      </material>
    </visual>
  </link>

  <joint name="hand_joint" type="revolute">
    <parent link="arm_link"/>
    <child link="hand_link"/>
    <origin xyz="0.5 0 0" rpy="0 0 0"/>
    <axis xyz="0 0 1"/>
    <limit lower="-1.57" upper="1.57" effort="10" velocity="1"/>
  </joint>

  <link name="hand_link">
    <visual>
      <geometry>
        <sphere radius="0.05"/>
      </geometry>
      <material name="red">
        <color rgba="1 0 0 1"/>
      </material>
    </visual>
  </link>
</robot>
```

### 3. Create a Launch File and RViz2 Config

-   First, launch RViz2 by itself (`ros2 run rviz2 rviz2`).
-   In the "Displays" panel, click "Add" and select "RobotModel".
-   In the "Global Options", set the "Fixed Frame" to `base_link`.
-   Save this configuration by going to `File -> Save Config As...` and saving it as `display.rviz` inside your `my_robot_description/rviz` directory.

-   Now, create a file named `display.launch.py` in your `launch` directory with the following content. This launch file will automate the process of loading the URDF and starting all the necessary nodes.

```python
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
import xacro

def generate_launch_description():
    pkg_path = os.path.join(get_package_share_directory('my_robot_description'))
    urdf_path = os.path.join(pkg_path, 'urdf', 'my_robot.urdf')
    rviz_config_path = os.path.join(pkg_path, 'rviz', 'display.rviz')

    robot_description_config = xacro.process_file(urdf_path)
    robot_description = {'robot_description': robot_description_config.toxml()}

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[robot_description]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher_gui',
            output='screen'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_path],
            output='screen'
        )
    ])
```

### 4. Configure `setup.py`

Open `setup.py` in your package's root and ensure it copies your new directories.

```python
# ... other setup code ...
from glob import glob
import os

package_name = 'my_robot_description'

setup(
    # ... other parameters ...
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        (os.path.join('share', package_name, 'rviz'), glob('rviz/*.rviz')),
    ],
)
```

### 5. Build and Launch

Navigate to your workspace root, build, and source:
```bash
colcon build
source install/setup.bash
```
Finally, launch your robot model:
```bash
ros2 launch my_robot_description display.launch.py
```
### Verification

- [X] RViz2 should open and display your robot arm.
- [X] A `joint_state_publisher_gui` window should appear.
- [X] Moving the sliders in the GUI should cause the corresponding joints of the robot arm in RViz2 to move.

You have now successfully described a robot's physical structure and brought it to life in a virtual environment!