# Module 4: Vision-Language-Action — Giving Your Robot a Mind

## Chapter 1: VLA Foundations — The LLM as a Robot Brain

Welcome to the final module. We've built a robot, given it senses, and taught it to navigate. Now, we're going to give it a mind. We will use a **Large Language Model (LLM)** as a high-level planner, enabling our robot to understand and execute complex, natural language commands.

This is the frontier of robotics, where we move from programming specific behaviors to simply telling the robot what we want it to do. This chapter will introduce you to the core concepts of **Vision-Language-Action (VLA)** systems and teach you how to use an LLM as a robot's reasoning engine.

### Core Concepts: LLMs for Robotics

LLMs are incredibly powerful tools for reasoning and planning. In robotics, we can leverage this power by treating the LLM as a "task planner" that translates human language into a sequence of robot actions.

-   **High-Level Task Planning**: An LLM can take a complex command like "bring me the red ball from the other room" and decompose it into a logical sequence of sub-goals:
    1.  Navigate to the other room.
    2.  Search for the red ball.
    3.  Once found, move towards it.
    4.  Grasp the red ball.
    5.  Navigate back to the user.
    6.  Release the red ball.

-   **Grounding**: This is the most critical concept. "Grounding" is the process of connecting the LLM's abstract textual world to the robot's physical world. The LLM might know what a "red ball" is conceptually, but it needs the robot's perception system to *find* the specific red ball in the room and the robot's control system to *grasp* it.

:::tip
Grounding is the central challenge in embodied AI. An LLM's abstract knowledge must be firmly connected to the robot's sensory inputs and motor outputs to enable meaningful interaction with the physical world.
:::


-   **Function Calling / Tool Use**: To achieve grounding, we use a technique called "function calling" or "tool use." We provide the LLM with a list of "tools" it can use, which are essentially the robot's available actions (e.g., `navigate_to(destination)`, `grasp_object(object_name)`). When given a command, the LLM's job is not to write a story, but to output a structured JSON object representing a call to one of its available tools. Our robot's code then parses this JSON and executes the corresponding real-world action.

### System Diagram

```ascii
+-----------------+      +-----------------+      +-----------------+
|  Human Command  |----->|       LLM       |----->|  Robot Action   |
| ("Get the       |      | (Task Planner)  |      |  (Executor)     |
|   blue cube")   |      +-----------------+      +-----------------+
+-----------------+              |                        ^
                                 | Chooses tool & args    | Executes
                                 v                        |
                         +-----------------------------+
                         | {"tool": "grasp_object",    |
                         |  "args": {"name": "blue_cube"}} |
                         +-----------------------------+
                                 (Structured JSON Output)
```

### System Diagram

```ascii
+-----------------+      +-----------------+      +-----------------+
|  Human Command  |----->|       LLM       |----->|  Robot Action   |
| ("Get the       |      | (Task Planner)  |      |  (Executor)     |
|   blue cube")   |      +-----------------+      +-----------------+
+-----------------+              |                        ^
                                 | Chooses tool & args    | Executes
                                 v                        |
                         +-----------------------------+
                         | {"tool": "grasp_object",    |
                         |  "args": {"name": "blue_cube"}} |
                         +-----------------------------+
                                 (Structured JSON Output)
```

---

## Lab: Using an LLM as a Robot Planner

In this lab, you won't write any robot code. Instead, you'll focus entirely on the "brain." You'll use the OpenAI API to send prompts to an LLM and engineer those prompts to make the LLM act as a robot planner.

### 1. LLM API Setup

-   Go to [platform.openai.com](https://platform.openai.com) and create an API key.
-   Install the OpenAI Python library: `pip install openai`.
-   Set your API key as an environment variable: `export OPENAI_API_KEY='your-key-here'`

### 2. Simple Robotics Prompting

Create a Python script (`planner.py`). We'll start by giving the LLM a role and a task.

```python
from openai import OpenAI
client = OpenAI()

# Define the robot's available actions (tools)
robot_actions = """
- navigate_to(location): moves the robot to a named location.
- find_object(object_name): looks for an object and returns its location.
- grasp_object(object_name): picks up a specified object.
- place_object(location): places the held object at a location.
"""

# The user's command
user_command = "Please find the apple on the table and bring it to me."

# Craft the prompt
system_prompt = f"""
You are a helpful robot assistant. Your job is to take a user's command
and break it down into a sequence of simple, numbered steps.
You can only use the following actions:
{robot_actions}
"""

response = client.chat.completions.create(
  model="gpt-4-turbo",
  messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_command}
  ]
)

print(response.choices[0].message.content)
```
Run the script. The LLM should output a numbered list of steps, like "1. navigate_to(table)", "2. find_object(apple)", etc.

### 3. Using Function Calling for Structured Output

A numbered list is good for humans, but hard for a program to parse. Let's use the "tool use" feature to get structured JSON output.

Modify your script:
```python
from openai import OpenAI
import json
client = OpenAI()

# Define the tools in the JSON format the API expects
tools = [
    {
        "type": "function",
        "function": {
            "name": "navigate_to",
            "description": "Moves the robot to a named location like 'table' or 'user'.",
            "parameters": { "type": "object", "properties": { "location": { "type": "string" } } }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "grasp_object",
            "description": "Picks up a specified object.",
            "parameters": { "type": "object", "properties": { "object_name": { "type": "string" } } }
        }
    }
]

# Send the request with the tools
response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[{"role": "user", "content": "Bring me the apple from the table."}],
    tools=tools,
    tool_choice="auto"
)

# The response will now contain structured 'tool_calls'
response_message = response.choices[0].message
tool_calls = response_message.tool_calls

if tool_calls:
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        print(f"Executing action: {function_name} with args: {function_args}")
        # In a real system, you would now call your actual robot function
        # e.g., if function_name == "navigate_to":
        #    my_robot.navigate_to(function_args.get("location"))
```
Run this script. Notice how the output is no longer a text sentence, but a structured "tool call" that your program can easily parse and execute.

### Verification

- [X] You have successfully used the OpenAI API to generate a text-based plan.
- [X] You have defined a robot's capabilities as structured "tools" for the LLM.
- [X] You have used the function calling/tool use feature to get a structured, machine-readable JSON output from the LLM.

You have now built the "brain" of your VLA system. The final step is to connect this brain to the robot's "body" (the ROS 2 actions) and its "ears" (the speech-to-text system).