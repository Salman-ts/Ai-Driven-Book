# Research & Decisions: Integrated RAG Chatbot

**Feature Branch**: `001-rag-chatbot`
**Date**: 2025-12-16

## Decisions

### 1. Docusaurus Markdown Parsing
**Decision**: Use `frontmatter` + `mistune` (or `markdown-it-py`) with custom renderers.
**Rationale**: 
- `python-frontmatter` reliably extracts metadata (title, slug, tags) needed for structured Qdrant payloads.
- `markdown-it-py` (Python port of markdown-it) is robust and extensible. We can write a simple plugin/renderer to strip Docusaurus-specific tags (like `<Tabs>`) or admonitions (`:::tip`) which create noise for embeddings.
- **Why not LangChain loaders**: Generic Markdown loaders often choke on Docusaurus-specific syntax or treat frontmatter as content. Custom parsing ensures cleaner semantic chunks.
**Alternatives Considered**:
- `BeautifulSoup` on HTML build output: Rejected per spec clarification (Raw Markdown preferred for cleanliness).
- `Unstructured`: Too heavy/slow for this specific use case.

### 2. Cohere RAG Pattern
**Decision**: Use Cohere's Chat API (`co.chat`) with `documents` parameter (RAG mode).
**Rationale**: 
- Cohere's native RAG mode handles context injection and citation generation automatically. passing retrieved chunks in the `documents` list allows the model to generate fine-grained citations (provenance) natively.
- This simplifies the "Generation Layer" significantly compared to manual prompt engineering.
**Alternatives Considered**:
- Standard Prompting ("Answer based on this context..."): Harder to enforce strict provenance and citation format.

### 3. Qdrant Search Strategy
**Decision**: Dense Vector Search + Metadata Filters.
**Rationale**:
- **Selection-Only Mode**: Implemented via a `must` filter on `doc_id` or similar metadata, effectively restricting search to the selected scope (if we indexed selections, though spec says "ignore Qdrant" for selection-only. For *hybrid* search or chapter-scoping, Qdrant's payload filtering is highly performant).
- **Hybrid Search**: Qdrant supports hybrid (sparse+dense) but for this book-RAG, dense search with good semantic chunking is usually sufficient. We will stick to **Dense Search** for Phase 1 to keep complexity low, as mandated by constraints.
**Alternatives Considered**:
- Sparse Vectors (BM25): Adds complexity (need sparse encoder). Reserve for "Phase 2" optimization if keyword search is poor.

### 4. Rate Limiting
**Decision**: `slowapi` (based on `limits`).
**Rationale**: 
- Simple decorator-based implementation compatible with FastAPI.
- Uses in-memory storage by default (good for single-instance deployment constraint) but can switch to Redis later.
- Easy to configure per-endpoint (`@limiter.limit("5/minute")`).
**Alternatives Considered**:
- `fastapi-limiter`: Requires Redis (violates "Neon + Qdrant only" simplicity unless we use a mock redis, which is brittle).
- Nginx/Infrastructure limits: Harder to configure for specific user logic/claims.

## Outstanding Questions (Resolved)
- **Ingestion**: We will write a custom `IngestionService` using `markdown-it-py` to parse docs.
- **Auth**: Admin auth will use the existing `verify_admin` dependency (to be created based on `get_current_user`).

## Next Steps
- Implement `app/services/ingestion.py` with custom parsing.
- Update `requirements.txt` with `cohere`, `markdown-it-py`, `python-frontmatter`, `slowapi`.
