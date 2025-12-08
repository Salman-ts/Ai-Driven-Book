## Chapter 2: Voice-to-Action — The Robot's Ears

To create a true voice-controlled robot, we need to build the "ears" of the system. This involves capturing audio from a microphone, converting that audio into text using a **Speech-to-Text (STT)** model, and publishing the resulting text into our ROS 2 system for the LLM brain to process.

This chapter will teach you how to build a ROS 2 pipeline on your Jetson device to handle real-time voice input.

### Core Concepts: The Voice Pipeline

1.  **Audio Capture**: This is the first step. We need a ROS 2 node that can listen to a microphone connected to our robot's computer (the Jetson). This node's only job is to capture raw audio data and publish it onto a ROS 2 topic. Libraries like `sounddevice` in Python are perfect for this.

2.  **Speech-to-Text (STT)**: This is the core of the voice pipeline. We'll use a powerful, open-source model called **OpenAI Whisper**. Whisper can run locally on the Jetson, allowing for fast, private, and offline-capable voice recognition. A dedicated STT node will subscribe to the raw audio topic, feed the audio to the Whisper model, and publish the transcribed text on a new topic.

:::note
OpenAI Whisper is an exceptionally versatile and accurate STT model. Its ability to run locally on edge devices like the Jetson is a significant advantage for robotics applications, ensuring low latency and privacy.
:::


3.  **Orchestrator**: The central node that connects the "ears" to the "brain." It subscribes to the transcribed text, sends it to the LLM planner from the previous chapter, receives the structured action plan, and then executes the robot's actions.

### System Diagram

```ascii
+-------------+      +------------------+      +-----------------+      +------------------+
| Microphone  |----->| Audio Input Node |----->|  STT Node       |----->| Orchestrator Node|
+-------------+      +------------------+      +-----------------+      +------------------+
                        | Publishes Raw    |      | (Whisper)       |      | (Sends to LLM)   |
                        | Audio            |      | Publishes Text  |      +------------------+
                        v                  v      v                 v              |
                    [ /audio/raw ]     [ /voice/command ]     (Calls robot actions)
```

### System Diagram

```ascii
+-------------+      +------------------+      +-----------------+      +------------------+
| Microphone  |----->| Audio Input Node |----->|  STT Node       |----->| Orchestrator Node|
+-------------+      +------------------+      +-----------------+      +------------------+
                        | Publishes Raw    |      | (Whisper)       |      | (Sends to LLM)   |
                        | Audio            |      | Publishes Text  |      +------------------+
                        v                  v      v                 v              |
                    [ /audio/raw ]     [ /voice/command ]     (Calls robot actions)
```

---

## Lab: Building the Voice-to-Action Pipeline

In this lab, you'll create the ROS 2 nodes necessary to capture, transcribe, and process voice commands on your Jetson device.

### 1. Microphone Setup on Jetson

-   Plug a standard USB microphone into your Jetson Orin Nano/NX.
-   Verify that the OS detects it using a command-line tool like `arecord -l`.

### 2. The Audio Input Node

Create a new ROS 2 package `robot_voice_control`. Inside, create an `audio_publisher_node.py`:
```python
import rclpy
from rclpy.node import Node
import sounddevice as sd
from std_msgs.msg import Int16MultiArray # A simple way to send audio chunks

class AudioPublisher(Node):
    def __init__(self):
        super().__init__('audio_publisher')
        self.publisher_ = self.create_publisher(Int16MultiArray, 'audio/raw', 10)
        self.samplerate = 16000
        self.blocksize = 1600 # 100ms chunks
        self.stream = sd.InputStream(callback=self.audio_callback,
                                     samplerate=self.samplerate,
                                     channels=1,
                                     blocksize=self.blocksize,
                                     dtype='int16')
        self.stream.start()

    def audio_callback(self, indata, frames, time, status):
        msg = Int16MultiArray()
        msg.data = indata.flatten().tolist()
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    audio_publisher = AudioPublisher()
    rclpy.spin(audio_publisher)
    audio_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 3. The STT Node (Whisper)

On your Jetson, you'll need to install Whisper: `pip install openai-whisper`. Now, create the `stt_node.py`:
```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String, Int16MultiArray
import whisper
import numpy as np

class SttNode(Node):
    def __init__(self):
        super().__init__('stt_node')
        self.model = whisper.load_model("tiny.en") # Use the tiny English model for performance
        self.subscription = self.create_subscription(
            Int16MultiArray,
            'audio/raw',
            self.listener_callback,
            10)
        self.publisher_ = self.create_publisher(String, 'voice/command', 10)
        self.audio_buffer = np.array([], dtype=np.int16)

    def listener_callback(self, msg):
        self.audio_buffer = np.append(self.audio_buffer, np.array(msg.data, dtype=np.int16))
        # Process every ~2 seconds of audio
        if len(self.audio_buffer) >= 16000 * 2:
            audio_float = self.audio_buffer.astype(np.float32) / 32768.0
            result = self.model.transcribe(audio_float)
            text = result["text"].strip()
            if text: # Only publish if there's text
                self.get_logger().info(f'Transcribed: "{text}"')
                text_msg = String()
                text_msg.data = text
                self.publisher_.publish(text_msg)
            self.audio_buffer = np.array([], dtype=np.int16) # Clear buffer

def main(args=None):
    rclpy.init(args=args)
    stt_node = SttNode()
    rclpy.spin(stt_node)
    stt_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 4. Create a Launch File

Create a launch file that starts both nodes. Remember to add the nodes to your `setup.py` `entry_points`.

### 5. Build and Test

-   Build your `robot_voice_control` package and source the workspace.
-   Launch your new launch file.
-   In a separate terminal, echo the `/voice/command` topic: `ros2 topic echo /voice/command`.

### Verification

- [X] When you speak into the microphone, you should see the `stt_node` log the transcribed text.
- [X] The transcribed text should appear in the terminal where you are echoing the `/voice/command` topic.
- [X] You have successfully created the "ears" for your robot, turning spoken words into a stream of text data within your ROS 2 system.

Now all the pieces are in place. In the final chapter, we will connect this voice pipeline to the LLM brain to achieve our ultimate goal: a fully voice-controlled, intelligent robot.