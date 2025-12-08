# Lab Outline: M3-C2 - Synthetic Data & Sensors

This document outlines the lab requirements for Module 3, Chapter 2, as required by Task 1.12.3.

## Lab Goal

The user will learn to add a high-fidelity camera sensor to their robot model in Isaac Sim, configure it for synthetic data generation, and implement basic domain randomization to create varied training data.

## Lab Requirements

1.  **Add a Camera Sensor to the Robot**:
    -   [ ] Load the robot model from the previous lab in Isaac Sim.
    -   [ ] Using the UI or Python scripting, add a camera sensor to a link on the robot (e.g., `base_link` or a new `camera_link`).
    -   [ ] Configure the camera's intrinsic parameters (resolution, focal length).

2.  **Configure Synthetic Data Generation**:
    -   [ ] Enable the necessary extensions for synthetic data (e.g., `omni.isaac.synthetic_data`).
    -   [ ] Using Python scripting, set up a data capture pipeline for the camera.
    -   [ ] Configure it to output:
        -   RGB images (`_rgb`)
        -   Depth maps (`_depth`)
        -   Semantic segmentation images (`_sem_segmentation`)
        -   2D Bounding Boxes (`_bounding_box_2d_tight`)
    -   [ ] Specify an output directory for the captured data.

3.  **Implement Basic Domain Randomization**:
    -   [ ] Introduce variability into the scene using the Domain Randomization (DR) API.
    -   [ ] Randomize the light source properties (e.g., color, intensity, position) at each simulation step or data capture event.
    -   [ ] Randomize the texture/color of objects in the scene (e.g., the ground plane, obstacle cubes).

4.  **Create a Scenario and Collect Data**:
    -   [ ] Place several simple primitive shapes (cubes, spheres) in the scene to act as objects for the robot to perceive.
    -   [ ] Write a Python script to:
        -   Initialize Isaac Sim.
        -   Load the robot and scene.
        -   Start the simulation.
        -   Loop for a specified number of frames, applying domain randomization and capturing data from the camera sensor at each step.
        -   Move the robot (e.g., rotate it or drive it randomly) during data collection to generate diverse views of the objects.

5.  **Verify Captured Data**:
    -   [ ] Inspect the output directory.
    -   [ ] Open some of the generated RGB images, depth maps, semantic segmentation, and bounding box JSON files to confirm that the data is being captured correctly and that the randomization is evident.

## Acceptance Criteria

-   The user can add and configure a camera sensor in Isaac Sim.
-   The user can set up a synthetic data pipeline to capture RGB, depth, semantic segmentation, and bounding box data.
-   The user can implement basic domain randomization to vary lighting and object textures.
-   The user can collect a dataset of synthetic images and verify the quality and diversity of the generated data.
