import requests
import json

BASE_URL = "http://localhost:8001"
ADMIN_API_KEY = "cTRM3lVsw-Xya1HHeenKYdQQv7AZh8dH53mqFyNLW-k" # User provided key

def trigger_ingestion():
    url = f"{BASE_URL}/ingest"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {ADMIN_API_KEY}"
    }
    payload = {
        "source_dir": "../docs",
        "force_reindex": True
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(payload))
        print(f"Ingestion Trigger Response ({response.status_code}):")
        print(json.dumps(response.json(), indent=2))
    except requests.exceptions.ConnectionError:
        print(f"Error: Could not connect to the server at {BASE_URL}. Is the FastAPI backend running?")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    trigger_ingestion()
