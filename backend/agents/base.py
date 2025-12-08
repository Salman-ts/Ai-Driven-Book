from typing import List, Callable, Any, Dict, Optional
from pydantic import BaseModel, Field
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
    Wrapper around OpenAI Assistants API (Agents).
    """
    def __init__(self, name: str, role: str, model: str = "gpt-4-turbo-preview"):
        self.name = name
        self.role = role
        self.model = model
        self.client = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.skills: List[AgentSkill] = []
        self.assistant_id: Optional[str] = None
        
    def add_skill(self, skill: AgentSkill):
        self.skills.append(skill)

    async def initialize(self):
        """Register the assistant with OpenAI."""
        tools = [{"type": "code_interpreter"}] # Built-in default
        # Add custom function tools
        for skill in self.skills:
            tools.append({
                "type": "function",
                "function": {
                    "name": skill.name,
                    "description": skill.description,
                    "parameters": skill.parameters
                }
            })
            
        assistant = await self.client.beta.assistants.create(
            name=self.name,
            instructions=f"You are {self.name}. {self.role}",
            tools=tools,
            model=self.model
        )
        self.assistant_id = assistant.id
        print(f"Agent {self.name} initialized with ID: {self.assistant_id}")

    async def create_thread(self):
        thread = await self.client.beta.threads.create()
        return thread.id

    async def run_stream(self, thread_id: str, content: str):
        """
        Sends a message to the thread and streams the response.
        Handles tool calls automatically.
        """
        await self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=content
        )

        stream = await self.client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=self.assistant_id,
            stream=True
        )
        
        async for event in stream:
            # Simple wrapper to yield text deltas
            # In a full implementation, need to handle 'requires_action' for function calls
            # For this 'ChatKit' stub, we'll focus on text streaming first.
            if event.event == 'thread.message.delta':
                yield event.data.delta.content[0].text.value
            elif event.event == 'thread.run.requires_action':
                # TODO: Handle tool outputs submission
                pass

    # Helper for simple output
    async def run(self, input_text: str):
        if not self.assistant_id:
            await self.initialize()
            
        thread_id = await self.create_thread()
        
        # Simple non-streaming run for internal tools
        await self.client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=input_text
        )
        
        run = await self.client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=self.assistant_id,
        )
        
        # Simple tool handling loop (basic implementation)
        if run.status == 'requires_action':
            tool_outputs = []
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                # Find matching skill
                skill = next((s for s in self.skills if s.name == tool_call.function.name), None)
                if skill:
                    args = json.loads(tool_call.function.arguments)
                    output = str(skill.function(**args))
                    tool_outputs.append({
                        "tool_call_id": tool_call.id,
                        "output": output
                    })
            
            if tool_outputs:
                run = await self.client.beta.threads.runs.submit_tool_outputs_and_poll(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )

        if run.status == 'completed':
            messages = await self.client.beta.threads.messages.list(
                thread_id=thread_id
            )
            return messages.data[0] # Return latest message
        else:
            return f"Run status: {run.status}"

