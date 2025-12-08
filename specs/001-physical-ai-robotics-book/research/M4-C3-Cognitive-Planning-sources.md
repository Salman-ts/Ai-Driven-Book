# Authoritative Sources for LLM as a Planner and Function Calling

This document lists primary sources for understanding how Large Language Models (LLMs) can be used for task planning and function calling in robotics, as required by Task 1.18.1.

## Primary Sources (Research Papers and API Documentation)

1.  **OpenAI Function Calling / Tool Use**: The official documentation from OpenAI on how to use their models to generate structured JSON output that can be used to call functions or tools. This is a foundational concept.
    -   URL: [https://platform.openai.com/docs/guides/function-calling](https://platform.openai.com/docs/guides/function-calling)

2.  **Google Gemini Function Calling / Tool Use**: Similar functionality offered by Google's Gemini models.
    -   URL: [https://ai.google.dev/docs/function_calling](https://ai.google.dev/docs/function_calling)

3.  **"Toolformer: Language Models Can Teach Themselves to Use Tools"**: A research paper demonstrating how LLMs can learn to use external tools through self-supervised learning. This underpins the idea of function calling.
    -   URL: [https://arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761)

4.  **"LLMs are General-Purpose Interfaces"**: A paper arguing that LLMs can serve as a universal interface for various tasks, including planning.
    -   URL: [https://arxiv.org/abs/2206.02677](https://arxiv.org/abs/2206.02677)

5.  **"Inner Monologue: Empowering LLMs as Active Robot Reasoners"**: (Re-iterated from M4-C1, as it's highly relevant here) This work explores how LLMs can reason about tasks and interact with their environment by chaining together actions and self-reflecting.
    -   URL: [https://innermonologue.github.io/](https://innermonologue.github.io/)
    -   Paper: [https://arxiv.org/abs/2307.05141](https://arxiv.org/abs/2307.05141)

## Secondary Sources (Frameworks and Tutorials)

1.  **LangChain Agents & Tools**: LangChain provides a robust framework for building LLM-powered agents that can use tools.
    -   URL: [https://python.langchain.com/docs/modules/agents/tools/](https://python.langchain.com/docs/modules/agents/tools/)

2.  **LlamaIndex Tools & Agents**: Similar to LangChain, LlamaIndex also offers abstractions for tool use with LLMs.
    -   URL: [https://docs.llamaindex.ai/en/stable/module_guides/tool_use/overview.html](https://docs.llamaindex.ai/en/stable/module_guides/tool_use/overview.html)
