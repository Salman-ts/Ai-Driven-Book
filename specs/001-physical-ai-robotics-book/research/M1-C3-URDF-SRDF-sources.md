# Authoritative Sources for URDF/SRDF Format

This document lists primary sources for understanding the Unified Robot Description Format (URDF) and Semantic Robot Description Format (SRDF), as required by Task 1.3.1.

## Primary Sources (Official ROS Documentation)

1.  **URDF and SRDF Overview**: A high-level introduction to the purpose of both formats.
    -   URL: [https://docs.ros.org/en/humble/Related-Projects/MoveIt/Concepts/URDF-and-SRDF.html](https://docs.ros.org/en/humble/Related-Projects/MoveIt/Concepts/URDF-and-SRDF.html)

2.  **URDF Tutorials**: Although part of the original ROS 1 documentation, these tutorials are still the definitive guide to the URDF XML format and are referenced by the ROS 2 documentation.
    -   URL: [http://wiki.ros.org/urdf/Tutorials](http://wiki.ros.org/urdf/Tutorials)

3.  **Building a Visual Robot Model with URDF**: A step-by-step tutorial for creating a visual URDF model.
    -   URL: [http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch](http://wiki.ros.org/urdf/Tutorials/Building%20a%20Visual%20Robot%20Model%20with%20URDF%20from%20Scratch)

4.  **URDF XML Schema**: The official specifications for URDF tags.
    -   **`<link>`**: [http://wiki.ros.org/urdf/XML/link](http://wiki.ros.org/urdf/XML/link)
    -   **`<joint>`**: [http://wiki.ros.org/urdf/XML/joint](http://wiki.ros.org/urdf/XML/joint)
    -   **`<robot>`**: [http://wiki.ros.org/urdf/XML/robot](http://wiki.ros.org/urdf/XML/robot)

5.  **Using URDF with `robot_state_publisher`**: The ROS 2 tutorial for launching a URDF model and visualizing it in RViz2. This is the modern way to display and interact with a URDF.
    -   URL: [https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher.html](https://docs.ros.org/en/humble/Tutorials/Intermediate/URDF/Using-URDF-with-Robot-State-Publisher.html)

## Secondary Sources

1.  **Xacro**: An XML macro language for simplifying URDF files. While not strictly URDF, it is the standard way to write complex URDFs.
    -   URL: [http://wiki.ros.org/xacro](http://wiki.ros.org/xacro)
