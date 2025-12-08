# Lab Outline: M3-C3 - Isaac ROS Jetson Pipeline

This document outlines the lab requirements for Module 3, Chapter 3, as required by Task 1.13.3.

## Lab Goal

The user will set up their NVIDIA Jetson device, deploy a Docker container with Isaac ROS, connect a RealSense camera, and run a basic Isaac ROS perception pipeline to visualize its output.

## Lab Requirements

1.  **Jetson Device Setup**:
    -   [ ] Install JetPack SDK on the Jetson Orin Nano/NX Developer Kit using SDK Manager.
    -   [ ] Verify the JetPack installation (e.g., check CUDA, TensorRT versions).
    -   [ ] Install Docker and NVIDIA Container Toolkit on the Jetson.

2.  **RealSense Camera Setup**:
    -   [ ] Connect an Intel RealSense D435i camera to the Jetson via USB.
    -   [ ] Install the `realsense-ros` ROS 2 wrapper.
    -   [ ] Launch the RealSense camera node and verify that `sensor_msgs/Image` and `sensor_msgs/PointCloud2` messages are being published on the correct topics.

3.  **Isaac ROS Container Deployment**:
    -   [ ] Pull an appropriate Isaac ROS base Docker image from NVIDIA NGC (e.g., `nvcr.io/nvidia/isaac-ros/isaac_ros_base:humble`).
    -   [ ] Create a Docker container, mapping the necessary host directories (e.g., `/dev` for USB devices) and setting up network access.
    -   [ ] Launch the container with `docker run --runtime nvidia -it --network host ...`.

4.  **Run an Isaac ROS Perception Pipeline**:
    -   [ ] Inside the Docker container, pull and build an example Isaac ROS perception package (e.g., `isaac_ros_detectnet` or `isaac_ros_image_pipeline`).
    -   [ ] Modify the launch file of the example to:
        -   Start the `realsense_node` (if not running on the host).
        -   Launch the Isaac ROS perception node (e.g., `detectnet_node`).
    -   [ ] Run the combined launch file.

5.  **Visualize Output**:
    -   [ ] From a separate workstation (or the Jetson if configured for desktop use), launch RViz2.
    -   [ ] Verify that the Isaac ROS node is publishing its output (e.g., detected objects with bounding boxes, processed images).
    -   [ ] Configure RViz2 to display the processed camera images and any detected objects.

## Acceptance Criteria

-   The user can successfully set up a Jetson device with JetPack and Docker.
-   The user can connect and run a RealSense camera with its ROS 2 wrapper.
-   The user can deploy and run an Isaac ROS Docker container on the Jetson.
-   The user can launch an Isaac ROS perception pipeline and visualize its output in RViz2, demonstrating real-time AI inference on the edge.
