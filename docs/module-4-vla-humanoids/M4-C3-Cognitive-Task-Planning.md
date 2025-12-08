## Chapter 3: Cognitive Task Planning — The Capstone Project

This is the final chapter, where everything comes together. We have built a robot, given it senses, taught it to navigate, and given it ears. Now, we will connect all these pieces to the LLM brain we developed, creating a fully-realized, voice-controlled robot capable of understanding and executing high-level commands.

This chapter will guide you through the creation of the final orchestrator node that bridges the gap between language, perception, and action.

### Core Concepts: The Full VLA Pipeline

The complete Vision-Language-Action pipeline is a testament to the power of modular, message-based architecture.

1.  **Voice Input**: The `audio_publisher_node` captures raw audio from a microphone.
2.  **Speech-to-Text**: The `stt_node` uses Whisper to convert the audio into a text command.
3.  **LLM Task Planning**: The central `orchestrator_node` takes the text command, sends it to an LLM (like GPT-4) along with a list of the robot's available "tools" (functions).
4.  **Structured Action**: The LLM returns a structured JSON object representing a function call—its plan for executing the command.
5.  **Action Execution**: The `orchestrator_node` parses the JSON and calls the appropriate ROS 2 service or action server to make the robot perform the action (e.g., calls Nav2 to navigate, calls a custom service to grasp an object).

:::tip
The orchestrator node is the heart of your VLA system. It acts as the intelligent agent that translates high-level human intent into concrete robot actions, effectively bridging the cognitive gap.
:::

6.  **Feedback (Future Work)**: In more advanced systems, the result of the action (e.g., "Grasp successful," or "Navigation failed") would be fed back to the LLM for the next step of planning or for error recovery.

### System Diagram: The Final Assembly

```ascii
+-------------+      +----------------+      +------------------+
| Microphone  |----->| Audio Node     |----->|   STT Node       |
+-------------+      +----------------+      +------------------+
                                                   |
                                                   | Publishes /voice/command
                                                   v
+-----------------------------+             +------------------+
|       LLM API               |<----------->| Orchestrator Node|
| (e.g., OpenAI)              |   (Sends      +------------------+
+-----------------------------+    prompt,         |
                                  gets plan)       | Calls Actions
                                                   v
+-----------------------------+      +------------------+
| Nav2 Action Server          |<-----| Grasping Service |
+-----------------------------+      +------------------+
```

### System Diagram: The Final Assembly

```ascii
+-------------+      +----------------+      +------------------+
| Microphone  |----->| Audio Node     |----->|   STT Node       |
+-------------+      +----------------+      +------------------+
                                                   |
                                                   | Publishes /voice/command
                                                   v
+-----------------------------+             +------------------+
|       LLM API               |<----------->| Orchestrator Node|
| (e.g., OpenAI)              |   (Sends      +------------------+
+-----------------------------+    prompt,         |
                                  gets plan)       | Calls Actions
                                                   v
+-----------------------------+      +------------------+
| Nav2 Action Server          |<-----| Grasping Service |
+-----------------------------+      +------------------+
```

---

## Lab: The Final Capstone — A Voice-Controlled Robot

In this lab, you will write the final orchestrator node that connects your voice pipeline to your LLM planner and your robot's navigation system.

### 1. Define Your Robot's "Tools"

First, we need to formally define the actions our robot can take in a way the LLM can understand. In a new `robot_tools.py` file, define the JSON schema for your robot's function calls.

```python
# robot_tools.py
tools = [
    {
        "type": "function",
        "function": {
            "name": "navigate_to_pose",
            "description": "Moves the robot to a specific 2D pose (x, y, theta) in the map frame.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {"type": "number", "description": "The x-coordinate."},
                    "y": {"type": "number", "description": "The y-coordinate."},
                    "theta": {"type": "number", "description": "The orientation angle in radians."}
                },
                "required": ["x", "y", "theta"]
            }
        }
    },
    # Add other tools here, like grasp_object, etc.
]
```

### 2. Create the LLM-Powered Orchestrator

Create the final node, `orchestrator_node.py`, in your `robot_voice_control` package. This node will be complex, so we'll break it down.

```python
import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from std_msgs.msg import String
from nav2_msgs.action import NavigateToPose
from openai import OpenAI
import json
from .robot_tools import tools # Import your tools definition

class OrchestratorNode(Node):
    def __init__(self):
        super().__init__('orchestrator_node')
        self.client = OpenAI()
        self.nav2_action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')

        self.subscription = self.create_subscription(
            String,
            '/voice/command',
            self.voice_command_callback,
            10)
        self.get_logger().info("Orchestrator is ready.")

    def voice_command_callback(self, msg):
        self.get_logger().info(f'Received voice command: "{msg.data}"')
        
        # 1. Send command to LLM
        response = self.client.chat.completions.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": msg.data}],
            tools=tools,
            tool_choice="auto"
        )
        response_message = response.choices[0].message
        tool_calls = response_message.tool_calls

        if not tool_calls:
            self.get_logger().info("LLM did not request a tool.")
            return

        # 2. Parse and Execute Tool Calls
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)
            
            self.get_logger().info(f"LLM requests to call: {function_name} with args: {function_args}")

            if function_name == "navigate_to_pose":
                self.execute_navigation(function_args)

    def execute_navigation(self, args):
        self.get_logger().info("Executing navigation...")
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = float(args.get("x"))
        goal_msg.pose.pose.position.y = float(args.get("y"))
        goal_msg.pose.pose.orientation.w = 1.0 # Simple orientation for now

        self.nav2_action_client.wait_for_server()
        self.nav2_action_client.send_goal_async(goal_msg)
        self.get_logger().info("Navigation goal sent.")

def main(args=None):
    rclpy.init(args=args)
    orchestrator_node = OrchestratorNode()
    rclpy.spin(orchestrator_node)
    orchestrator_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

### 3. Launch the Full System

Create a final top-level launch file that starts:
-   Your Isaac Sim simulation with the Nav2-enabled robot.
-   The full Nav2 stack (loading your pre-made map).
-   Your `audio_publisher_node`.
-   Your `stt_node`.
-   Your new `orchestrator_node`.

### Verification

- [X] Launch the complete system.
- [X] Speak a command into the microphone, for example: "Robot, please go to position x equals one, y equals two."
- [X] Watch the terminals. You should see:
    1.  The `stt_node` transcribe your speech.
    2.  The `orchestrator_node` receive the text, log that it's calling the LLM, and then log that it's executing the `navigate_to_pose` function.
    3.  The robot in Isaac Sim should begin moving to the specified coordinates.

You have successfully built a complete Vision-Language-Action pipeline. You have integrated a microphone, a local speech-to-text model, a cloud-based Large Language Model for planning, and a ROS 2 navigation stack to create an intelligent, voice-controlled robot. This is the capstone of your journey and a template for building the next generation of robotic applications.