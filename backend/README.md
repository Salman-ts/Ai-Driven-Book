# AI Book Backend - RAG Chatbot

This document provides instructions for setting up and running the backend services for the AI Book RAG Chatbot.

## 1. Prerequisites

-   **Python 3.11+** (Ensure you have this version installed)
-   **Poetry** (Recommended for dependency management, install via `pip install poetry`) or **pip**
-   **Qdrant Cloud Account** (You will need your Qdrant URL and API Key)
-   **Cohere API Key**
-   **Neon Serverless Postgres** (You will need your Database URL/DSN)
-   **Git**

## 2. Setup Environment Variables

Create a `.env` file in the root of this backend directory. Copy the contents of `env_example` and fill in your actual credentials:

```ini
# .env example
# --- Basic App Settings ---
PROJECT_NAME="AI Book Backend"
API_V1_STR="/api/v1"

# --- Database ---
NEON_DSN="postgresql://user:password@your-neon-host.neon.tech/your-db?sslmode=require"

# --- Qdrant Vector Database ---
QDRANT_URL="https://your-qdrant-url.qdrant.tech"
QDRANT_API_KEY="your_qdrant_api_key"

# --- AI Model Providers ---
GEMINI_API_KEY="your_gemini_api_key" # Existing Gemini key
COHERE_API_KEY="your_cohere_api_key"

# --- Admin Authentication (for /ingest, /admin/reindex) ---
ADMIN_API_KEY="your_secure_admin_api_key" # Use a strong, unique key for admin operations

# --- OpenAI (Deprecated or Optional now) ---
OPENAI_API_KEY="" 
EMBEDDING_MODEL="text-embedding-004" # Still referenced for old services
```
**Important**: Do NOT commit your `.env` file to version control.

## 3. Installation

### Using Poetry (Recommended)

1.  Navigate to the backend directory:
    ```bash
    cd path/to/your/backend
    ```
2.  Install dependencies:
    ```bash
    poetry install
    ```
3.  Activate the virtual environment:
    ```bash
    poetry shell
    ```

### Using pip

1.  Navigate to the backend directory:
    ```bash
    cd path/to/your/backend
    ```
2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    # Ensure all new RAG dependencies are installed:
    # pip install cohere markdown-it-py python-frontmatter slowapi beautifulsoup4
    ```
3.  (Optional but Recommended) Create and activate a virtual environment first:
    ```bash
    python -m venv venv
    .\venv\Scripts\activate # On Windows
    source venv/bin/activate # On Linux/macOS
    ```

## 4. Run Migrations (for Neon Postgres)

The `app/db/models.py` defines the SQL schema. You'll need to run migrations to create these tables in your Neon Postgres database. (A dedicated migration tool like Alembic would be used in production, but for local setup, you might manually create tables or use a simple script.)

**Note**: For this project, you would typically use a tool like Alembic for proper migrations. For initial setup, ensure your database user has privileges to create tables.

## 5. Start the FastAPI Application

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
The `--reload` flag is useful for development as it restarts the server on code changes.

The API will be accessible at `http://localhost:8000`.

## 6. Basic Usage - RAG Chatbot

Once the server is running and your environment variables are set up:

### 6.1. Initialize Qdrant Collection (via Lifecycle Hook)

The Qdrant collection for storing document chunks (`ai_book_chunks_cohere`) will be automatically created on application startup if it doesn't exist.

### 6.2. Ingest Content (Admin Protected)

To ingest Docusaurus Markdown files (e.g., from your `docs/` folder), you need an Admin API Key (or a JWT for an admin user).

```bash
curl -X POST "http://localhost:8000/ingest" \
     -H "Content-Type: application/json" \
     -H "Authorization: Bearer YOUR_ADMIN_API_KEY" \
     -d 
           "source_dir": "path/to/your/docusaurus/docs", 
           "force_reindex": false
         }"
```
Replace `YOUR_ADMIN_API_KEY` with the value from your `.env` file and `path/to/your/docusaurus/docs` with the actual path to your Markdown content.

### 6.3. Query the Chatbot

**Global Search:**
```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d 
           "query": "What is an Agentic Workflow?"
         }"
```

**Selected-Text Only Query:**
```bash
curl -X POST "http://localhost:8000/query" \
     -H "Content-Type: application/json" \
     -d 
           "query": "Explain this paragraph.",
           "selection_context": "Agents can plan their actions, perceive their environment, and act autonomously to achieve goals.",
           "selection_only": true
         }"
```

## 7. Running Tests

```bash
pytest
```
To run specific tests:
```bash
pytest tests/integration/test_ingestion.py
pytest tests/unit/test_provenance.py
```

## 8. API Documentation

Access the interactive API documentation (Swagger UI) at `http://localhost:8000/docs`.

---

This `README.md` should help you get started with the backend.
