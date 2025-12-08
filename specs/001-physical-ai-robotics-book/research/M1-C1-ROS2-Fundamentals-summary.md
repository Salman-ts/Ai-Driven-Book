# Summary of ROS 2 Core Concepts

This document synthesizes fundamental ROS 2 concepts based on the sources identified in Task 1.1.1, fulfilling the requirements of Task 1.1.2.

## ROS 2 Graph: The Big Picture

The ROS "graph" is the network of ROS 2 elements processing data together. It consists of:

-   **Nodes**: The main computational units in ROS. A node is an executable that performs a specific task (e.g., controlling a motor, reading a sensor, planning a path).
-   **Topics**: Buses over which nodes exchange messages. Nodes can "publish" messages to a topic or "subscribe" to a topic to receive messages. This is a one-to-many communication model.
-   **Services**: A request/response communication model. A client node sends a request to a service server node and waits for a response. This is a one-to-one communication model.
-   **Actions**: A communication model for long-running tasks. An action client sends a goal to an action server (e.g., "navigate to point A"). The server provides continuous feedback on the goal's progress and a final result. This is more robust than a service for tasks that take time.
-   **Launch Files**: Scripts (in Python or XML) that start up and configure a collection of nodes. They are essential for launching complex robotics systems with many interdependent components.

## Key Functions

-   **Nodes**: The "workers" of the system. Each node should have a single, clear purpose.
-   **Topics**: Used for continuous data streams, like sensor data or robot state.
-   **Services**: Used for quick, remote procedure calls where a result is needed immediately.
-   **Actions**: Used for tasks that have a defined goal and require feedback during execution.
-   **Launch Files**: The "orchestrators" that bring the entire system online correctly.
