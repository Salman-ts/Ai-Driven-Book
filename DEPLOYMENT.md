# AI Book Deployment Guide

## 1. Backend Service (FastAPI)
Deployed on **Railway** or **Render**.

### Environment Variables
```bash
NEON_DSN=postgres://user:pass@host/db
QDRANT_URL=https://cluster.qdrant.io
QDRANT_API_KEY=...
GEMINI_API_KEY=...
BETTER_AUTH_SECRET=...
```

### Build Command
```bash
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 2. Frontend (Docusaurus)
Deployed on **Vercel**.

### Build Command
```bash
npm install
npm run build
```

## 3. Database (Neon Postgres)
- Ensure extensions `uuid-ossp` and `vector` (if using pgvector, otherwise Qdrant handles vectors) are enabled.
- Run `schema.sql` to initialize tables.

## 4. Better-Auth
- Run the Better-Auth Node.js server (separate repo) or use the Python adapter if available.
- Sync `BETTER_AUTH_SECRET` across services.
