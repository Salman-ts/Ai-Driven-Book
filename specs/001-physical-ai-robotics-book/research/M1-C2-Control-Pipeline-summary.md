# Summary of ROS 2 Python (`rclpy`) Concepts

This document synthesizes fundamental `rclpy` concepts for building ROS 2 nodes in Python, as required by Task 1.2.2.

## Core `rclpy` Components

-   **`rclpy.init()` and `rclpy.shutdown()`**: These functions initialize and shut down the ROS 2 communication middleware. Every `rclpy` program must call `init()` at the beginning and `shutdown()` at the end.

-   **`rclpy.create_node()`**: This function creates a ROS 2 node. The user provides a node name as an argument. The returned object is the handle to the node.

-   **`Node.create_publisher()`**: This method of the Node class creates a publisher. It requires the message type and the topic name as arguments. The returned publisher object is used to send messages.

-   **`Node.create_subscription()`**: This method creates a subscriber. It requires the message type, the topic name, and a callback function as arguments. The callback function is executed whenever a message is received on the topic.

-   **`rclpy.spin()` and `rclpy.spin_once()`**: These functions process events and invoke callbacks.
    -   `spin(node)` blocks execution and keeps the node "alive," continuously processing incoming messages and events until the node is shut down.
    -   `spin_once(node, timeout_sec=None)` processes a single batch of events and then returns. It is often used in loops for more complex applications where other tasks need to be done between processing ROS 2 events.

## Publisher/Subscriber Implementation Pattern

1.  **Import Libraries**: Import `rclpy` and the required message types (e.g., `from std_msgs.msg import String`).
2.  **Initialize `rclpy`**: Call `rclpy.init()`.
3.  **Create a Node**: Create a class that inherits from `rclpy.node.Node`.
4.  **Create Publisher/Subscriber**: Inside the node's `__init__` method, create publisher or subscriber objects using `self.create_publisher()` or `self.create_subscription()`.
5.  **Define Callback**: For a subscriber, define the callback method that will handle incoming messages.
6.  **Spin the Node**: In the main part of the script, create an instance of the node class and pass it to `rclpy.spin()`.
7.  **Shutdown**: Ensure `rclpy.shutdown()` is called after the spin function exits.
