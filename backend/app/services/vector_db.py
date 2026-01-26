from qdrant_client import QdrantClient
from app.core.config import settings

class VectorDBClient:
    _instance = None
    
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = QdrantClient(
                url=settings.QDRANT_URL,
                api_key=settings.QDRANT_API_KEY
            )
        return cls._instance

def get_qdrant_client():
    return VectorDBClient.get_instance()
