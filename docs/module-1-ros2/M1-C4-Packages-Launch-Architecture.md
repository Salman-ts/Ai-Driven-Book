## Chapter 4: Packages & Launch Architecture — Managing Complexity

As your robotics projects grow, you'll find yourself managing dozens of nodes, configurations, and models. ROS 2 provides two key tools to manage this complexity: **Packages** and **Launch Files**.

This chapter will teach you how to structure a complex project by refactoring your code into multiple, single-purpose packages and how to use Python launch files to start and configure your entire system with a single command.

### Core Concepts: Modularity and Orchestration

-   **Packages**: A package is the fundamental unit of organization in ROS 2. The best practice is to have each package serve a single, clear purpose. For example:
    -   `my_robot_description`: Contains only the robot's URDF model, 3D meshes, and RViz configurations.
    -   `my_robot_bringup`: Contains the main launch files for starting the robot.
    -   `my_robot_control`: Contains the controller nodes.
    -   `my_robot_navigation`: Contains navigation-specific configurations.
    This separation of concerns makes your project easier to understand, maintain, and reuse.

:::tip
For very large projects, you might encounter **metapackages**. A metapackage is an empty package that simply groups related packages together (e.g., a `robot_software` metapackage that depends on `robot_description`, `robot_control`, `robot_navigation`). This simplifies dependency management and installation.
:::


-   **Launch Files**: A launch file is a script that starts a collection of ROS 2 nodes and sets their parameters. Python launch files are the most powerful and common type. They allow you to programmatically define your system's startup sequence.
    -   **`IncludeLaunchDescription`**: This powerful action allows one launch file to include another. This is the key to creating a modular launch architecture, where a top-level launch file can bring up multiple subsystems, each defined in its own launch file.
    -   **Launch Arguments**: You can pass arguments to your launch files from the command line, allowing you to change behavior without editing code. For example, you could have a `use_simulation` argument that, when true, starts a simulator and, when false, connects to a physical robot.

### System Diagram

```ascii
+------------------------------+
|   Top-Level Launch File      |
|    (robot_bringup.launch.py) |
+------------------------------+
    |
    | Includes...
    |
    +-----> +--------------------------+
    |       |   Display Launch File    |
    |       |  (display.launch.py)     |
    |       +--------------------------+
    |           |
    |           +-----> (robot_state_publisher)
    |           |
    |           +-----> (joint_state_publisher_gui)
    |           |
    |           +-----> (rviz2)
    |
    | Starts...
    |
    +-----> (my_publisher_node)
    |
    +-----> (my_subscriber_node)
```

### System Diagram

```ascii
+------------------------------+
|   Top-Level Launch File      |
|    (robot_bringup.launch.py) |
+------------------------------+
    |
    | Includes...
    |
    +-----> +--------------------------+
    |       |   Display Launch File    |
    |       |  (display.launch.py)     |
    |       +--------------------------+
    |           |
    |           +-----> (robot_state_publisher)
    |           |
    |           +-----> (joint_state_publisher_gui)
    |           |
    |           +-----> (rviz2)
    |
    | Starts...
    |
    +-----> (my_publisher_node)
    |
    +-----> (my_subscriber_node)
```

---

## Lab: Refactoring into a Professional Project Structure

In this lab, you'll take the packages you've already created and reorganize them into a more scalable, professional structure.

### 1. Refactor Packages

We will move the launch file from `my_robot_description` into a new, dedicated `bringup` package.

First, create the new package in your `src` directory:
```bash
ros2 pkg create --build-type ament_python my_robot_bringup
```

Now, move the `display.launch.py` file from `my_robot_description/launch` to `my_robot_bringup/launch`.

You'll need to update `my_robot_bringup/launch/display.launch.py` to find the URDF and RViz files, which are now in a different package. We use `get_package_share_directory` to do this.

```python
# In display.launch.py

import os
from ament_index_python.packages import get_package_share_directory
# ... other imports

# Find the path to the other package
description_pkg_path = get_package_share_directory('my_robot_description')
urdf_path = os.path.join(description_pkg_path, 'urdf', 'my_robot.urdf')
rviz_config_path = os.path.join(description_pkg_path, 'rviz', 'display.rviz')

# ... rest of the launch file uses these new paths
```

### 2. Create a Top-Level Launch File

Inside `my_robot_bringup/launch`, create a new file `robot.launch.py`. This will be our main entry point. It will *include* the display launch file and also start our chatter nodes from Chapter 2.

```python
# In robot.launch.py

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    bringup_pkg_path = get_package_share_directory('my_robot_bringup')
    
    display_launch_path = os.path.join(
        bringup_pkg_path, 'launch', 'display.launch.py')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(display_launch_path)
        ),
        Node(
            package='my_first_package',
            executable='my_publisher_node',
            name='chatter_publisher'
        ),
        Node(
            package='my_first_package',
            executable='my_subscriber_node',
            name='chatter_subscriber'
        ),
    ])
```

### 3. Update `setup.py` and Build

Update the `setup.py` file in `my_robot_bringup` to install the new launch files. Also, update the `package.xml` to add an `<exec_depend>` on `my_robot_description` and `my_first_package`.

Go to your workspace root, build, and source:
```bash
colcon build
source install/setup.bash
```

### 4. Launch the Full System

Now, you can start everything with a single command:
```bash
ros2 launch my_robot_bringup robot.launch.py
```

### Verification

- [X] RViz2, the robot model, the joint state GUI, and both chatter nodes should all start correctly.
- [X] You have successfully refactored your code into a multi-package architecture.
- [X] You have created a top-level launch file to orchestrate a complex system.

This modular structure is how real robotics projects are built, and it will be the foundation for the rest of this book.