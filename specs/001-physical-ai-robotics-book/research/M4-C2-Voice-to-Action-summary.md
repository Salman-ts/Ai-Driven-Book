# Summary of STT and Audio Integration Concepts

This document synthesizes concepts for integrating Speech-to-Text (STT) and audio capture into a ROS 2 robot, as required by Task 1.17.2.

## Speech-to-Text (STT)

Speech-to-Text (STT) technology converts spoken language into written text. For robotics, this is the first step in enabling voice commands.

-   **Model Choice**:
    -   **Cloud-based STT**: Services like Google Cloud Speech-to-Text, Azure Speech Services, or OpenAI's Whisper API. These generally offer high accuracy and handle various languages/accents well, but require an internet connection and incur costs.
    -   **On-device STT**: Models like OpenAI Whisper can also run locally on edge devices (like the Jetson). This provides low-latency, privacy-preserving transcription without internet dependency, though it requires more computational resources on the device.

-   **Real-time vs. Batch**: For voice commands, real-time or near real-time STT is essential. The audio stream needs to be captured, processed in chunks, and transcribed continuously.

## Audio Capture in Python

Python libraries like `sounddevice` or `PyAudio` provide interfaces to access microphone input.

-   **`sounddevice`**:
    -   Allows direct control over audio streams (sample rate, buffer size, number of channels).
    -   Can be configured to run a callback function when new audio data is available, enabling real-time processing.
    -   Requires `PortAudio` development libraries to be installed on the system.

## Integrating into ROS 2

To make audio and STT a part of the ROS 2 ecosystem, the typical approach involves creating custom ROS 2 nodes:

1.  **Audio Input Node**:
    -   **Purpose**: Captures audio from the microphone and publishes it as a ROS 2 topic.
    -   **Implementation**: A Python `rclpy` node that uses `sounddevice` or `PyAudio` to record audio. The raw audio data can be published as a custom ROS 2 message (e.g., a byte array with metadata like sample rate) or potentially a `sensor_msgs/Image` (if treated as a 1D signal) or a custom audio message type.
    -   **Key Considerations**: Handling buffer sizes, sample rates, and converting raw audio to a suitable ROS message format.

2.  **STT Processing Node**:
    -   **Purpose**: Subscribes to the raw audio topic, performs STT, and publishes the transcribed text.
    -   **Implementation**: A Python `rclpy` node.
        -   If using a cloud STT service: It sends audio chunks to the cloud API and publishes the resulting text.
        -   If using an on-device STT model (e.g., local Whisper): It loads the model, processes the audio chunks, and publishes the text.
    -   **Output**: Typically publishes a `std_msgs/String` message containing the transcribed text on a topic like `/speech_to_text`.

3.  **Orchestrator Node**:
    -   **Purpose**: Acts as the central intelligence that takes the transcribed text, interprets it, and triggers appropriate robot actions.
    -   **Implementation**: A Python `rclpy` node that subscribes to the `/speech_to_text` topic. It will contain logic to:
        -   Filter or normalize commands.
        -   Map commands to robot capabilities (e.g., "move forward" -> call a `move_forward()` service).
        -   In the context of VLA, this node will be responsible for feeding the transcribed text to the LLM and then executing the LLM's planned actions.

This modular approach allows for flexibility in choosing STT models, microphone hardware, and command interpretation logic.
