# Module 1: The Robotic Nervous System

## Chapter 1: ROS 2 Fundamentals — Your Robot's Central Command

Welcome to the world of robotics! Before we can build intelligent machines, we need to understand their nervous system. In modern robotics, that nervous system is the Robot Operating System (ROS), specifically its latest iteration, ROS 2.

This chapter will introduce you to the absolute fundamentals of ROS 2. By the end, you'll be able to speak the language of ROS and take your first steps in controlling a simulated robot.

### Core Concepts: The ROS 2 Graph

Imagine a bustling city. You have different specialists (bakers, blacksmiths, merchants) who need to communicate and work together. This is a perfect analogy for a ROS 2 system. Each specialist is a **Node**, and they communicate over a network of pathways.

Here are the key elements of this network, which we call the **ROS 2 Graph**:

-   **Nodes**: A node is the main computational unit in ROS 2. Think of it as a small program that does one thing well. You might have a node for reading sensor data, another for controlling a motor, and a third for planning a path.
-   **Topics**: Topics are communication "channels" or "buses." A node can **publish** messages to a topic, and any number of other nodes can **subscribe** to that topic to receive those messages. This is great for continuous data streams, like camera feeds or laser scans.
-   **Services**: Services are for request/response interactions. A **client** node sends a request to a **server** node and waits for a response. This is a one-to-one communication, perfect for when you need to ask a question and get an answer, like "What's the robot's current position?"
-   **Actions**: Actions are for long-running tasks. An **action client** sends a goal to an **action server** (e.g., "Navigate to the kitchen"). The server provides continuous feedback (e.g., "I'm 50% of the way there") and a final result. This is more robust than a service for tasks that take time to complete.
-   **Launch Files**: These are scripts that start up and configure a whole team of nodes. As your robot gets more complex, launch files become essential for bringing the entire system online correctly.

<div class="glass-card">
  ![ROS 2 Graph City Analogy](/img/chapters/ros2-graph-city.png)
  <details>
  <summary>🤖 <strong>AI Insight: Why "Nodes"?</strong></summary>
  <p>Think of <strong>Nodes</strong> like apps on your phone. One app handles the camera, another handles maps, and another plays music. In ROS 2, we break a robot's brain into these small "apps" so if one crashes (like the music player), the robot doesn't stop driving (the map app is still safe!).</p>
  </details>
</div>

### System Diagram

<div class="glass-card">
  ![Teleop System Diagram](/img/chapters/turtlesim-teleop.png)
  <div class="admonition admonition-info">
    <div class="admonition-heading">
      <h5>🔍 Deep Dive: The Data Flow</h5>
    </div>
    <div class="admonition-content">
      <p>Follow the arrows in the diagram above!</p>
      <ul>
        <li><strong>Blue Line</strong>: Your keystrokes become velocity commands (Speed & Turn).</li>
        <li><strong>Green Line</strong>: The simulation tells us where the turtle actually ended up (X, Y, Angle).</li>
      </ul>
    </div>
  </div>
</div>

---

## Lab: Your First ROS 2 System with TurtleSim

In this lab, you'll get hands-on with these concepts by controlling a simple simulated turtle.

### 1. Environment Setup

First, you need to have ROS 2 Humble Hawksbill installed on Ubuntu 22.04. If you haven't done this, please follow the official ROS 2 installation guide.

Once installed, open a new terminal and "source" the ROS 2 setup files. This command makes all the ROS 2 tools available in your terminal.

:::note
You must run `source /opt/ros/humble/setup.bash` (or your specific ROS 2 installation path) in *every new terminal* you open when working with ROS 2. This command sets up the necessary environment variables.
:::

```bash
# Source the ROS 2 setup file (you'll do this in every new terminal)
source /opt/ros/humble/setup.bash
```

### 2. Running the Simulation

We'll use a fun, simple simulator called `turtlesim`.

In your first terminal, run the turtlesim node:
```bash
ros2 run turtlesim turtlesim_node
```
A window should appear with a lone turtle in the middle. This is your first ROS 2 node!

Now, open a **second terminal**. Remember to source the setup file again!
```bash
source /opt/ros/humble/setup.bash
```
In this second terminal, run the keyboard teleoperation node:
```bash
ros2 run turtlesim turtle_teleop_key
```

### 3. Controlling and Inspecting the System

Click on the second terminal (the one running `turtle_teleop_key`) and use the arrow keys on your keyboard. You should see the turtle in the simulation window move!

You are now controlling a ROS 2 system. The `turtle_teleop_key` node is publishing velocity commands on a topic, and the `turtlesim_node` is subscribing to that topic to move the turtle.

Let's verify this using ROS 2 command-line tools. Open a **third terminal** (and source it!).

**A. List the running nodes:**
```bash
ros2 node list
```
You should see `/turtlesim` and `/teleop_turtle`.

**B. List the topics:**
```bash
ros2 topic list
```
You'll see a few topics. The important one is `/turtle1/cmd_vel`. This is the channel the teleop node uses to send commands to the turtle.

**C. "Echo" a topic:**
Let's spy on the messages being sent. In the third terminal, run:
```bash
ros2 topic echo /turtle1/cmd_vel
```
Now, go back to the second terminal and press the arrow keys. You'll see `geometry_msgs/msg/Twist` messages appear in your third terminal, showing the linear and angular velocities being sent to the turtle. Press `Ctrl+C` in the third terminal to stop the echo.

**D. Call a service:**
The turtlesim node offers services to change the simulation. Let's spawn a new turtle. Run this command in your third terminal:
```bash
ros2 service call /spawn turtlesim/srv/Spawn "{'x': 2.0, 'y': 2.0, 'theta': 0.2, 'name': 'my_turtle'}"
```
A new turtle named `my_turtle` will appear in the simulation!

### Verification

You have successfully:
- [X] Launched and controlled a ROS 2 simulation.
- [X] Used command-line tools to inspect nodes and topics.
- [X] Called a ROS 2 service to change the state of a running system.

Congratulations! You've taken your first steps into the larger world of ROS 2.