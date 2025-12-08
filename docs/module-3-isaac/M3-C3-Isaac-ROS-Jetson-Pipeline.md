## Chapter 3: The Isaac ROS Jetson Pipeline — AI on the Edge

So far, our AI training and simulation has been on a powerful desktop PC. But robots in the real world are mobile and need to run their "brains" on small, power-efficient embedded systems. This is the world of **edge computing**, and NVIDIA's platform for AI at the edge is **Jetson**.

This chapter will teach you how to set up an NVIDIA Jetson device and deploy a hardware-accelerated perception pipeline using **Isaac ROS**, NVIDIA's collection of high-performance ROS 2 packages.

### Core Concepts: The Edge AI Stack

-   **NVIDIA Jetson**: A family of small, powerful computers that bring the NVIDIA GPU architecture to embedded systems. The Jetson Orin series is capable of running modern AI models in real-time, making it perfect for robotics.
-   **JetPack SDK**: The software stack for Jetson, including the Ubuntu OS, CUDA libraries, and **TensorRT**.
-   **TensorRT**: NVIDIA's SDK for high-performance deep learning inference. It takes a trained model and optimizes it for a specific NVIDIA GPU, dramatically increasing speed and efficiency.
-   **Isaac ROS**: A collection of ROS 2 packages specifically designed and optimized for the Jetson platform. These packages handle common, computationally-heavy perception tasks.
-   **NITROS (NVIDIA Isaac ROS Optimized)**: The secret sauce behind Isaac ROS. NITROS uses techniques like zero-copy data transfer to avoid unnecessary memory copies between the CPU and GPU, and leverages hardware-accelerated components (like TensorRT and other parts of the Jetson system) to process data directly on the GPU. This results in massive performance gains for perception pipelines.

:::tip
NITROS is a fundamental innovation that enables real-time AI perception on edge devices. Understanding its role in data transfer and hardware acceleration is key to developing high-performance ROS 2 applications on Jetson.
:::


### System Diagram

```ascii
+--------------------+      +---------------------------+      +---------------------+
| RealSense Camera   |----->|   isaac_ros_image_proc    |----->| isaac_ros_detectnet |
| (Publishes Raw Img)|      | (Rectifies & Converts Img)|      | (Runs AI Model)     |
+--------------------+      +---------------------------+      +---------------------+
                                       (NITROS-accelerated)             |
                                                                        | Publishes Detections
                                                                        v
                                                                  [ /detections ] (Topic)
                                                                        |
                                                                        v
                                                                +----------------+
                                                                |     RViz2      |
                                                                +----------------+
```

### System Diagram

```ascii
+--------------------+      +---------------------------+      +---------------------+
| RealSense Camera   |----->|   isaac_ros_image_proc    |----->| isaac_ros_detectnet |
| (Publishes Raw Img)|      | (Rectifies & Converts Img)|      | (Runs AI Model)     |
+--------------------+      +---------------------------+      +---------------------+
                                       (NITROS-accelerated)             |
                                                                        | Publishes Detections
                                                                        v
                                                                  [ /detections ] (Topic)
                                                                        |
                                                                        v
                                                                +----------------+
                                                                |     RViz2      |
                                                                +----------------+
```

---

## Lab: Running an Accelerated Perception Pipeline on Jetson

In this lab, you'll set up your Jetson device, connect a camera, and run a pre-built Isaac ROS package for object detection, visualizing the results in RViz2.

### 1. Jetson Device Setup

-   Follow the official NVIDIA guide to flash your Jetson Orin Nano/NX Developer Kit with the latest **JetPack SDK**. This will install Ubuntu and all necessary NVIDIA drivers and libraries.
-   On the Jetson, install Docker and the NVIDIA Container Toolkit. This is the recommended way to run Isaac ROS.

### 2. Connect Camera and Deploy Isaac ROS

-   Connect an Intel RealSense depth camera to the Jetson's USB port.
-   On the Jetson, pull the Isaac ROS Docker image for object detection from the NVIDIA NGC registry:
    ```bash
    docker pull nvcr.io/nvidia/isaac-ros/isaac-ros-detectnet:humble
    ```
-   Run the container, making sure to pass through the camera devices and enable host networking:
    ```bash
    docker run --runtime nvidia -it --network host -v /dev:/dev nvcr.io/nvidia/isaac-ros/isaac-ros-detectnet:humble
    ```

### 3. Run the Isaac ROS Launch File

Inside the Docker container, Isaac ROS provides pre-built launch files that are ready to run.

-   Launch the RealSense camera node:
    ```bash
    ros2 launch realsense2_camera rs_launch.py
    ```
-   In a second terminal within the container, launch the `detectnet` pipeline. This will start the Isaac ROS nodes that are optimized to run a pre-trained object detection model.
    ```bash
    ros2 launch isaac_ros_detectnet isaac_ros_detectnet.launch.py
    ```

### 4. Visualize the Output

-   On your desktop computer (which must be on the same network as the Jetson), launch RViz2.
-   Add an `Image` display and subscribe to the `/image_rect` topic to see the camera feed.
-   Add a `MarkerArray` display and subscribe to the `/detections` topic.

### Verification

- [X] In RViz2, you should see the live camera feed from the Jetson's RealSense camera.
- [X] When you point the camera at objects the pre-trained model recognizes (like people, keyboards, etc.), you should see bounding boxes and labels appear overlaid on the image in RViz2.
- [X] You are now running a complete, hardware-accelerated AI perception pipeline on an embedded device, a cornerstone of modern robotics.

This workflow—developing and training in a powerful simulator like Isaac Sim, then deploying the resulting AI model to a power-efficient edge device like Jetson—is the future of intelligent robotics.