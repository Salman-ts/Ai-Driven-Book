# Quickstart: Integrated RAG Chatbot

## Prerequisites

- **Python 3.11+**
- **Qdrant Cloud Account** (API Key + URL)
- **Cohere API Key**
- **Neon Postgres DSN**

## Environment Setup

Add these to your `.env` file:

```bash
COHERE_API_KEY=your_key_here
QDRANT_URL=https://xyz.qdrant.tech
QDRANT_API_KEY=your_qdrant_key
NEON_DSN=postgresql://user:pass@host/db
ADMIN_API_KEY=secret_for_local_testing_or_set_jwt
```

## Running the RAG Service

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Start the server**:
    ```bash
    uvicorn main:app --reload
    ```

3.  **Ingest Content** (Admin only):
    ```bash
    curl -X POST http://localhost:8000/ingest \
      -H "Authorization: Bearer <ADMIN_TOKEN>" \
      -H "Content-Type: application/json" \
      -d '{}'
    ```

## Testing the Query Endpoint

**Global Search**:
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Define agentic workflow"
  }'
```

**Selection-Only**:
```bash
curl -X POST http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{
    "query": "Explain this",
    "selection_context": "Agents can plan...",
    "selection_only": true
  }'
```

