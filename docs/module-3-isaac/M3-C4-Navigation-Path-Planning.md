## Chapter 4: Navigation & Path Planning with Nav2

An intelligent robot needs to be able to move purposefully through its environment. The ROS 2 Navigation Stack, known as **Nav2**, is the powerful, industry-standard framework for enabling autonomous navigation.

This chapter will teach you how to configure and run Nav2 in your Isaac Sim environment. You'll learn how to create a map of an unknown world (SLAM), localize your robot within that map, and send it to a goal, watching as it autonomously avoids obstacles to get there.

### Core Concepts: The Nav2 Stack

Nav2 is a complex system of interacting nodes, each with a specific job.

1.  **Map Server**: Provides a static map of the world.
2.  **AMCL (Adaptive Monte Carlo Localization)**: The localization engine. It uses a particle filter to compare incoming sensor data (like a laser scan) to the static map, determining the robot's most likely position.
3.  **Costmaps (Global & Local)**: These are the brains of obstacle avoidance.
    -   **Global Costmap**: A large map used by the global planner. It includes obstacles from the static map.
    -   **Local Costmap**: A small, rolling window around the robot that is continuously updated with real-time sensor data, allowing it to see and react to dynamic obstacles.
4.  **Planners**:
    -   **Global Planner**: Computes a long-range path from the robot's current location to a goal, usually using an algorithm like A*.
    -   **Local Planner**: Computes short-term, feasible velocity commands to follow the global path while avoiding obstacles in the local costmap.
5.  **Behavior Tree (BT) Navigator**: The orchestrator of Nav2. Instead of a hard-coded state machine, Nav2 uses flexible Behavior Trees to manage the process of planning, moving, and recovering from failures.

:::note
Behavior Trees offer a modular and robust way to design complex robot behaviors. They are increasingly popular in robotics and game AI for their ability to handle dynamic environments and recovery strategies elegantly.
:::


### System Diagram

```ascii
+----------------+      +----------------+
|   Goal Pose    |----->|  BT Navigator  |
| (From RViz2)   |      +----------------+
+----------------+       |           |
                         | Controls  | Gets robot pose
                         v           ^
+----------------+      +----------------+      +----------------+
| Local Planner  |<---->|  Costmaps      |<---->|    AMCL        |
+----------------+      +----------------+      +----------------+
      |                                                ^
      | Sends velocity commands                        | Reads /scan & /tf
      v                                                |
+----------------+                             +----------------+
|  Robot Base    |                             | LIDAR & Odometry |
| (/cmd_vel)     |                             +----------------+
+----------------+
```

### System Diagram

```ascii
+----------------+      +----------------+
|   Goal Pose    |----->|  BT Navigator  |
| (From RViz2)   |      +----------------+
+----------------+       |           |
                         | Controls  | Gets robot pose
                         v           ^
+----------------+      +----------------+      +----------------+
| Local Planner  |<---->|  Costmaps      |<---->|    AMCL        |
+----------------+      +----------------+      +----------------+
      |                                                ^
      | Sends velocity commands                        | Reads /scan & /tf
      v                                                |
+----------------+                             +----------------+
|  Robot Base    |                             | LIDAR & Odometry |
| (/cmd_vel)     |                             +----------------+
+----------------+
```

---

## Lab: Autonomous Navigation in Isaac Sim

In this lab, you'll use Isaac Sim's built-in ROS 2 bridge to connect to a full Nav2 stack, map an environment, and perform autonomous navigation.

### 1. Prepare the Isaac Sim Environment

-   Launch Isaac Sim.
-   Create an interesting environment for your robot to navigate. Use the `Create -> Shapes` menu to add walls, cubes, and other obstacles. The `simple_room` environment is a good starting point.
-   Add your differential drive robot to the scene.
-   In the `Property` panel for your robot, enable the ROS 2 odometry and LIDAR sensors. Make sure they are publishing to the `/odom` and `/scan` topics, respectively. Isaac Sim's native bridge makes this much easier than Gazebo plugins.

### 2. Configure and Launch Nav2

-   Create a new ROS 2 package for your navigation configuration (e.g., `my_robot_nav`).
-   Inside, create a `config` directory containing YAML files with the parameters for Nav2. You can get a good starting set from the official Nav2 tutorials or the `nav2_bringup` package. You'll need to adjust parameters like the robot's footprint and sensor topics.
-   Create a launch file (`nav_isaac.launch.py`) that launches the entire Nav2 stack, passing your custom configuration files to it.

### 3. Perform SLAM

-   First, we need a map. We'll use SLAM (Simultaneous Localization and Mapping).
-   Create a separate launch file that starts the `slam_toolbox` node.
-   Start your Isaac Sim simulation.
-   Launch your SLAM launch file: `ros2 launch my_robot_nav slam.launch.py`.
-   In a new terminal, run `teleop_twist_keyboard` to drive your robot around.
-   As you drive, you will see the map being built in RViz2.
-   Once you've mapped the whole area, save the map using the `ros2 run nav2_map_server map_saver_cli` command. This will create `my_map.pgm` and `my_map.yaml`.

### 4. Autonomous Navigation

-   Stop the SLAM process.
-   Modify your main `nav_isaac.launch.py` to load the map you just saved.
-   Launch the full Nav2 stack: `ros2 launch my_robot_nav nav_isaac.launch.py`.
-   In RViz2:
    -   Use the "2D Pose Estimate" tool to give Nav2 an idea of where the robot is on the map. AMCL will refine this.
    -   Use the "2D Goal Pose" tool to set a navigation goal.

### Verification

- [X] In RViz2, you should see the global planner create a path (usually a green line).
- [X] Your robot in Isaac Sim should begin moving, following the path.
- [X] The local planner's path should appear (usually a blue line), adjusting to avoid obstacles.
- [X] The robot should autonomously reach its destination.

You have just unlocked one of the most powerful and fundamental capabilities in robotics: the ability for a machine to navigate its own world.