# Implementation Plan: Integrated RAG Chatbot

**Branch**: `001-rag-chatbot` | **Date**: 2025-12-16 | **Spec**: [specs/001-rag-chatbot/spec.md](../spec.md)
**Input**: Feature specification from `specs/001-rag-chatbot/spec.md`

## Summary

Build a production-grade RAG chatbot embedded in a Docusaurus book that answers questions strictly grounded in book content. Key features include full-book retrieval via Cohere/Qdrant, a "selected-text-only" mode for focused Q&A, and traceable provenance for all answers. The system will leverage the existing FastAPI backend and Neon Postgres database, adding new ingestion and query endpoints while maintaining high security and reproducibility standards.

## Technical Context

**Language/Version**: Python 3.11+
**Primary Dependencies**: FastAPI, Cohere SDK, Qdrant Client, SQLAlchemy (async), Pydantic
**Storage**: Qdrant Cloud (Vectors), Neon Serverless Postgres (Metadata), Local/S3 (Ingestion Artifacts - transient)
**Testing**: pytest (Unit/Integration), specialized RAG evaluation suite
**Target Platform**: Cloud-hosted container (e.g., Fly.io/Render) + Docusaurus static site
**Project Type**: Web API + Frontend Widget
**Performance Goals**: <2s median latency for retrieval+generation; <5min full re-indexing time
**Constraints**: Qdrant Free Tier limits (approx 1 cluster), Neon Free Tier limits, Cohere API Rate Limits
**Scale/Scope**: Single book context (~50-200k tokens), <100 concurrent users

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [x] **Truth-first Retrieval**: Spec mandates answers grounded in text (FR-005) and fallback (User Story 1.2).
- [x] **User-selected Context Priority**: Spec explicitly defines "Selection-Only" mode behavior (FR-004, User Story 2).
- [x] **Traceable Provenance**: Spec requires source lists with scores and links (FR-006, User Story 3).
- [x] **Privacy & Secrets Hygiene**: Spec enforces env var configuration and no secrets in code (Constraints).
- [x] **Reproducibility & Automation**: Spec mandates deterministic hashing and re-indexing endpoints (FR-007, FR-008).
- [x] **Tech Stack Compliance**: Plan uses Cohere, Qdrant, Neon, FastAPI, Docusaurus as mandated.

## Project Structure

### Documentation (this feature)

```text
specs/001-rag-chatbot/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output (OpenAPI schemas)
└── tasks.md             # Phase 2 output
```

### Source Code (repository root)

```text
app/
├── core/
│   ├── config.py          # Update with Cohere/Qdrant settings
│   └── security.py        # Reuse existing JWT logic
├── db/
│   └── models.py          # Add DocumentChunk, IngestionJob, QueryLog models
├── routers/
│   ├── ingest.py          # New: /ingest endpoints
│   ├── query.py           # New: /query endpoints
│   └── admin.py           # New: /admin/reindex endpoint
├── services/
│   ├── ingestion.py       # Core logic: Markdown parsing, chunking, hashing
│   ├── rag.py             # Core logic: Embedding, Retrieval, Generation
│   └── vector_db.py       # Qdrant client wrapper
└── schemas/
    ├── ingest.py          # Pydantic models for ingestion payloads
    └── query.py           # Pydantic models for query request/response
    
tests/
├── integration/
│   ├── test_ingestion.py
│   └── test_query_flow.py
└── unit/
    ├── test_chunking.py
    └── test_provenance.py
```

**Structure Decision**: Option 2 (Web application) - Extending existing backend structure.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| New Service Layer (`services/`) | Encapsulate complex RAG logic (chunking, embedding, retrieval) | Placing logic in routers makes them untestable and bloated. |
| Hybrid Storage (SQL + Vector) | Metadata reliability and job tracking | Storing all metadata in Qdrant limits complex filtering/job management. |
