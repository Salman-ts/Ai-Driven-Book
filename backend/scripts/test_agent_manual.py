import requests
import json

BASE_URL = "http://localhost:8001"  # Assuming running on 8001 as suggested

def test_health():
    try:
        response = requests.get(f"{BASE_URL}/chat/health")
        print(f"Health Check: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"Health Check Failed: {e}")

def test_query():
    print("\nTesting Query Endpoint...")
    payload = {
        "query": "What is an agentic workflow?"
    }
    try:
        # Note: /chat/message is the streaming endpoint the frontend uses
        # /query is the new structured endpoint we added
        
        # Test 1: The Chat Endpoint (Frontend use case)
        print("1. Testing /chat/message (Streamed)...")
        with requests.post(f"{BASE_URL}/chat/message", json=payload, stream=True) as r:
            if r.status_code == 200:
                print("Response stream content:")
                for chunk in r.iter_content(chunk_size=None):
                    if chunk:
                        print(chunk.decode('utf-8'), end='', flush=True)
                print("\n[End of Stream]")
            else:
                print(f"Error: {r.status_code} - {r.text}")

        # Test 2: The Structured Query Endpoint (Internal/Admin use case)
        print("\n2. Testing /query (Structured)...")
        r = requests.post(f"{BASE_URL}/query", json=payload)
        if r.status_code == 200:
            print(json.dumps(r.json(), indent=2))
        else:
            print(f"Error: {r.status_code} - {r.text}")

    except Exception as e:
        print(f"Query Test Failed: {e}")

if __name__ == "__main__":
    test_health()
    test_query()