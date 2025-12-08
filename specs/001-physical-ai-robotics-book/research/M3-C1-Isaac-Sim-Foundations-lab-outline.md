# Lab Outline: M3-C1 - Isaac Sim Foundations

This document outlines the lab requirements for Module 3, Chapter 1, as required by Task 1.11.3.

## Lab Goal

The user will install NVIDIA Isaac Sim, become familiar with its user interface, and learn the basic workflow for importing a robot URDF, creating a scene, and running a simulation.

## Lab Requirements

1.  **Installation and Setup**:
    -   [ ] Install the NVIDIA Omniverse Launcher.
    -   [ ] From the Omniverse Launcher, install and launch the Isaac Sim application.
    -   [ ] Ensure the ROS 2 Humble bridge is enabled in the Isaac Sim extensions.

2.  **UI and Scene Navigation**:
    -   [ ] Follow a guided tour of the Isaac Sim UI, identifying key windows like the Stage (scene graph), Viewport (3D view), Property panel, and Content browser.
    -   [ ] Practice navigating the 3D viewport (pan, orbit, zoom).

3.  **Create a Basic Scene**:
    -   [ ] Create a new, empty scene.
    -   [ ] From the Content browser, add a "Ground Plane" to the stage.
    -   [ ] Add basic shapes (cubes, spheres) to the scene and practice moving, rotating, and scaling them.
    -   [ ] Add a "Distant Light" to illuminate the scene.

4.  **Import a Robot URDF**:
    -   [ ] Use the URDF Importer tool (Content -> Import -> URDF).
    -   [ ] Import the differential drive robot URDF created in the previous module.
    -   [ ] Configure the importer to fix the base link and create physics articulations for the joints.
    -   [ ] Verify that the robot appears in the scene, positioned on the ground plane.

5.  **Run the Simulation**:
    -   [ ] Press the "Play" button to start the physics simulation.
    -   [ ] Verify that the robot falls onto the ground plane and rests there realistically.
    -   [ ] Use the Python scripting interface to apply a simple force or torque to one of the robot's wheels and observe the effect.

## Acceptance Criteria

-   The user can successfully install and launch Isaac Sim via the Omniverse Launcher.
-   The user can navigate the Isaac Sim UI and create a basic scene with lights and objects.
-   The user can successfully import a URDF robot model and have it appear correctly in the scene.
-   The physics simulation runs correctly, and the imported robot interacts realistically with the environment.
