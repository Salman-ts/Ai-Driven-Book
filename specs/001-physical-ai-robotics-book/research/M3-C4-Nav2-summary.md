# Summary of Nav2 Concepts

This document synthesizes the core concepts and components of the ROS 2 Navigation Stack (Nav2), as required by Task 1.14.2.

## What is Nav2?

Nav2 is the modular, behavior-tree-based navigation stack for ROS 2. Its primary goal is to enable a mobile robot to autonomously navigate from a starting pose to a goal pose while avoiding obstacles. Unlike its ROS 1 predecessor, Nav2 is highly configurable and built around a flexible Behavior Tree (BT) architecture, allowing for easier customization and robustness.

## Core Components and Their Roles

Nav2 is composed of many independent ROS 2 nodes, each responsible for a specific task. They communicate via standard ROS 2 interfaces (topics, services, actions).

1.  **Map Server**: Provides the static map of the environment (usually a `OccupancyGrid` message) to other Nav2 components.

2.  **State Estimator (e.g., `robot_localization` or `ekf_node`)**: Fuses sensor data (like odometry, IMU, GPS) to provide an accurate estimate of the robot's current pose (`odom` frame).

3.  **Localization**: Determines the robot's position within a known map.
    -   **`AMCL` (Adaptive Monte Carlo Localization)**: A probabilistic localization method that uses a particle filter. It requires an initial pose estimate and a static map.
    -   **`SLAM_Toolbox`**: Performs Simultaneous Localization and Mapping. It builds a map of an unknown environment while simultaneously localizing the robot within that map. Often used to create the initial map.

4.  **Costmaps (Local and Global)**: Gridded representations of the environment that provide information about obstacles for path planning.
    -   **Global Costmap**: A large, static map used for global planning. It typically includes known obstacles from the `Map Server` and can incorporate static sensor readings.
    -   **Local Costmap**: A smaller, dynamic map centered around the robot, continuously updated with real-time sensor data. It includes dynamic obstacles and is used for local path planning and collision avoidance.

5.  **Planners**:
    -   **Global Planner (e.g., `NavFn`, `SmacPlanner`)**: Calculates an optimal path from the robot's current location to the goal location on the global costmap. This path typically ignores dynamic obstacles as it's computed on a static map.
    -   **Local Planner (e.g., `DwbLocalPlanner`, `TebLocalPlanner`)**: Also known as a motion planner or controller. It takes the global path and the local costmap, and generates a short-term, collision-free trajectory. It then translates this trajectory into velocity commands (`Twist` messages) for the robot's base controller. This is where dynamic obstacle avoidance occurs.

6.  **Recovery Behaviors**: If the robot gets stuck or is unable to follow its path, Nav2 can execute recovery actions (e.g., `Backup`, `Spin`, `ClearCostmap`) to try and free itself or re-localize.

7.  **Behavior Tree (BT) Navigator**: The orchestrator of Nav2. It defines the sequence of actions, decisions, and recovery behaviors the robot takes to achieve its navigation goal. This allows for flexible and robust navigation strategies.

8.  **Waypoints Follower**: A simple behavior that allows the robot to visit a sequence of poses.

## Communication Flow for Navigation

1.  User sends a navigation goal (e.g., via RViz2 or a client application) to the `navigate_to_pose` action server.
2.  The BT Navigator's `navigate_to_pose` action is triggered.
3.  The BT first localizes the robot (e.g., using `AMCL` if a map exists).
4.  A global path is planned from the robot's current position to the goal.
5.  The local planner then attempts to follow this path while avoiding obstacles in the local costmap, sending velocity commands to the robot's base.
6.  If the robot encounters an issue, recovery behaviors are executed.
7.  Once the robot reaches the goal, the `navigate_to_pose` action completes successfully.
