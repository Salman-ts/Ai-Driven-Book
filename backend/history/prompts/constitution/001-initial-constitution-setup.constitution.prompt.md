---
id: 001
title: Initial Constitution Setup
stage: constitution
date: 2025-12-16
surface: agent
model: gemini-2.0-flash-exp
feature: none
branch: main
user: uni-tech
command: /sp.constitution
labels: ["setup", "governance"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - (none)
---

## Prompt

/sp.constitution

Project: Integrated RAG Chatbot for Book — Retrieval-Augmented Generation chatbot embedded in the published Spec-Kit Plus/Docusaurus book.
Stack (required): Cohere API (embeddings + generation + optional rerank), Qdrant Cloud (Free Tier) for vector index, Neon Serverless Postgres for metadata, FastAPI backend, Docusaurus frontend integration, Spec-Kit Plus + Gemini CLI for spec/code scaffolding.

Core principles

Truth-first retrieval: Answers must be grounded in exact book text and retrievable sources. When the retrieved evidence is insufficient, the assistant must explicitly say so rather than hallucinate.

User-selected context priority: If the user selects text, the system treats that text as authoritative context and prefers it above other retrieved material.

Traceable provenance: Every factual assertion must include provenance — section/chapter IDs, snippet offsets, and scoring metadata — so users can verify claims.

Minimal hallucination policy: When the model cannot support a claim with retrieved evidence, it must respond with a safe fallback (e.g., “I don’t know based on the provided text”) and provide steps to obtain verification.

Privacy & secrets hygiene: No book content, user-submitted text, or API keys are leaked to logs or third parties. All keys are stored in secure secrets (environment variables / CI secrets).

Reproducibility & automation: Ingest, indexing, and tests are automated so other contributors can reproduce the RAG index and validation pipeline. Use Spec-Kit Plus and Gemini CLI to produce reproducible scaffolding.

Key standards (behavioural, technical, and editorial)

Primary retrieval source: The published book content (indexed by module/chapter/section) — this is canonical.

Citation style for answers: Provide provenance inline; for any factual claim include: (Module X — Chapter Y — Section Z) [score=0.87]. For quoted passages, include APA-style reference in the final section when requested.

Selected-text behavior: If user explicitly asks “Answer using only selected text,” the RAG pipeline must:

Use selection as sole context (no external retrieval).

If selection insufficient for answer, return explicit “insufficient evidence” response and suggest the nearest supporting sections.

Embeddings & retrieval: Use Cohere embeddings for vectorization; store vectors in Qdrant with cosine similarity (or distance metric recommended by Cohere). Maintain mapping table in Neon Postgres: doc_id, module, chapter, section_id, chunk_id, qdrant_point_id, token_count, checksum, source_url.

Chunking: Chunk book text for indexing with overlap (e.g., 600–900 token chunk size with 20–30% overlap) — exact parameters recorded in ingestion config.

Relevance & rerank: Retrieve top-N (configurable) from Qdrant, optionally apply Cohere Rerank or MMR to prefer diverse yet relevant chunks before synthesis. Reranking weights and parameters must be documented.

Prompting & generation: Use Cohere Generate (or the recommended Cohere chat/generate workflow) with clear system instructions that force attribution to retrieved chunks and require explicit "source block" for each claim. Never prompt the model to invent sources.

Latency & performance: Document expected SLOs (e.g., median retrieval+generation latency) and fallback UX for slow networks. (Implementation teams will define precise SLO values based on infra.)

CI & tests: All ingestion, indexing, and retrieval code must include unit tests and integration tests. End-to-end tests must verify sample queries return expected provenance and no hallucinations for known inputs.

Constraints

API constraint: Use Cohere API only for embedding/generation/reranking. Do not use OpenAI APIs or OpenAI API keys. (If any third-party LLM is later approved, it must be documented and reapproved.)

Free-tier limits: Qdrant Free Tier and Neon Serverless free tiers have usage constraints — index size, QPS, and storage must be planned accordingly; include sharding/pruning strategy in /sp.plan.

Data residency / export: Book content and user selections may contain IP. Ensure Neon and Qdrant accounts are configured per institution policy; sanitize user-provided data when persisted.

Security: No secrets in repo; CI/CD uses GitHub Actions secrets (or equivalent). All endpoints must require authentication for write/ingest operations; read/query can be public or protected per project policy.

Integrations: FastAPI backend handles retrieval, aggregation, provenance formatting, and Cohere calls. The Docusaurus frontend is responsible for user selection UX and query submission. The RAG UI should be embeddable in the book pages as a client that calls the backend.

Success criteria (measurable)

Authoritative retrieval: For 95% of benchmark queries from a validation set derived from the book, the top-1 generated answer must cite at least one correct source chunk (human-evaluated).

Selected-text accuracy: For queries labeled “selected-text only” in the validation suite, the system must either answer correctly using only the selection or declare insufficiency with no hallucination in 100% of cases.

Provenance visibility: All answers must include source pointers (module/chapter/section/chunk) and a relevance score.

Reproducible ingestion: Given the raw book markdown/HTML, the ingestion pipeline (chunk → embed → index → metadata) must be runnable via CI and produce identical vector indices (within deterministic tolerances).

Security & compliance: No secrets checked into version control; all server endpoints follow auth and rate limiting policies defined in /sp.plan.

Performance: Retrieval + generation median latency acceptable for interactive use (project team to define numeric SLOs).

Deployability: The frontend widget can be embedded into the Docusaurus book and works against the FastAPI backend deployed to the chosen host.

Technical requirements (high level)

Ingestion & Indexing

Ingest formats: Markdown / HTML from Docusaurus build artifacts.

Chunking: configurable token-based chunking with overlap and checksum.

Embeddings: Cohere embedding model (configurable), vector dim logged.

Index: Qdrant Cloud, store metadata pointer to Neon Postgres.

Mapping DB: Neon Serverless Postgres to store document metadata, ingestion jobs, revision history, and mapping to Qdrant IDs.

Deterministic pipeline: hashing of content + manifest to avoid duplicate indexing.

Retrieval & Rerank

Vector retrieval: Qdrant top-K retrieval, configurable K.

Rerank: Cohere Rerank or MMR to reorder candidates.

Selected-text override: toggle to use selection-only retrieval.

Synthesis & Generation

Generator: Cohere Generate with controlled sampling (temperature, max_tokens, stop sequences).

Attribution policy: always include “Sources” block listing the supporting chunks.

Answer format: machine-readable JSON and human-readable string (for UI).

Backend

FastAPI app: endpoints for ingest, query, health, metadata, reindex, admin.

Auth: JWT or API key for admin endpoints; optional OAuth for user-level features.

Observability: request logs, trace IDs, metrics (latency, QPS, cost).

Frontend

Docusaurus-embeddable widget: selection capture, query input, display of answer + sources, copy export.

Accessibility: keyboard support, readable formatting, contrast.

Fallback: When backend unavailable, show offline help or cached docs.

Dev tooling & automation

Use Spec-Kit Plus to generate /sp.spec files for ingestion, retrieval, and UI, and to orchestrate tasks.

Use Gemini CLI for fast local scaffolding, code generation, and iterative prompt tuning (store prompts in repo).

CI: GitHub Actions to run ingestion test, unit tests, and deploy (use secrets for Cohere, Qdrant, Neon).

Testing, validation & acceptance checks (examples)

Unit tests: chunker correctness (token counts, overlap), metadata mapping, Cohere client wrapper stubs.

Integration tests: index a small book subset, run queries with expected top documents (assert Qdrant returns expected IDs).

E2E tests: simulate selection-based query + full retrieval + generation — assert output contains expected source references and no unsupported facts.

Benchmark set: curated set of 100 Q/A pairs and 50 selection-only pairs from the book for automated evaluation (metrics: Precision@1, Recall@k, MRR, hallucination rate).

Security tests: secrets scanning, endpoint auth checks, rate limiting tests.

Performance tests: measure retrieval+generation latency under representative load.

Decisions that must be documented (format: decision + options + tradeoffs)

Embedding model choice (Cohere): embed-small vs embed-medium vs embed-large — tradeoffs: accuracy vs cost vs vector dim.

Chunk size & overlap: smaller chunks = more precise pinpointing vs larger chunks = more context per vector.

Retrieval flow: Qdrant-only vs Qdrant + Cohere rerank — tradeoffs: speed vs precision.

Selected-text semantics: strict (only selection) vs preferential (selection + retrieval) — tradeoffs: fidelity vs helpfulness.

Where to host backend: Fly.io / Railway / Render / self-hosted — tradeoffs: latency, cost, ease of CI/CD.

Provenance format: inline short pointer vs full APA citation — tradeoffs: readability vs formality.

Storage & retention: keep user selections in DB? (yes: enables analytics; no: privacy-preserving). Document choice.

Governance & editorial rules

Source-of-truth: Book content (published/committed Docusaurus HTML/Markdown) only. External sources permitted only with explicit citation and labeled as “external.”

Plagiarism & reuse: When quoting long passages, keep within copyright and include proper APA reference.

Prompt & prompt-tuning governance: Store canonical prompt templates in repo; maintain versioning and test harness for prompt changes.

Change log: Any reindexing or ingestion change must be recorded with checksum and reason.

Deliverables (minimum)

/sp.spec files: ingestion, retrieval, rerank, generation, frontend widget, CI scripts.

Ingest pipeline code + config (tokenizer, chunker, embedder, indexer).

FastAPI backend with documented endpoints and authentication.

Docusaurus embeddable widget and example pages.

Test suite and benchmark dataset (selection of gold Q/A).

Deployment playbook (how to deploy Qdrant/Neon/FastAPI/Cohere secrets).

Decision register and architecture diagram(s) in ASCII + markdown.

Acceptance criteria (pass/fail)

Pass if: the system answers benchmark queries with correct provenance ≥ 95% (and selection-only queries with 100% no-hallucination flag when selection insufficient), ingestion pipeline is reproducible, and the widget integrates into the Docusaurus site.

Fail if: generated answers include unsupported factual claims without provenance, ingestion is non-deterministic, or secrets are exposed in repo/CI.

Notes & warnings

Cohere usage costs must be monitored; embed/generate calls can be high volume. Add sampling or caching layers.

Qdrant free tier capacity may limit index size — include pruning/segmentation strategy early.

Simplicity first: implement selection-only flow and a small index for the hackathon MVP before scaling.

## Response snapshot

Updated the project constitution to v1.0.0 with new principles (Truth-first Retrieval, User-selected Context Priority, Traceable Provenance, etc.) and defined the technical stack (Cohere, Qdrant, Neon, FastAPI).

## Outcome

- ✅ Impact: Established project governance and technical baseline.
- 🧪 Tests: N/A
- 📁 Files: Updated constitution.md
- 🔁 Next prompts: /sp.plan
- 🧠 Reflection: Successfully synthesized a comprehensive constitution from detailed user input.

## Evaluation notes (flywheel)

- Failure modes observed: None
- Graders run and results (PASS/FAIL): PASS
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
