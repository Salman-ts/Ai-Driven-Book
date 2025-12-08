# Authoritative Sources for ROS-Unity Integration

This document lists primary sources for understanding how to integrate ROS 2 with the Unity 3D engine, as required by Task 1.10.1.

## Primary Sources (Unity Documentation)

1.  **Unity Robotics Hub**: This is the official home for all of Unity's robotics packages and tutorials.
    -   URL: [https://github.com/Unity-Technologies/Unity-Robotics-Hub](https://github.com/Unity-Technologies/Unity-Robotics-Hub)

2.  **ROS TCP Connector**: This is the core package that enables communication between Unity and a ROS network. It creates a TCP endpoint that ROS nodes can connect to (via the corresponding ROS-side `ros_tcp_endpoint` package).
    -   URL: [https://github.com/Unity-Technologies/ROS-TCP-Connector](https://github.com/Unity-Technologies/ROS-TCP-Connector)

3.  **URDF Importer**: A Unity package that can parse a URDF file and automatically generate a corresponding articulated robot model inside the Unity scene.
    -   URL: [https://github.com/Unity-Technologies/URDF-Importer](https://github.com/Unity-Technologies/URDF-Importer)

4.  **Unity Robotics Visualizations Package**: This package provides ready-made C# components for visualizing common ROS message types in Unity, such as `LaserScan` and `PointCloud2`.
    -   URL: [https://github.com/Unity-Technologies/Unity-Robotics-Visualizations](https://github.com/Unity-Technologies/Unity-Robotics-Visualizations)

## Secondary Sources (Tutorials and Examples)

1.  **Unity Robotics Hub Tutorials**: The official tutorials are the best place to start. They cover setting up a new project, importing a robot, and connecting to ROS.
    -   URL: [https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/README.md](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/README.md)

2.  **Pick-and-Place Tutorial**: A more advanced tutorial that demonstrates a full pick-and-place application using ROS 2, MoveIt, and Unity. This is a good example of a complete system.
    -   URL: [https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/README.md](https://github.com/Unity-Technologies/Unity-Robotics-Hub/blob/main/tutorials/pick_and_place/README.md)
