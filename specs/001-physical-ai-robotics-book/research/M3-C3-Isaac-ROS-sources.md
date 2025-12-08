# Authoritative Sources for Isaac ROS and Jetson Setup

This document lists primary sources for understanding NVIDIA Isaac ROS, the Jetson platform, and their setup for robotic perception pipelines, as required by Task 1.13.1.

## Primary Sources (NVIDIA Documentation)

1.  **Isaac ROS Overview**: The main landing page for Isaac ROS, providing an overview of its benefits and available modules.
    -   URL: [https://developer.nvidia.com/isaac-ros](https://developer.nvidia.com/isaac-ros)

2.  **Isaac ROS Documentation**: The official and most comprehensive source for Isaac ROS, including installation guides, tutorials, and module descriptions.
    -   **Getting Started**: [https://nvidia-isaac-ros.github.io/getting_started/index.html](https://nvidia-isaac-ros.github.io/getting_started/index.html)
    -   **Supported Platforms (Jetson)**: Details on compatible Jetson devices and JetPack versions.
        -   URL: [https://nvidia-isaac-ros.github.io/getting_started/requirements.html](https://nvidia-isaac-ros.github.io/getting_started/requirements.html)
    -   **Deployment with Docker**: Explains how to deploy Isaac ROS containers, which is the recommended method.
        -   URL: [https://nvidia-isaac-ros.github.io/getting_started/deployment/deployment.html](https://nvidia-isaac-ros.github.io/getting_started/deployment/deployment.html)

3.  **NVIDIA Jetson Developer Kit Documentation**: Resources for setting up and developing on Jetson devices.
    -   **JetPack SDK**: The full development software stack for Jetson.
        -   URL: [https://developer.nvidia.com/embedded/jetpack](https://developer.nvidia.com/embedded/jetpack)
    -   **Getting Started with Jetson Orin Nano Developer Kit**:
        -   URL: [https://developer.nvidia.com/embedded/learn/getting-started-jetson-orin-nano-devkit](https://developer.nvidia.com/embedded/learn/getting-started-jetson-orin-nano-devkit)

4.  **NITROS (NVIDIA Isaac ROS Optimized)**: The core technology that accelerates ROS 2 message processing on NVIDIA hardware.
    -   URL: [https://nvidia-isaac-ros.github.io/concepts/nitros.html](https://nvidia-isaac-ros.github.io/concepts/nitros.html)

5.  **TensorRT**: NVIDIA's SDK for high-performance deep learning inference. Isaac ROS leverages TensorRT.
    -   URL: [https://developer.nvidia.com/tensorrt](https://developer.nvidia.com/tensorrt)

## Secondary Sources (Community and Tutorials)

1.  **RealSense ROS 2 Wrapper**: If using a RealSense camera, the official ROS 2 wrapper is essential.
    -   URL: [https://github.com/IntelRealSense/realsense-ros](https://github.com/IntelRealSense/realsense-ros)
