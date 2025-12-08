import asyncio
import os
import sys
import asyncpg
from qdrant_client import QdrantClient

# Add parent dir
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.core.config import settings

async def verify_infrastructure():
    print("🔍 Starting Infrastructure Verification...\n")
    
    # 1. Verify Neon Postgres
    print(f"1. Testing Neon Postgres Connection...")
    try:
        conn = await asyncpg.connect(settings.NEON_DSN)
        version = await conn.fetchval("SELECT version()")
        print(f"   ✅ Connected to Postgres! Version: {version}")
        await conn.close()
    except Exception as e:
        print(f"   ❌ Postgres Connection Failed: {e}")

    # 2. Verify Qdrant Cloud
    print(f"\n2. Testing Qdrant Cloud Connection...")
    try:
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        collections = client.get_collections()
        print(f"   ✅ Connected to Qdrant! Found {len(collections.collections)} collections.")
    except Exception as e:
        print(f"   ❌ Qdrant Connection Failed: {e}")

    # 3. Verify OpenAI (Simple Model Check)
    # Optional, uncomment if you want to test API key
    # print(f"\n3. Testing OpenAI Connection...")
    # try:
    #     from openai import AsyncOpenAI
    #     ai = AsyncOpenAI(api_key=settings.OPENAI_API_KEY)
    #     await ai.models.list()
    #     print(f"   ✅ Connected to OpenAI!")
    # except Exception as e:
    #     print(f"   ❌ OpenAI Connection Failed: {e}")

    print("\n🏁 Verification Complete.")

if __name__ == "__main__":
    asyncio.run(verify_infrastructure())
