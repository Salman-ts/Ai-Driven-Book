# Authoritative Sources for ROS 2 Navigation Stack (Nav2)

This document lists primary sources for understanding the ROS 2 Navigation Stack (Nav2), as required by Task 1.14.1.

## Primary Sources (Official Nav2 Documentation)

1.  **Nav2 Documentation**: The official and most comprehensive source for Nav2, including an overview of its architecture, core concepts, and tutorials.
    -   URL: [https://navigation.ros.org/](https://navigation.ros.org/)

2.  **Nav2 Architecture and Concepts**: Essential reading for understanding how Nav2 works, including its modular design and behavior trees.
    -   **Overview**: [https://navigation.ros.org/overview.html](https://navigation.ros.org/overview.html)
    -   **Concepts**: [https://navigation.ros.org/concepts.html](https://navigation.ros.org/concepts.html)

3.  **Key Nav2 Components**:
    -   **`amcl` (Adaptive Monte Carlo Localization)**: For probabilistic localization using a particle filter.
        -   URL: [https://navigation.ros.org/configuration/packages/amcl.html](https://navigation.ros.org/configuration/packages/amcl.html)
    -   **`slam_toolbox`**: For Simultaneous Localization and Mapping (SLAM).
        -   URL: [https://navigation.ros.org/configuration/packages/slam_toolbox.html](https://navigation.ros.org/configuration/packages/slam_toolbox.html)
    -   **Global Planners (e.g., `NavFn`, `SmacPlanner`)**: For computing a path from start to goal on a static map.
        -   URL: [https://navigation.ros.org/configuration/packages/navfn_planner.html](https://navigation.ros.org/configuration/packages/navfn_planner.html)
    -   **Local Planners (e.g., `DwbLocalPlanner`, `TebLocalPlanner`)**: For computing a safe, collision-free velocity command to follow the global path and avoid dynamic obstacles.
        -   URL: [https://navigation.ros.org/configuration/packages/dwb_local_planner.html](https://navigation.ros.org/configuration/packages/dwb_local_planner.html)
    -   **Costmaps**: Layers that represent environmental information, including obstacles, for planning.
        -   URL: [https://navigation.ros.org/configuration/costmap_filters/costmap_filter.html](https://navigation.ros.org/configuration/costmap_filters/costmap_filter.html)

4.  **Nav2 Tutorials**: Step-by-step guides for setting up and using Nav2 in various scenarios.
    -   **Getting Started**: [https://navigation.ros.org/tutorials/index.html](https://navigation.ros.org/tutorials/index.html)
    -   **SLAM with Nav2**: [https://navigation.ros.org/tutorials/docs/navigation_system.html](https://navigation.ros.org/tutorials/docs/navigation_system.html) (Look for SLAM examples within this or related tutorials)

## Secondary Sources (Community and Examples)

1.  **Nav2 Bringup Repository**: Contains example launch files and configurations for various robot types.
    -   URL: [https://github.com/ros-planning/navigation2/tree/main/nav2_bringup](https://github.com/ros-planning/navigation2/tree/main/nav2_bringup)
