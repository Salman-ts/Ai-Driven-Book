# Summary of URDF/SRDF Concepts

This document synthesizes key concepts of the Unified Robot Description Format (URDF) and its visualization in RViz2, as required by Task 1.3.2.

## URDF (Unified Robot Description Format)

URDF is an XML format used in ROS to describe the physical structure of a robot. It represents the robot as a tree of links connected by joints.

### Key URDF Elements

-   **`<robot name="my_robot">`**: The root element of the URDF file.

-   **`<link name="link_name">`**: A link represents a rigid body part of the robot (e.g., a forearm, a wheel, a torso). Each link has its own coordinate frame. A link element typically contains three sub-elements:
    -   **`<visual>`**: Defines the visual appearance of the link (how it looks). This can be a simple geometric shape (box, cylinder, sphere) or a reference to a 3D mesh file (like `.stl` or `.dae`).
    -   **`<collision>`**: Defines the collision geometry of the link (its physical shape for physics calculations). This is often a simpler version of the visual geometry to speed up collision checking.
    -   **`<inertial>`**: Defines the dynamic properties of the link, including its mass and inertia tensor. This is crucial for accurate physics simulation.

-   **`<joint name="joint_name" type="joint_type">`**: A joint connects two links together and defines how they can move relative to each other. Key attributes include:
    -   **`type`**: The type of motion allowed. Common types are:
        -   `revolute`: A hinge joint that rotates around a single axis (e.g., an elbow).
        -   `continuous`: A revolute joint with no angle limits (e.g., a wheel).
        -   `prismatic`: A sliding joint that moves along a single axis.
        -   `fixed`: A rigid connection between two links with no relative motion.
    -   **`<parent link="parent_link_name"/>`**: The "parent" link in the kinematic tree.
    -   **`<child link="child_link_name"/>`**: The "child" link in the kinematic tree.
    -   **`<origin xyz="..." rpy="..."/>`**: Defines the transform (position and orientation) from the parent link's coordinate frame to the child link's coordinate frame.
    -   **`<axis xyz="..."/>`**: Defines the axis of rotation (for revolute joints) or translation (for prismatic joints).

## Visualization in RViz2

-   **`robot_state_publisher`**: This ROS 2 node is the key to visualizing a URDF. It reads the URDF file, subscribes to the `/joint_states` topic (which contains the current angle/position of each joint), and publishes the required coordinate frame transformations (`/tf`) for the entire robot.
-   **RViz2**: The standard ROS 2 visualization tool. By adding a "RobotModel" display and setting the correct topic, RViz2 subscribes to the `/tf` data and renders the robot model according to the URDF's visual tags and the current joint states.
-   **`joint_state_publisher_gui`**: A simple graphical tool that provides sliders to manually change the values on the `/joint_states` topic, allowing you to move the robot's joints in RViz2.
