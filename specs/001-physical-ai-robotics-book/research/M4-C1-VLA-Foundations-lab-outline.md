# Lab Outline: M4-C1 - VLA Foundations

This document outlines the lab requirements for Module 4, Chapter 1, as required by Task 1.16.3.

## Lab Goal

The user will explore the foundational concepts of Vision-Language-Action (VLA) by interacting with a Large Language Model (LLM) and learning basic prompt engineering techniques for robotics.

## Lab Requirements

1.  **LLM API Setup**:
    -   [ ] Obtain an API key for a commercial LLM (e.g., OpenAI's GPT, Google's Gemini, Anthropic's Claude).
    -   [ ] Install the corresponding Python client library (e.g., `openai`, `google-generativeai`, `anthropic`).

2.  **Basic LLM Interaction ("Hello World")**:
    -   [ ] Write a simple Python script to send a basic text prompt to the LLM and print its response.
    -   [ ] Experiment with different simple prompts to understand the LLM's general capabilities (e.g., "Tell me a joke," "Summarize AI in one paragraph").

3.  **Robotics Prompting Exercise - Simple Task Planning**:
    -   [ ] Assume a simple robot with a limited set of actions (e.g., `move_forward()`, `turn_left()`, `pick_up(object_name)`, `drop_off(location)`).
    -   [ ] Craft a prompt that instructs the LLM to act as a "robot planner."
    -   [ ] Provide the LLM with a scenario (e.g., "The robot is in a room with a red ball and a blue box. Pick up the red ball and place it in the blue box.")
    -   [ ] Provide the LLM with the available robot functions and instruct it to output a sequence of function calls to achieve the goal.
    -   [ ] Analyze the LLM's output. Does it correctly decompose the task? Is the output in a parseable format?

4.  **Prompt Engineering for Output Format**:
    -   [ ] Refine the prompt to explicitly instruct the LLM to output its plan in a structured format, such as a JSON list of actions.
    -   [ ] For example, a response like:
        ```json
        [
          {"action": "move_to", "target": "red_ball"},
          {"action": "pick_up", "object": "red_ball"},
          {"action": "move_to", "target": "blue_box"},
          {"action": "drop_off", "location": "blue_box"}
        ]
        ```
    -   [ ] Parse the LLM's structured output in Python.

## Acceptance Criteria

-   The user can successfully set up access to an LLM API.
-   The user can send simple text prompts to an LLM and receive responses.
-   The user can design a prompt that guides the LLM to generate a sequence of robot actions for a given task.
-   The user can refine their prompt to ensure the LLM outputs its plan in a structured, machine-readable format (e.g., JSON) and parse that output.
