# Feature Specification: Integrated RAG Chatbot

**Feature Branch**: `001-rag-chatbot`  
**Created**: 2025-12-16  
**Status**: Draft  
**Input**: Integrated RAG Chatbot Embedded in Book (Cohere + Qdrant + Neon)

## Clarifications
### Session 2025-12-16
- Q: Ingestion Input Format: Raw Markdown or HTML Build Output? → A: Raw Markdown Source (`docs/**/*.md`) to ensure cleaner semantic chunking and avoidance of HTML noise.
- Q: Admin Auth Mechanism? → A: JWT/OAuth (Option B) - Leverage existing `auth` router and `get_current_user` dependency, requiring an admin role/claim for sensitive endpoints like `/admin/reindex`.
- Q: Copy/export answer format? → A: Dual Format (Markdown + HTML) for comprehensive sharing options.
- Q: Rate Limiting Strategy? → A: Basic Server-Side Rate Limiting on the FastAPI backend to prevent abuse and manage external API costs.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Full-Book Q&A (Priority: P1)

A reader wants to ask a conceptual question about the book's content and receive an accurate answer cited from the text, so they can understand the material without manually searching.

**Why this priority**: Core value proposition of the RAG system.

**Independent Test**: Can be tested by ingesting the book and running queries against the `/query` endpoint without frontend integration.

**Acceptance Scenarios**:

1. **Given** the book is ingested, **When** user asks "What is the definition of Agentic Workflow?", **Then** the system returns a coherent answer citing the specific chapter and section.
2. **Given** a query with no relevant content in the book, **When** user asks "How to bake a cake?", **Then** the system explicitly states "I cannot answer this based on the provided text" (no hallucination).
3. **Given** a valid query, **When** an answer is generated, **Then** it includes a "Sources" list with clickable references to book sections.

---

### User Story 2 - Selected-Text Q&A (Priority: P1)

A reader highlights a specific paragraph and asks a question about *just that text* (e.g., "Explain this code snippet"), so they can get focused help without the system retrieving irrelevant global context.

**Why this priority**: Critical for detailed comprehension and preventing "context pollution" from other chapters.

**Independent Test**: Can be tested by sending a query payload with `selection_context` populated and `selection_only=true`.

**Acceptance Scenarios**:

1. **Given** user selects a paragraph about "Chain of Thought", **When** they ask "Summarize this", **Then** the answer is derived *only* from that selected text.
2. **Given** user selects text, **When** they ask a question not answerable by that selection, **Then** the system returns "Not enough evidence in selection" even if the answer exists elsewhere in the book.

---

### User Story 3 - Provenance & Verification (Priority: P2)

A technical reviewer or skeptical reader wants to verify the chatbot's claim, so they click the source citation to jump to the exact location in the book.

**Why this priority**: Essential for trust and technical correctness (Success Criterion: Traceable Provenance).

**Independent Test**: Verify the API response structure contains `provenance` metadata (chunk ID, section URL, score).

**Acceptance Scenarios**:

1. **Given** a generated answer, **When** user inspects the sources, **Then** each source includes a precise location identifier (Chapter > Section).
2. **Given** a factual claim in the answer, **When** verified against the cited source, **Then** the source text directly supports the claim.

### Edge Cases

- **Empty Selection**: User switches to "Selected Text Only" mode but selects nothing. System should prompt to select text.
- **Service Outage**: Qdrant or Cohere API is down. System should return a graceful error message, not a 500 stack trace.
- **Rate Limits**: User spams queries. System should implement server-side rate limiting and handle upstream 429 errors gracefully.
- **Re-ingestion**: Admin triggers re-indexing while users are querying. System should maintain read availability or queue the job.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: System MUST provide an ingestion endpoint (`/ingest`) that accepts raw Docusaurus Markdown files (`docs/**/*.md`), chunks them by header/structure, and stores vectors in Qdrant and metadata in Neon Postgres.
- **FR-002**: System MUST provide a query endpoint (`/query`) that accepts a text query, optional selected text context, and a mode flag (Global vs. Selection-Only).
- **FR-003**: In "Global" mode, system MUST retrieve top-K relevant chunks from Qdrant using Cohere embeddings.
- **FR-004**: In "Selection-Only" mode, system MUST ignore Qdrant retrieval and use the provided selection as the sole context.
- **FR-005**: System MUST generate answers using Cohere's generation API, strictly conditioned on the retrieved/selected context.
- **FR-006**: Generated answers MUST include a structured list of sources, each containing: Chapter Title, Section Title, and Relevance Score.
- **FR-007**: System MUST provide an admin endpoint (`/admin/reindex`) to trigger a full rebuild of the vector index from source.
- **FR-008**: System MUST deterministically hash content chunks to prevent duplicate vectors upon re-ingestion.
- **FR-009**: Frontend widget MUST capture user text selections from the Docusaurus page and populate the query context.
- **FR-010**: Frontend widget MUST display the answer and render clickable source links that navigate to the cited book section.
- **FR-011**: Frontend widget MUST provide a "Copy" function that places the answer and its references onto the clipboard in both Markdown and HTML formats.
- **FR-012**: Implementation MUST utilize the existing backend structure, refactoring only as necessary to meet RAG requirements; backend rewrite is out of scope.
- **FR-013**: Admin endpoints MUST be protected by existing JWT-based authentication, requiring an admin role/scope.
- **FR-014**: The FastAPI backend MUST implement basic server-side rate limiting for query endpoints to manage resource usage and prevent abuse.

### Key Entities

- **DocumentChunk**: Represents a discrete, indexable part of the book (e.g., a paragraph or section). Attributes: content, vector_id, source_url, checksum, token_count.
- **IngestionJob**: Record of an ingestion run. Attributes: status, start_time, end_time, chunk_count, error_log.
- **QueryLog**: (Optional/Anonymized) Record of queries for debugging. Attributes: timestamp, mode (global/selection), latency.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: **Authoritative Retrieval**: ≥95% of benchmark questions return answers where the top cited source is correct (human-verified).
- **SC-002**: **Zero Hallucination in Selection Mode**: 100% of "selected-text-only" queries either answer correctly from selection or state "insufficient evidence".
- **SC-003**: **Traceable Provenance**: 100% of factual answers include at least one valid citation (Section/Chapter reference).
- **SC-004**: **Reproducibility**: Re-running ingestion on the same source content produces identical vector checksums and Qdrant object counts.
- **SC-005**: **Availability**: System runs within the constraints of Qdrant Free Tier (storage/throughput) and Neon Free Tier.

## Constraints & Assumptions

- **Infrastructure**: Must use Cohere (Embed/Generate), Qdrant Cloud (Free), and Neon Serverless Postgres.
- **Security**: No secrets in code. All configuration via environment variables.
- **Cost**: implementation must minimize unnecessary API calls (e.g., caching embeddings if content hasn't changed).
- **Scope**: No fine-tuning; RAG only. No multi-book support (single repository context).
- **Implementation**: Implementation MUST leverage existing backend codebase (`app/`, `main.py`, etc.) and avoid creating a new service from scratch.