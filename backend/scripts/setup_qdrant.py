import asyncio
import os
import sys
from qdrant_client import QdrantClient, models

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings

async def setup_qdrant():
    print(f"Connecting to Qdrant at {settings.QDRANT_URL}...")
    
    client = QdrantClient(
        url=settings.QDRANT_URL,
        api_key=settings.QDRANT_API_KEY
    )
    
    collection_name = "ai_book_chunks"
    vector_size = 3072 # text-embedding-3-large
    
    # Check if exists
    if client.collection_exists(collection_name):
        print(f"Collection '{collection_name}' already exists.")
        # Optional: client.delete_collection(collection_name) to reset
        return

    print(f"Creating collection '{collection_name}'...")
    
    # Production Optimized Configuration
    client.create_collection(
        collection_name=collection_name,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE
        ),
        # HNSW Index Configuration for Speed/Accuracy Tradeoff
        optimizers_config=models.OptimizersConfigDiff(
            default_segment_number=2,
            memmap_threshold=20000
        ),
        # Quantization for memory efficiency (optional, good for large datasets)
        quantization_config=models.ScalarQuantization(
            scalar=models.ScalarQuantizationConfig(
                type=models.ScalarType.INT8,
                quantile=0.99,
                always_ram=True
            )
        )
    )
    
    # Create Payload Indexes for Metadata Filtering
    print("Creating metadata indexes...")
    client.create_payload_index(collection_name, "chapter", models.PayloadSchemaType.KEYWORD)
    client.create_payload_index(collection_name, "section", models.PayloadSchemaType.KEYWORD)
    client.create_payload_index(collection_name, "tags", models.PayloadSchemaType.KEYWORD)
    
    print("✅ Qdrant Collection Setup Complete!")

if __name__ == "__main__":
    asyncio.run(setup_qdrant())
