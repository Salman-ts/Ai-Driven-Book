import pytest
from httpx import AsyncClient

@pytest.mark.asyncio
async def test_global_query_flow(client: AsyncClient):
    """Test standard global RAG query."""
    payload = {
        "query": "What is an agent?",
        "selection_only": False
    }
    
    # Note: This test assumes /query endpoint exists (TDD)
    response = await client.post("/query", json=payload)
    
    if response.status_code == 404:
        pytest.fail("Query endpoint not found (Expected 404 until implemented)")
        
    assert response.status_code == 200
    data = response.json()
    
    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["sources"], list)
    assert "provenance" in data
    assert data["provenance"]["mode"] == "global"

@pytest.mark.asyncio
async def test_selection_only_query_flow(client: AsyncClient):
    """Test selection-only RAG query."""
    payload = {
        "query": "What is an agent?",
        "selection_context": "An agent is an autonomous entity that perceives its environment through sensors and acts upon that environment using actuators.",
        "selection_only": True
    }
    
    response = await client.post("/query", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    
    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["sources"], list)
    assert "provenance" in data
    assert data["provenance"]["mode"] == "selection"
    assert "agent" in data["answer"].lower() or "autonomous entity" in data["answer"].lower() # Basic check for answer relevance

@pytest.mark.asyncio
async def test_selection_only_insufficient_evidence(client: AsyncClient):
    """Test selection-only query with insufficient context."""
    payload = {
        "query": "What is the capital of France?",
        "selection_context": "The quick brown fox jumps over the lazy dog.",
        "selection_only": True
    }
    
    response = await client.post("/query", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "i cannot answer this based on the provided" in data["answer"].lower()

@pytest.mark.asyncio
async def test_query_validation(client: AsyncClient):
    """Test query validation (empty query)."""
    response = await client.post("/query", json={"query": ""})
    assert response.status_code == 422
