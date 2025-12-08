# Summary of LLM Planning and Tool Use Concepts

This document synthesizes key concepts for using Large Language Models (LLMs) as task planners in robotics, particularly through "function calling" or "tool use," as required by Task 1.18.2.

## LLMs as Task Planners

Traditionally, robot task planning has relied on symbolic AI methods (e.g., PDDL) or reinforcement learning. LLMs offer a new paradigm by leveraging their vast learned knowledge to generate plans from natural language instructions.

The core idea is to treat the LLM as a high-level planner that can:
1.  **Interpret High-Level Goals**: Understand human instructions (e.g., "clean the room," "make coffee").
2.  **Decompose into Sub-Goals**: Break down the complex goal into a sequence of smaller, more manageable steps.
3.  **Select Appropriate Tools/Actions**: Choose the right robot capabilities ("tools" or "functions") to achieve each sub-goal.
4.  **Order Actions Logically**: Arrange the selected actions in a correct and safe sequence.
5.  **Generate Parameters**: Infer the necessary parameters for each action (e.g., `move_to(table)`, `grasp(cup)`).

## Function Calling / Tool Use

"Function Calling" (or "Tool Use") is a specific technique that allows LLMs to interact with external systems or APIs. Instead of just generating human-readable text, the LLM can generate structured calls to predefined functions that the robot can then execute.

### The Process

1.  **Define Robot "Tools"**: The robot's capabilities are described to the LLM in a structured format (e.g., JSON schema). Each "tool" corresponds to an action the robot can perform, along with its parameters and their descriptions.
    -   Example Tool:
        ```json
        {
          "name": "move_robot_to",
          "description": "Moves the robot to a specified named location.",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "The name of the location to move to (e.g., 'kitchen', 'charging_station')."
              }
            },
            "required": ["location"]
          }
        }
        ```

2.  **Prompt the LLM**: The user's natural language command, along with the descriptions of the available tools, is sent to the LLM. The prompt instructs the LLM to choose the appropriate tool(s) and their parameters to fulfill the request.

3.  **LLM Generates Tool Calls**: If the LLM determines that a tool can achieve the user's intent, it will generate a structured JSON object representing a call to that tool.
    -   Example LLM Output for "Go to the kitchen":
        ```json
        {
          "tool_calls": [
            {
              "function": {
                "name": "move_robot_to",
                "arguments": {
                  "location": "kitchen"
                }
              }
            }
          ]
        }
        ```

4.  **Execute Tool Calls**: The robot's "orchestrator" or "agent" code parses this JSON output and then executes the corresponding robot action (e.g., calls the `move_robot_to("kitchen")` function, which might internally trigger a Nav2 goal).

5.  **Observe and Iterate (Optional)**: The result of the action (success/failure, sensor feedback) can be fed back to the LLM as part of a multi-turn conversation, allowing for more complex reasoning, error recovery, or plan refinement.

### Benefits for Robotics

-   **Natural Language Interface**: Humans can command robots using intuitive language.
-   **Flexibility**: The LLM can dynamically adapt its plan based on the input and available tools.
-   **Abstract Reasoning**: The LLM handles the high-level logic, freeing the robot developer from coding complex state machines for every task.
-   **Modularity**: Robot capabilities (tools) can be developed and updated independently of the LLM.

### Challenges

-   **Grounding**: Ensuring the LLM's abstract plan maps correctly and safely to the physical world.
-   **Prompt Engineering**: Crafting effective prompts to elicit desired behavior and output.
-   **Robustness**: Handling ambiguous commands, unexpected situations, and LLM "hallucinations."
-   **Latency**: The time taken for LLM inference can impact real-time performance.
