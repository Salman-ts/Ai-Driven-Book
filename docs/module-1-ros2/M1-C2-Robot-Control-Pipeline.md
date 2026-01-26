## Chapter 2: The Robot Control Pipeline — Writing Your First Node

In the last chapter, we used pre-built ROS 2 nodes. Now, it's time to create our own. This chapter will teach you how to write your own ROS 2 nodes in Python, the most common language for high-level robotics programming. You'll learn the fundamental publisher/subscriber pattern, which is the backbone of most ROS 2 applications.

### Core Concepts: The `rclpy` Client Library

To write a ROS 2 node in Python, we use the `rclpy` (ROS Client Library for Python). It provides all the tools we need to interact with the ROS 2 graph.

Here's the basic structure of a Python ROS 2 node:

1.  **Import Libraries**: We import `rclpy`, the `Node` class, and any message types we want to use.
2.  **Define a Node Class**: We create a class that inherits from `rclpy.node.Node`.
3.  **Create Publishers/Subscribers**: Inside the node's `__init__` method, we create publisher or subscriber objects.
    -   `self.create_publisher()`: Creates a publisher. It needs the message type, topic name, and a "quality of service" (QoS) setting.
    -   `self.create_subscription()`: Creates a subscriber. It needs the message type, topic name, a callback function, and a QoS setting.
4.  **Define the Callback**: For a subscriber, the callback function is the most important part. This function is automatically called whenever a new message arrives on the subscribed topic.
5.  **Main Execution Block**: We initialize `rclpy`, create an instance of our node class, and then "spin" the node. `rclpy.spin()` enters a loop, keeping the node alive and processing any incoming messages or events until you shut it down (e.g., with `Ctrl+C`).

### System Diagram

```ascii
+-----------------------+      +--------------------------+
|  /my_publisher_node   |----->|     /my_subscriber_node  |
+-----------------------+      +--------------------------+
           |                             |
           | Publishes String messages   | Subscribes to String messages
           |                             |
           +---------[ /chatter ]--------+
                       (Topic)
```

---

## Lab: Creating a Publisher and Subscriber

In this lab, you'll create a ROS 2 package and write two nodes: one that publishes "chatter" and another that listens to it.

### 1. Create a ROS 2 Package

First, we need a package to hold our code.

In your terminal, navigate to your ROS 2 workspace's `src` directory (e.g., `~/ros2_ws/src`) and run:
```bash
ros2 pkg create --build-type ament_python my_first_package --dependencies rclpy std_msgs
```
This command creates a new directory named `my_first_package` with all the necessary files for a Python ROS 2 package.

### 2. Write the Publisher Node

Navigate into your new package: `cd my_first_package/my_first_package`. Create a new file named `publisher_node.py` and add the following code:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatterPublisher(Node):
    def __init__(self):
        super().__init__('my_publisher_node')
        self.publisher_ = self.create_publisher(String, 'chatter', 10)
        timer_period = 1.0  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello World: {self.i}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    chatter_publisher = ChatterPublisher()
    rclpy.spin(chatter_publisher)
    chatter_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 3. Write the Subscriber Node

In the same directory, create a new file named `subscriber_node.py` with this code:

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class ChatterSubscriber(Node):
    def __init__(self):
        super().__init__('my_subscriber_node')
        self.subscription = self.create_subscription(
            String,
            'chatter',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    chatter_subscriber = ChatterSubscriber()
    rclpy.spin(chatter_subscriber)
    chatter_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 4. Configure `setup.py`

Now we need to tell ROS 2 how to run our nodes. Open the `setup.py` file in the root of your `my_first_package` directory and modify the `entry_points` section to look like this:

:::tip
Always remember to add new executable Python nodes to the `entry_points` in `setup.py`. This makes them discoverable and runnable using `ros2 run`.
:::

```python
# ... other setup code ...
entry_points={
    'console_scripts': [
        'my_publisher_node = my_first_package.publisher_node:main',
        'my_subscriber_node = my_first_package.subscriber_node:main',
    ],
},
# ... other setup code ...
```

### 5. Build and Run

Navigate back to the root of your workspace (e.g., `~/ros2_ws`) and build your package:
```bash
colcon build
```

Now, source your workspace's setup file. This is important!
```bash
source install/setup.bash
```

Open two terminals. In the first, run the publisher:
```bash
ros2 run my_first_package my_publisher_node
```
In the second, run the subscriber:
```bash
ros2 run my_first_package my_subscriber_node
```

### Verification

You have successfully:
- [X] Created a ROS 2 package.
- [X] Written a publisher node that sends messages on a timer.
- [X] Written a subscriber node that listens to messages and acts on them via a callback.
- [X] Built and run your own custom nodes.

You should see the publisher terminal printing "Publishing..." and the subscriber terminal printing "I heard...". You've just created your first ROS 2 control pipeline!