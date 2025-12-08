# Lab Outline: M4-C3 - Cognitive Task Planning

This document outlines the lab requirements for Module 4, Chapter 3, as required by Task 1.18.3.

## Lab Goal

The user will enhance their robot's voice control by integrating a Large Language Model (LLM) for cognitive task planning. The robot will translate high-level natural language commands into a sequence of executable ROS 2 actions using LLM function calling capabilities.

## Lab Requirements

1.  **Define Robot "Tools" (Functions)**:
    -   [ ] Expand the robot's capabilities to include a few more actions that can be triggered via ROS 2. Examples:
        -   `navigate_to_pose(x: float, y: float, theta: float)`: Uses Nav2 to move to a specific coordinate.
        -   `identify_object(object_name: str)`: Simulates an object detection and returns its perceived location (e.g., a simple print statement for this lab).
        -   `grasp_object(object_name: str)`: Simulates grasping an object at its current location.
    -   [ ] For each of these "tools," define a clear JSON schema for its parameters, following the LLM's function calling API specification (e.g., OpenAI or Gemini).

2.  **Upgrade the Orchestrator Node**:
    -   [ ] Modify the `simple_command_orchestrator.py` node (from M4-C2) to become an "LLM-powered orchestrator."
    -   [ ] It should still subscribe to `/voice/command` for transcribed text.
    -   [ ] When a command is received:
        -   It sends the user's command to the LLM, along with the descriptions of all available robot "tools."
        -   It instructs the LLM to choose and call the appropriate tool(s) to fulfill the request.
    -   [ ] The orchestrator node must then parse the LLM's function call output (JSON).
    -   [ ] Based on the parsed function calls, it should then trigger the corresponding ROS 2 actions (e.g., publish a Nav2 goal, call a custom ROS 2 service for `identify_object` or `grasp_object`).

3.  **Prompt Engineering for Robustness**:
    -   [ ] Experiment with different system prompts for the LLM to:
        -   Ensure it always uses the defined tools for robot control.
        -   Handle ambiguous commands (e.g., asking for clarification).
        -   Incorporate simple environmental context (e.g., "The robot is currently at [current_location]").

4.  **Full System Demo**:
    -   [ ] Launch the entire system:
        -   Robot (simulated in Isaac Sim with Nav2, or physical robot with Nav2).
        -   Audio capture and STT nodes.
        -   The new LLM-powered orchestrator node.
    -   [ ] Give high-level voice commands to the robot (e.g., "Robot, please navigate to the charging station," "Find the blue box and bring it to me").
    -   [ ] Observe the orchestrator node interacting with the LLM, and the robot executing the planned actions.

## Acceptance Criteria

-   The user can define robot capabilities as structured "tools" for an LLM.
-   The user can implement an orchestrator node that uses an LLM's function calling feature to generate robot action plans from natural language.
-   The user can integrate the voice input, STT, LLM planning, and robot execution into a single, functional system.
-   The robot can successfully perform multi-step tasks based on high-level voice commands, demonstrating cognitive task planning.
