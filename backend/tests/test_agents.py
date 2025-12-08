import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
from backend.agents.base import ChatKitAgent, AgentSkill

# Mock Settings to avoid missing env var errors
@pytest.fixture(autouse=True)
def mock_settings():
    with patch("backend.agents.base.settings") as mock:
        mock.OPENAI_API_KEY = "sk-mock-key"
        yield mock

@pytest.fixture
def mock_openai_client():
    with patch("backend.agents.base.AsyncOpenAI") as mock_cls:
        mock_client = AsyncMock()
        mock_cls.return_value = mock_client
        
        # Mock Beta Assistants
        mock_client.beta.assistants.create = AsyncMock(return_value=MagicMock(id="asst_123"))
        mock_client.beta.threads.create = AsyncMock(return_value=MagicMock(id="thread_123"))
        mock_client.beta.threads.messages.create = AsyncMock()
        
        # Mock Run
        mock_run = MagicMock(id="run_123", status="completed")
        mock_client.beta.threads.runs.create_and_poll = AsyncMock(return_value=mock_run)
        
        # Mock Message List
        mock_msg = MagicMock()
        mock_msg.content = [MagicMock(text=MagicMock(value="Hello World"))]
        mock_client.beta.threads.messages.list = AsyncMock(return_value=MagicMock(data=[mock_msg]))
        
        yield mock_client

@pytest.mark.asyncio
async def test_agent_initialization(mock_openai_client):
    agent = ChatKitAgent(name="TestAgent", role="Tester")
    await agent.initialize()
    
    assert agent.assistant_id == "asst_123"
    mock_openai_client.beta.assistants.create.assert_called_once()

@pytest.mark.asyncio
async def test_agent_run_basic(mock_openai_client):
    agent = ChatKitAgent(name="TestAgent", role="Tester")
    agent.assistant_id = "asst_123" # Skip init
    
    response = await agent.run("Hello")
    
    assert response.content[0].text.value == "Hello World"
    mock_openai_client.beta.threads.create.assert_called_once()
    mock_openai_client.beta.threads.runs.create_and_poll.assert_called_with(
        thread_id="thread_123",
        assistant_id="asst_123"
    )

@pytest.mark.asyncio
async def test_agent_tool_execution(mock_openai_client):
    # Setup Tool
    mock_tool_func = MagicMock(return_value="Tool Result")
    skill = AgentSkill(name="test_tool", description="desc", function=mock_tool_func)
    
    agent = ChatKitAgent(name="ToolAgent", role="Worker")
    agent.add_skill(skill)
    agent.assistant_id = "asst_tool"
    
    # 1. Mock run returning requires_action
    mock_run_action = MagicMock(id="run_action", status="requires_action")
    mock_tool_call = MagicMock(id="call_123", function=MagicMock(name="test_tool", arguments='{}'))
    mock_run_action.required_action.submit_tool_outputs.tool_calls = [mock_tool_call]
    
    # 2. Mock run returning completed after submission
    mock_run_completed = MagicMock(id="run_action", status="completed")
    
    # Side effect: first call -> action, second call -> completed (not strictly needed for create_and_poll unless mocked carefully, 
    # but here we mock the polling result directly. 
    # For simplicity in this unit test, let's assume create_and_poll returns the action state first)
    
    mock_openai_client.beta.threads.runs.create_and_poll.return_value = mock_run_action
    
    # Mock submit_tool_outputs_and_poll to return completed
    mock_openai_client.beta.threads.runs.submit_tool_outputs_and_poll = AsyncMock(return_value=mock_run_completed)
    
    response = await agent.run("Use tool")
    
    # Assertions
    mock_tool_func.assert_called_once()
    mock_openai_client.beta.threads.runs.submit_tool_outputs_and_poll.assert_called_once()
    assert response.content[0].text.value == "Hello World"
