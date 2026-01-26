## Chapter 2: Synthetic Data & Sensors in Isaac Sim

The single most powerful feature of Isaac Sim is its ability to generate vast quantities of high-quality, perfectly-labeled **Synthetic Data**. This data is the fuel for training the AI models that give our robots intelligence.

This chapter will teach you how to add a high-fidelity camera to your robot in Isaac Sim, configure it to capture different types of data (like depth and segmentation masks), and use **Domain Randomization** to ensure the data is robust enough for sim-to-real transfer.

### Core Concepts: Fueling Your AI

-   **Synthetic Data**: Artificially generated data that mimics real-world data. In robotics, it's a game-changer because it's cheap, scalable, and comes with perfect ground-truth labels (e.g., you know exactly where every pixel of a "coffee cup" is in an image).
-   **Replicator**: The powerful API within Isaac Sim that allows you to programmatically define and run synthetic data generation pipelines.
-   **Data Writers**: Replicator components that save the generated data to disk in a specific format. You can have writers for RGB images, depth maps, semantic segmentation, instance segmentation, bounding boxes, and more.
-   **Domain Randomization (DR)**: The key technique for bridging the sim-to-real gap. Instead of trying to make one perfect simulation, we create thousands of slightly different ones by randomizing properties like lighting, textures, object positions, and camera angles. This forces the AI model to learn the essential features of the objects it needs to recognize, rather than just memorizing the simulation.

:::note
Domain Randomization is a critical technique for training AI models robust enough to transfer from simulation to the real world. By introducing variability in simulation, the model becomes less sensitive to specific simulation details and generalizes better to real-world conditions.
:::


### System Diagram

```ascii
+-----------------------------+
|    Isaac Sim Python Script  |
+-----------------------------+
    |           |           |
    | Controls  | Triggers  | Randomizes
    v           v           v
+-----------------------------+
|      Isaac Sim Engine       |
|  (Physics, Rendering, etc.) |
+-----------------------------+
    |
    | Generates...
    v
+-----------------------------+      +-----------------------------+
|    Raw Sensor Data          |----->|      Replicator Writers     |
| (RGB, Depth, Segmentation)  |      +-----------------------------+
+-----------------------------+                    |
                                                   v
                                          +-----------------+
                                          | Labeled Dataset |
                                          | (Images & JSON) |
                                          +-----------------+
```

---

## Lab: Generating a Labeled Dataset

In this lab, you'll use a Python script to control Isaac Sim, capture a dataset of images with ground-truth labels, and apply domain randomization.

### 1. Add a Camera to Your Robot

-   Load the scene with your differential drive robot from the previous chapter.
-   In the `Stage` panel, right-click on your robot's `base_link`, go to `Create -> Camera`.
-   Position the new camera so it has a clear forward-facing view.

### 2. Create the Python Script

Isaac Sim's primary interface is Python scripting. Create a new Python script (`generate_data.py`) outside of your ROS workspace for now. This script will use the `omni.isaac.core` and `omni.replicator` APIs.

```python
from omni.isaac.kit import SimulationApp

# --- Simulation setup ---
simulation_app = SimulationApp({"headless": False})
import omni.replicator.core as rep
from omni.isaac.core import World
from omni.isaac.core.objects import cuboid

# --- Create a new world and add objects ---
world = World()
# Add a few cubes for the robot to see
cuboid.Cuboid(prim_path="/World/Cube_01", position=[1.0, 0, 0.1], scale=[0.2, 0.2, 0.2], color=[0,0,1])
cuboid.Cuboid(prim_path="/World/Cube_02", position=[1.0, 0.5, 0.1], scale=[0.2, 0.2, 0.2], color=[1,0,0])
world.scene.add_default_ground_plane()

# --- Find the camera and define the output path ---
camera = rep.get.prims(path_pattern="/World/my_robot/base_link/Camera")
output_dir = "/path/to/your/output_folder"

# --- Create and attach writers ---
rep.WriterRegistry.register(rep.BasicWriter)
writer = rep.BasicWriter(output_dir=output_dir, 
                         data_types=["rgb", "bounding_box_2d_tight", "semantic_segmentation"])

# --- Setup randomization ---
with rep.trigger.on_frame():
    with rep.randomizer.lighting(num_lights=rep.distribution.uniform(1, 3)):
        rep.modify.light(intensity=rep.distribution.uniform(500, 2000), 
                         color=rep.distribution.uniform((0.1,0.1,0.1), (1,1,1)))
    with rep.get.prims(path_pattern="/World/Cube*") as cubes:
        rep.modify.semantics(cubes, "class", "cube") # Add semantic label
        rep.modify.pose(cubes, position=rep.distribution.uniform((-1, -1, 0.1), (1, 1, 0.1)))

# --- Run the simulation and capture data ---
rep.orchestrator.run()
for i in range(100):
    world.step()
rep.orchestrator.stop()
simulation_app.close()
```

### 3. Run the Script

You run Isaac Sim scripts using the provided Python executable.
```bash
./python.sh /path/to/your/generate_data.py
```
This will launch Isaac Sim, run your script, and then close automatically.

### Verification

- [X] Isaac Sim should launch, and you should see the cubes and robot appear.
- [X] The lighting and cube positions should change on each frame.
- [X] In your specified output folder, you should find subdirectories for `rgb`, `bounding_box_2d_tight`, and `semantic_segmentation`.
- [X] The folders should contain 100 images and corresponding JSON files with the label data.

You have just created a high-quality, perfectly labeled dataset for training a perception AI, a task that would have taken days or weeks to do manually.