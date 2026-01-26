import pytest
from app.services.rag import rag_service, SemanticChunker
from app.services.auth import verify_jwt
from app.core.config import settings

@pytest.mark.asyncio
async def test_semantic_chunking():
    chunker = SemanticChunker(chunk_size=100)
    text = "## Header 1\nContent under header 1.\n## Header 2\nContent under header 2."
    chunks = chunker.chunk(text, {"source": "test"})
    
    assert len(chunks) >= 2
    assert "Header 1" in chunks[0]['content']
    assert "Header 2" in chunks[1]['content']

@pytest.mark.asyncio
async def test_rag_embedding_mock(mocker):
    # Mock Cohere client
    mock_response = mocker.Mock()
    mock_response.embeddings = mocker.Mock()
    mock_response.embeddings.float = [[0.1] * 1024]  # Cohere embed-english-v3.0 = 1024 dims
    mocker.patch.object(rag_service.client, 'embed', return_value=mock_response)
    
    emb = await rag_service.get_embedding("test")
    assert len(emb) == 1024

@pytest.mark.asyncio
async def test_auth_jwt_validation(mocker):
    # This requires a valid token or mocking jwt.decode
    mocker.patch('jose.jwt.decode', return_value={"sub": "user123", "exp": 9999999999})
    payload = await verify_jwt("valid-token")
    assert payload["sub"] == "user123"
