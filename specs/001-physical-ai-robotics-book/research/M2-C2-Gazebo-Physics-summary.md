# Summary of Gazebo Physics Concepts

This document synthesizes key concepts related to defining physics properties for robot models in Gazebo, as required by Task 1.7.2.

## Key Physics Properties

For a realistic simulation, Gazebo's physics engine needs to know the physical properties of each link (rigid body) in the model. These are typically defined within the link's description in a URDF or SDF file.

-   **Mass**: The amount of matter in the link. It determines how the link reacts to forces (inertia) and how it is affected by gravity.
    -   Defined in the `<mass value="..."/>` tag within the `<inertial>` element.

-   **Inertia Tensor**: A 3x3 matrix that describes how the mass is distributed within the link. It determines the link's resistance to rotational motion around different axes. An incorrect inertia tensor can lead to very unrealistic simulation behavior.
    -   Defined by the `<inertia ixx="..." ixy="..." .../>` tag within the `<inertial>` element.
    -   It's common to use modeling software (like Blender or SolidWorks) to automatically calculate the inertia tensor for complex shapes. For simple shapes (spheres, boxes), formulas can be used.

-   **Collision Geometry**: The shape used by the physics engine to calculate collisions. It is defined in the `<collision>` element and should be a simpler representation than the visual model to ensure fast and stable collision detection.

-   **Surface Properties**: These are defined within the `<surface>` tag of a `<collision>` element and control how two objects interact when they touch.
    -   **Friction**: The force that resists sliding motion between two surfaces. In Gazebo, this is often modeled using a pyramid friction model with two coefficients:
        -   `mu`: The primary coefficient of friction.
        -   `mu2`: The secondary coefficient of friction (for anisotropic friction).
    -   **Restitution**: The "bounciness" of a collision. A value of 0 means the objects don't bounce at all, while a value of 1 means they have a perfectly elastic collision.
    -   **Damping**: A force that opposes motion, used to simulate effects like air resistance. `linear` damping affects linear velocity, and `angular` damping affects angular velocity.

## Applying Properties: URDF vs. SDF

-   **SDF (Simulation Description Format)**: Gazebo's native format. All physics properties have corresponding tags directly in the SDF specification.

-   **URDF (Unified Robot Description Format)**: A more general format that is not specific to Gazebo. To add Gazebo-specific physics properties to a URDF, you must use a special `<gazebo>` tag.

    -   **Example**: To set the friction for a link in URDF, you would add a `<gazebo>` tag within that link's definition:
        ```xml
        <link name="my_link">
          ...
          <collision>...</collision>
          <visual>...</visual>
          <inertial>...</inertial>
        </link>

        <gazebo reference="my_link">
          <mu1>1.0</mu1>
          <mu2>1.0</mu2>
          <material>Gazebo/Orange</material>
        </gazebo>
        ```
    -   The `reference` attribute of the `<gazebo>` tag links it to the corresponding URDF link.
    -   This tag is also used to set materials (colors) for visualization in Gazebo and to specify sensor or controller plugins.
