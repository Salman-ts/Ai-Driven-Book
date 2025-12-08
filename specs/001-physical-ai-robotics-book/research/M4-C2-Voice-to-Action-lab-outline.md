# Lab Outline: M4-C2 - Voice-to-Action

This document outlines the lab requirements for Module 4, Chapter 2, as required by Task 1.17.3.

## Lab Goal

The user will learn to integrate Speech-to-Text (STT) into their ROS 2 robot system. They will create nodes for audio capture and STT processing on the Jetson, enabling the robot to receive and interpret spoken commands.

## Lab Requirements

1.  **Microphone Setup on Jetson**:
    -   [ ] Connect a USB microphone to the Jetson Orin Nano/NX.
    -   [ ] Verify microphone functionality using `arecord` or similar Linux audio tools.

2.  **Audio Input ROS 2 Node**:
    -   [ ] Create a new ROS 2 Python package (e.g., `robot_audio`).
    -   [ ] Inside this package, create a Python node (`audio_publisher_node.py`) that uses `sounddevice` or `PyAudio` to capture audio from the USB microphone.
    -   [ ] This node should publish raw audio data (e.g., as a custom `AudioData` message with `data` (bytes), `sample_rate`, `channels`) to a ROS 2 topic (e.g., `/audio/raw`).

3.  **STT Processing Node**:
    -   [ ] Create another Python node (`stt_node.py`) in the `robot_audio` package.
    -   [ ] This node should subscribe to the `/audio/raw` topic.
    -   [ ] Implement a local STT solution using OpenAI Whisper (or a similar lightweight model) on the Jetson. The audio chunks from the subscription will be fed to the Whisper model.
    -   [ ] The node should publish the transcribed text as a `std_msgs/String` message on a topic (e.g., `/voice/command`).

4.  **Simple Orchestrator Node**:
    -   [ ] Create a simple Python orchestrator node (`simple_command_orchestrator.py`) in the `robot_audio` package.
    -   [ ] This node subscribes to `/voice/command`.
    -   [ ] When a command is received, it should perform a simple lookup (e.g., if "move forward" is heard, publish a `Twist` message to move forward; if "stop" is heard, publish a stop command).
    -   [ ] For this lab, assume the robot has a pre-existing `/cmd_vel` topic that it can subscribe to.

5.  **Launch File Integration**:
    -   [ ] Create a launch file (`voice_control.launch.py`) to start all three nodes (`audio_publisher_node`, `stt_node`, `simple_command_orchestrator`).
    -   [ ] Ensure the `robot_audio` package is correctly built and its executables are installed via `setup.py`.

6.  **Test Voice Control**:
    -   [ ] Deploy the `robot_audio` package and its dependencies to the Jetson.
    -   [ ] Launch the system: `ros2 launch robot_audio voice_control.launch.py`.
    -   [ ] Speak commands into the microphone (e.g., "move forward", "stop").
    -   [ ] Verify that the `simple_command_orchestrator` logs the transcribed text and the robot (simulated or physical, if connected) responds to the commands.

## Acceptance Criteria

-   The user can successfully capture audio from a USB microphone on the Jetson and publish it as a ROS 2 topic.
-   The user can implement a local STT solution (e.g., Whisper) on the Jetson to transcribe spoken commands.
-   The user can create a simple orchestrator node that interprets transcribed text and triggers basic robot actions.
-   The user can launch the entire voice control pipeline and successfully control the robot using spoken commands.
