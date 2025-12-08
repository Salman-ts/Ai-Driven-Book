# Authoritative Sources for Gazebo Physics Properties

This document lists primary sources for understanding physics properties in the Gazebo simulator, as required by Task 1.7.1.

## Primary Sources (Gazebo and SDF Documentation)

1.  **SDF `physics` Tag**: The Simulation Description Format (SDF) is the native format for Gazebo worlds. The `<physics>` tag within an SDF file defines the global physics engine properties.
    -   URL: [http://sdformat.org/spec?ver=1.7&elem=physics](http://sdformat.org/spec?ver=1.7&elem=physics)

2.  **SDF `<link>` Tag**: The `<link>` element in SDF is where the physical properties of a single body are defined. This is analogous to the URDF `<link>` tag but with more Gazebo-specific options.
    -   URL: [http://sdformat.org/spec?ver=1.7&elem=link](http://sdformat.org/spec?ver=1.7&elem=link)

3.  **SDF `<inertial>` Tag**: Defines the mass and inertia tensor of a link.
    -   URL: [http://sdformat.org/spec?ver=1.7&elem=inertial](http://sdformat.org/spec?ver=1.7&elem=inertial)

4.  **SDF `<collision>` Tag**: Defines the collision geometry of a link. This element contains a `<surface>` tag where properties like friction and restitution are set.
    -   URL: [http://sdformat.org/spec?ver=1.7&elem=collision](http://sdformat.org/spec?ver=1.7&elem=collision)
    -   URL: [http://sdformat.org/spec?ver=1.7&elem=surface](http://sdformat.org/spec?ver=1.7&elem=surface)

5.  **Adding Physics Properties Tutorial**: A Gazebo Classic tutorial showing how to add mass and inertia to a model. The principles are directly applicable to modern Gazebo.
    -   URL: [https://classic.gazebosim.org/tutorials?tut=physics_params](https://classic.gazebosim.org/tutorials?tut=physics_params)

6.  **The `<gazebo>` tag for URDF**: When using a URDF file with Gazebo, a special `<gazebo>` tag can be added to specify Gazebo-specific properties that are not part of the standard URDF specification. This is the primary way to set physics materials and other properties when not using SDF directly.
    -   URL: [http://wiki.ros.org/urdf/XML/gazebo](http://wiki.ros.org/urdf/XML/gazebo)

## Secondary Sources

1.  **Gazebo Tutorials - Friction**: A tutorial explaining how to set friction properties for objects in Gazebo.
    -   URL: [https://classic.gazebosim.org/tutorials?tut=friction](https://classic.gazebosim.org/tutorials?tut=friction)
