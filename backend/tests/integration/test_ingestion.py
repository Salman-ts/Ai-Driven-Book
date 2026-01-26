import pytest
from httpx import AsyncClient
from app.db.models import IngestionJob
from app.core.config import settings

@pytest.mark.asyncio
async def test_ingestion_flow_unauthorized(client: AsyncClient):
    """Ensure unauthorized users cannot trigger ingestion."""
    response = await client.post("/ingest", json={})
    assert response.status_code == 401

@pytest.mark.asyncio
async def test_ingestion_flow_admin_key(client: AsyncClient, db_session):
    """Test ingestion trigger with valid admin key."""
    # Mocking admin key check is tricky without overriding settings, 
    # but we can rely on dependency overrides in conftest if setup.
    # For now, we assume the test environment configures ADMIN_API_KEY.
    
    headers = {"Authorization": f"Bearer {settings.ADMIN_API_KEY}"} if settings.ADMIN_API_KEY else {}
    
    # We might need to mock the actual heavy ingestion service to avoid processing real files
    # but for integration test, hitting the endpoint and getting a Job ID is key.
    
    # Note: This test assumes /ingest endpoint exists (TDD)
    response = await client.post("/ingest", json={"force_reindex": True}, headers=headers)
    
    # Assert
    # If endpoint isn't implemented yet, this will be 404 (TDD red state)
    if response.status_code == 404:
        pytest.fail("Ingest endpoint not found (Expected 404 until implemented)")
        
    assert response.status_code == 202
    data = response.json()
    assert "job_id" in data
    assert data["status"] == "pending"
    
    # Verify DB
    job = await db_session.get(IngestionJob, data["job_id"])
    assert job is not None
    assert job.status == "pending"
