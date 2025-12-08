from qdrant_client import QdrantClient, models
from openai import AsyncOpenAI
from app.core.config import settings
import uuid

class RAGService:
    def __init__(self):
        self.qdrant = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.openai = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
        self.collection_name = "ai_book_chunks"
        self.embedding_model = settings.EMBEDDING_MODEL
        self.vector_size = 3072 # Size for text-embedding-3-large

    def init_collection(self):
        # Check if collection exists
        if not self.qdrant.collection_exists(self.collection_name):
            self.qdrant.create_collection(
                collection_name=self.collection_name,
                vectors_config=models.VectorParams(
                    size=self.vector_size,
                    distance=models.Distance.COSINE
                )
            )
            print(f"Collection {self.collection_name} created.")

    async def get_embedding(self, text: str):
        response = await self.openai.embeddings.create(
            input=text,
            model=self.embedding_model
        )
        return response.data[0].embedding

    async def search(self, query: str, limit: int = 5):
        query_vector = await self.get_embedding(query)
        results = self.qdrant.search(
            collection_name=self.collection_name,
            query_vector=query_vector,
            limit=limit,
            with_payload=True
        )
        return results

    async def ingest_file(self, content: str, metadata: dict):
        # Simple chunking for now (can specific splitters later)
        # TODO: Implement robust chunking
        chunks = [content[i:i+8000] for i in range(0, len(content), 8000)]
        
        points = []
        for chunk in chunks:
            vector = await self.get_embedding(chunk)
            points.append(models.PointStruct(
                id=str(uuid.uuid4()),
                vector=vector,
                payload={ "content": chunk, **metadata }
            ))
        
        self.qdrant.upload_points(
            collection_name=self.collection_name,
            points=points
        )

rag_service = RAGService()
