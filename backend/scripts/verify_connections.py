import cohere
from app.core.config import settings
import sys

def verify_cohere():
    print(f"Testing Cohere Connection...")
    print(f"API Key: {settings.COHERE_API_KEY[:5]}... (Length: {len(settings.COHERE_API_KEY)})")
    
    try:
        client = cohere.ClientV2(api_key=settings.COHERE_API_KEY)
        
        # Simple generation test
        response = client.chat(
            model="command-r-plus-08-2024",
            messages=[{"role": "user", "content": "Say hello!"}]
        )
        print(f"Success! Response: {response.message.content[0].text}")
        return True
    except Exception as e:
        print(f"Cohere Error: {e}")
        return False

def verify_qdrant():
    print(f"\nTesting Qdrant Connection...")
    from qdrant_client import QdrantClient
    try:
        client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        collections = client.get_collections()
        print(f"Success! Collections: {[c.name for c in collections.collections]}")
        return True
    except Exception as e:
        print(f"Qdrant Error: {e}")
        return False

if __name__ == "__main__":
    c_ok = verify_cohere()
    q_ok = verify_qdrant()
    
    if c_ok and q_ok:
        print("\nAll systems GO.")
        sys.exit(0)
    else:
        print("\nConnection verification FAILED.")
        sys.exit(1)