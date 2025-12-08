# Authoritative Sources for Isaac Sim Synthetic Data Generation

This document lists primary sources for understanding how to generate synthetic data with NVIDIA Isaac Sim, as required by Task 1.12.1.

## Primary Sources (NVIDIA Documentation)

1.  **Synthetic Data Generation Overview**: The main documentation page for Isaac Sim's synthetic data capabilities.
    -   URL: [https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation.html](https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation.html)

2.  **Sensors**: Details on configuring various sensors for synthetic data, including RGB-D cameras, LIDAR, and IMU.
    -   **Camera Sensor**: [https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/camera_sensor.html](https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/camera_sensor.html)
    -   **Lidar Sensor**: [https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/lidar_sensor.html](https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/lidar_sensor.html)

3.  **Writers**: Information on the different types of data writers available (e.g., for semantic segmentation, bounding boxes, depth).
    -   URL: [https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/writers.html](https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/writers.html)

4.  **Domain Randomization**: Explanation of how to use domain randomization techniques to improve the robustness of models trained on synthetic data.
    -   URL: [https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/domain_randomization.html](https://docs.omniverse.nvidia.com/isaacsim/latest/features/synthetic_data_generation/domain_randomization.html)

5.  **Replicator API**: The Python API that allows programmatic control over synthetic data generation, sensor configuration, and domain randomization.
    -   URL: [https://docs.omniverse.nvidia.com/isaacsim/latest/reference_api/isaac_sim_reference/synthetic_data_api.html](https://docs.omniverse.nvidia.com/isaacsim/latest/reference_api/isaac_sim_reference/synthetic_data_api.html)

## Secondary Sources (Tutorials and Examples)

1.  **Isaac Sim Tutorials - Synthetic Data**: Official tutorials demonstrating how to set up synthetic data generation.
    -   URL: [https://docs.omniverse.nvidia.com/isaacsim/latest/tutorials/data_generation/synthetic_data.html](https://docs.omniverse.nvidia.com/isaacsim/latest/tutorials/data_generation/synthetic_data.html)

2.  **Isaac Sim Samples (GitHub)**: Various examples demonstrating synthetic data workflows.
    -   URL: [https://github.com/NVIDIA-Omniverse/IsaacSim-Samples/tree/main/exts/omni.isaac.synthetic_data](https://github.com/NVIDIA-Omniverse/IsaacSim-Samples/tree/main/exts/omni.isaac.synthetic_data)
