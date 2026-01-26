from typing import List, Callable, Any, Dict, Optional
from pydantic import BaseModel
from openai import AsyncOpenAI
from app.core.config import settings
import json
import asyncio

class AgentSkill(BaseModel):
    name: str
    description: str
    function: Callable[..., Any]
    parameters: Dict[str, Any] = {"type": "object", "properties": {}, "required": []}

class ChatKitAgent:
    """
    Wrapper around OpenAI SDK targeting Google Gemini API.
    """
    def __init__(self, name: str, role: str, model: str = "gemini-1.5-flash"):
        self.name = name
        self.role = role
        self.model = model
        # Configure OpenAI client for Gemini
        self.client = AsyncOpenAI(
            api_key=settings.GEMINI_API_KEY,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        self.skills: List[AgentSkill] = []
        self.history = []
        
    def add_skill(self, skill: AgentSkill):
        self.skills.append(skill)

    async def initialize(self):
        # No explicit init needed for stateless REST API, but keeping for interface compat
        print(f"Agent {self.name} initialized with model: {self.model} via OpenAI SDK")

    def _get_tools(self):
        tools = []
        for skill in self.skills:
            tools.append({
                "type": "function",
                "function": {
                    "name": skill.name,
                    "description": skill.description,
                    "parameters": skill.parameters
                }
            })
        return tools if tools else None

    async def run_stream(self, content: str):
        """
        Sends a message and streams the response.
        """
        messages = [{"role": "system", "content": f"You are {self.name}. {self.role}"}]
        messages.extend(self.history)
        messages.append({"role": "user", "content": content})
        
        # Tools configuration
        tools = self._get_tools()
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools,
            stream=True
        )
        
        async for chunk in response:
            if chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    async def run(self, input_text: str) -> str:
        """
        Non-streaming run with automatic tool calling loop.
        """
        messages = [{"role": "system", "content": f"You are {self.name}. {self.role}"}]
        messages.extend(self.history)
        messages.append({"role": "user", "content": input_text})
        
        tools = self._get_tools()
        
        response = await self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=tools
        )
        
        response_msg = response.choices[0].message
        
        # Check for tool calls
        if response_msg.tool_calls:
            # Append assistant message with tool calls
            messages.append(response_msg)
            
            for tool_call in response_msg.tool_calls:
                # Find matching skill
                skill = next((s for s in self.skills if s.name == tool_call.function.name), None)
                if skill:
                    args = json.loads(tool_call.function.arguments)
                    function_response = str(skill.function(**args))
                    
                    messages.append({
                        "tool_call_id": tool_call.id,
                        "role": "tool",
                        "name": tool_call.function.name,
                        "content": function_response,
                    })
            
            # Follow up request to get final answer
            second_response = await self.client.chat.completions.create(
                model=self.model,
                messages=messages
            )
            final_content = second_response.choices[0].message.content
            self.history.append({"role": "user", "content": input_text})
            self.history.append({"role": "assistant", "content": final_content})
            return final_content
        else:
            content = response_msg.content
            self.history.append({"role": "user", "content": input_text})
            self.history.append({"role": "assistant", "content": content})
            return content
