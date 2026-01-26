## Chapter 5: Unity Visualization — The Hollywood Upgrade

Gazebo is a powerful and practical simulator, but for photorealistic rendering, commercial presentations, or creating stunning visuals, many roboticists turn to game engines. **Unity** is one of the most popular choices for creating high-fidelity digital twins.

This chapter will provide a conceptual overview and lab outline for using Unity as a high-quality visualizer for your existing ROS 2/Gazebo simulation.

### Core Concept: The TCP Bridge

Unity does not have the same native ROS 2 integration as Gazebo. Instead, it communicates with a ROS 2 system over a network using a TCP bridge.

:::note
The TCP bridge approach offers greater flexibility, allowing the ROS 2 system and the Unity application to run on separate machines or even different operating systems, communicating over standard network protocols.
:::


The two key components are:
1.  **`ROS-TCP-Connector` (Unity side)**: A C# package that runs in Unity. It starts a TCP server, listens for connections, and handles converting ROS messages to and from Unity's native C# objects.
2.  **`ros_tcp_endpoint` (ROS side)**: A Python ROS 2 node that connects to the Unity server. It subscribes to ROS topics, forwards the messages to Unity, and receives messages from Unity to publish back to the ROS network.

This architecture allows your core simulation (Gazebo) and your high-fidelity visualizer (Unity) to run completely independently, even on different machines.

### System Diagram

```ascii
+------------------------+
|    Gazebo Simulation   |
| (Physics & Control)    |
+------------------------+
    |           ^
    |           |
    v           |
+------------------------+
| ROS 2 Graph (/tf, etc.)|
+------------------------+
    |           ^
    | Forwards  | Receives
    v           |
+------------------------+      TCP/IP      +------------------------+
|  ros_tcp_endpoint      |<---------------->| ROS-TCP-Connector      |
|  (ROS 2 Node)          |                  | (Unity Script)         |
+------------------------+                  +------------------------+
                                                   |
                                                   v
                                          +------------------------+
                                          |     Unity Engine       |
                                          | (High-Fidelity Render) |
                                          +------------------------+
```

---

## Lab: Visualizing Your Robot in Unity

In this lab, you'll set up a Unity project to act as a real-time, high-fidelity visualizer for the Gazebo simulation you've already built.

### 1. Set Up Unity Project

-   Install Unity Hub and the recommended Unity Editor version.
-   Create a new 3D project.
-   Using the Unity Package Manager, install the official Unity Robotics packages:
    -   `ROS-TCP-Connector`
    -   `URDF-Importer`
    -   `Unity-Robotics-Visualizations`

### 2. Import the Robot

-   In the Unity Editor, use the `Robotics -> URDF Importer` menu to import your `diff_drive.urdf` file.
-   This will create a "prefab" (a reusable asset) of your robot. Configure the importer to use `ArticulationBody` components, which are Unity's system for physics-based robotics joints.

### 3. Create the Unity Scene

-   Create a new scene.
-   Add a ground plane and lighting to make it look good.
-   Drag your imported robot prefab into the scene.
-   Add the "ROS Connection" prefab to the scene and configure it with the IP address of the machine running ROS.

### 4. Update the ROS 2 Launch

Modify your main `gazebo.launch.py` to also start the ROS-side TCP endpoint.
```python
# In gazebo.launch.py
# ... other nodes ...
Node(
    package='ros_tcp_endpoint',
    executable='default_server_endpoint',
    name='ros_endpoint'
),
```

### 5. Visualize Robot and Sensor Data

-   Attach the provided `SourceDestinationSetter` C# script to your robot model in Unity. This script automatically handles subscribing to `/joint_states` and updating the robot's joint angles.
-   Add a `LaserScan` visualizer component to the scene from the Visualizations package and configure it to subscribe to the `/scan` topic.

### 6. Run the Full System

-   Launch your ROS 2 system: `ros2 launch my_robot_bringup gazebo.launch.py`. This starts Gazebo, your robot, the controllers, the sensors, and the TCP endpoint.
-   Press the "Play" button in the Unity Editor.

### Verification

- [X] The robot in the Unity scene should move in perfect sync with the robot in Gazebo.
- [X] The LIDAR scan data from the Gazebo simulation should be rendered in real-time in the Unity 3D scene.
- [X] You have successfully used a professional game engine as a high-fidelity digital twin visualizer.

This workflow, separating physics simulation from high-quality rendering, is common in professional robotics development for creating demos, collecting synthetic data, and building user interfaces.