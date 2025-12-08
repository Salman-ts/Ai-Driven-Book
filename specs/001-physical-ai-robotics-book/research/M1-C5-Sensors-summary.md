# Summary of ROS 2 Sensor Concepts

This document synthesizes concepts related to common sensor message types and their visualization in RViz2, as required by Task 1.5.2.

## Common Sensor Message Types (`sensor_msgs`)

The `sensor_msgs` package provides a standard set of message definitions for sensor data, which allows different sensor drivers, processing nodes, and visualization tools to work together seamlessly.

-   **`LaserScan`**: Represents data from a 2D LIDAR or laser scanner.
    -   **Key Fields**:
        -   `header`: Contains the timestamp and coordinate frame ID (`frame_id`).
        -   `angle_min`, `angle_max`: The start and end angles of the scan in radians.
        -   `angle_increment`: The angular distance between measurements.
        -   `ranges`: An array of floating-point numbers representing the distance measurements for each angle.
    -   **RViz2 Display**: The `LaserScan` display type renders this as a set of points or lines in 2D space, showing detected obstacles.

-   **`Image`**: Represents a camera image.
    -   **Key Fields**:
        -   `header`: Timestamp and `frame_id`.
        -   `height`, `width`: The dimensions of the image.
        -   `encoding`: The color/pixel format (e.g., `rgb8`, `mono8`, `bgr8`).
        -   `data`: The raw image data as a byte array.
    -   **RViz2 Display**: The `Image` display type shows the video stream in a dedicated panel. Note that it does not render the image in the 3D scene. To project an image into the 3D world, a `Camera` display is needed, which also requires camera calibration info.

-   **`PointCloud2`**: A flexible message for representing n-dimensional point clouds. It is the standard for 3D LIDARs and depth cameras.
    -   **Key Fields**:
        -   `header`: Timestamp and `frame_id`.
        -   `height`, `width`: Can represent an organized (grid-like) or unorganized cloud.
        -   `fields`: An array describing the channels in the data (e.g., `x`, `y`, `z`, `intensity`, `rgb`).
        -   `data`: The raw point cloud data as a byte array.
    -   **RViz2 Display**: The `PointCloud2` display type renders the points in the 3D scene, allowing for rich visualization of the robot's 3D environment.

## Visualization in RViz2

RViz2 uses "Display" plugins to visualize data from different topics. To visualize sensor data, you must:

1.  **Add the Display**: Click "Add" in the Displays panel and choose the appropriate display type (e.g., `LaserScan`, `PointCloud2`).
2.  **Set the Topic**: In the display's properties, set the "Topic" to the name of the topic publishing the sensor data (e.g., `/scan`, `/my_camera/image_raw`).
3.  **Ensure TF is Correct**: RViz2 needs to know the relationship between the coordinate frame of the sensor (`frame_id` in the message header) and the other coordinate frames in the system (like the robot's `base_link` and the world's `map` frame). This is provided by the `/tf` topic, typically published by `robot_state_publisher`. If the transforms are missing, you will see errors in the display's status.
