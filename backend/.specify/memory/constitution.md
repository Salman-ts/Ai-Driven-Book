<!--
SYNC IMPACT REPORT
Version change: New File -> 1.0.0
Modified Principles: All new
Added Sections: Core Principles, Technical Constraints & Standards, Success Criteria, Governance
Removed Sections: None
Templates requiring updates: None (dynamic reference)
Follow-up TODOs: None
-->

# Integrated RAG Chatbot for Book Constitution

## Core Principles

### I. Truth-first Retrieval
Answers must be grounded in exact book text and retrievable sources. When the retrieved evidence is insufficient, the assistant must explicitly say so rather than hallucinate.

### II. User-selected Context Priority
If the user selects text, the system treats that text as authoritative context and prefers it above other retrieved material.

### III. Traceable Provenance
Every factual assertion must include provenance — section/chapter IDs, snippet offsets, and scoring metadata — so users can verify claims.

### IV. Minimal Hallucination Policy
When the model cannot support a claim with retrieved evidence, it must respond with a safe fallback (e.g., “I don’t know based on the provided text”) and provide steps to obtain verification.

### V. Privacy & Secrets Hygiene
No book content, user-submitted text, or API keys are leaked to logs or third parties. All keys are stored in secure secrets (environment variables / CI secrets).

### VI. Reproducibility & Automation
Ingest, indexing, and tests are automated so other contributors can reproduce the RAG index and validation pipeline. Use Spec-Kit Plus and Gemini CLI to produce reproducible scaffolding.

## Technical Constraints & Standards

### Stack & Infrastructure
- **API**: Cohere API (embeddings + generation + optional rerank).
- **Vector DB**: Qdrant Cloud (Free Tier).
- **Metadata DB**: Neon Serverless Postgres.
- **Backend**: FastAPI.
- **Frontend**: Docusaurus integration.
- **Scaffolding**: Spec-Kit Plus + Gemini CLI.

### Data Residency & Security
- Book content and user selections may contain IP. Ensure Neon and Qdrant accounts are configured per institution policy.
- Sanitize user-provided data when persisted.
- No secrets in repo; CI/CD uses GitHub Actions secrets.
- All endpoints must require authentication for write/ingest operations.

## Success Criteria

### Measurable Outcomes
- **Authoritative Retrieval**: For 95% of benchmark queries, the top-1 generated answer must cite at least one correct source chunk.
- **Selected-text Accuracy**: 100% correct answers or insufficiency declarations for selection-only queries.
- **Provenance Visibility**: All answers must include source pointers (module/chapter/section/chunk) and a relevance score.
- **Reproducible Ingestion**: The ingestion pipeline must be deterministic and runnable via CI.

## Governance

### Source of Truth
The published book content (indexed by module/chapter/section) is canonical.

### Amendments
This Constitution supersedes all other practices. Amendments require documentation and approval.

### Versioning Policy
Follow Semantic Versioning (MAJOR.MINOR.PATCH):
- MAJOR: Backward incompatible governance or principle changes.
- MINOR: New principle/section added or materially expanded guidance.
- PATCH: Clarifications, wording, typo fixes.

**Version**: 1.0.0 | **Ratified**: 2025-12-16 | **Last Amended**: 2025-12-16