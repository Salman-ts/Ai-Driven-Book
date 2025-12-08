# Authoritative Sources for Speech-to-Text (STT) and Audio Capture

This document lists primary sources for understanding Speech-to-Text (STT) technologies and audio capture methods relevant to ROS 2 robotics, as required by Task 1.17.1.

## Primary Sources (Official Documentation and Research)

1.  **OpenAI Whisper**: A highly accurate general-purpose speech recognition model. It's often the go-to for local STT on capable hardware.
    -   **GitHub Repository**: [https://github.com/openai/whisper](https://github.com/openai/whisper)
    -   **Paper**: [https://arxiv.org/abs/2212.04356](https://arxiv.org/abs/2212.04356)

2.  **`sounddevice` Python Library**: A cross-platform Python library for playing and recording audio. It's built on PortAudio.
    -   **Documentation**: [https://python-sounddevice.readthedocs.io/en/latest/](https://python-sounddevice.readthedocs.io/en/latest/)
    -   **GitHub**: [https://github.com/spatialaudio/python-sounddevice](https://github.com/spatialaudio/python-sounddevice)

3.  **ROS 2 Audio Nodes**: While not an official `ros-audio` package, there are community packages and tutorials for integrating audio.
    -   **`audio_common` (ROS 1, but concepts transfer)**: The ROS 1 package often used as inspiration for ROS 2 audio.
        -   URL: [http://wiki.ros.org/audio_common](http://wiki.ros.org/audio_common)
    -   **Community ROS 2 Audio Packages/Examples**: Search on GitHub for `ros2 audio` or `ros2 microphone` for current implementations. For instance, packages that wrap `pyaudio` or `sounddevice`.

4.  **`PyAudio` Python Library**: Another popular Python library for cross-platform audio input/output.
    -   **Documentation**: [https://pyaudio.readthedocs.io/en/latest/](https://pyaudio.readthedocs.io/en/latest/)

## Secondary Sources (Tutorials and Blogs)

1.  **Real-Time Speech Recognition with Whisper**: Blog posts or tutorials demonstrating how to integrate Whisper for real-time applications.
    -   Search: "realtime whisper python" or "whisper microphone python"

2.  **ROS 2 Microphone Input**: Tutorials on setting up a microphone and publishing audio data as a ROS 2 topic.
    -   Search: "ros2 microphone input tutorial"
