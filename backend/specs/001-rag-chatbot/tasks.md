# Tasks: Integrated RAG Chatbot

**Input**: Design documents from `/specs/001-rag-chatbot/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Testing tasks are included as requested by the plan.md (Unit/Integration).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Install new dependencies (cohere, qdrant-client, markdown-it-py, python-frontmatter, slowapi) in `requirements.txt`
- [X] T002 Update environment configuration `app/core/config.py` with Cohere, Qdrant, and Admin Auth settings
- [X] T003 [P] Configure basic rate limiting middleware in `main.py` using `slowapi`

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T004 Create SQLAlchemy models (DocumentChunk, IngestionJob, QueryLog) in `app/db/models.py`
- [X] T005 [P] Implement `verify_admin` dependency in `app/services/auth.py` for JWT-based admin access
- [X] T006 Initialize Qdrant client wrapper in `app/services/vector_db.py` (connection management)
- [X] T007 [P] Create Pydantic schemas for Ingestion/Query in `app/schemas/ingest.py` and `app/schemas/query.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

## Phase 3: User Story 1 - Full-Book Q&A (Priority: P1) 🎯 MVP

**Goal**: Enable users to ask grounded questions about the entire book content.

**Independent Test**: Ingest book -> Query endpoint returns cited answer.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T008 [P] [US1] Create integration test for ingestion flow in `tests/integration/test_ingestion.py`
- [X] T009 [P] [US1] Create integration test for global query flow in `tests/integration/test_query_flow.py`

### Implementation for User Story 1

- [X] T010 [US1] Implement Markdown parsing and chunking logic with `markdown-it-py` in `app/services/ingestion.py`
- [X] T011 [US1] Implement vector embedding and Qdrant upsert logic in `app/services/rag.py`
- [X] T012 [US1] Implement `ingest_content` function in `app/services/ingestion.py` (orchestrates parsing -> embedding -> storage)
- [X] T013 [US1] Create `/ingest` endpoint in `app/routers/ingest.py`
- [X] T014 [US1] Implement retrieval and grounded generation logic (Global Mode) in `app/services/rag.py` using Cohere
- [X] T015 [US1] Create `/query` endpoint in `app/routers/query.py` (handling Global mode)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

## Phase 4: User Story 2 - Selected-Text Q&A (Priority: P1)

**Goal**: Enable users to ask questions focused strictly on a selected text snippet.

**Independent Test**: Query with `selection_only=true` returns answer based only on selection.

### Tests for User Story 2 ⚠️

- [X] T016 [P] [US2] Create test case for selection-only query in `tests/integration/test_query_flow.py`

### Implementation for User Story 2

- [X] T017 [US2] Update `app/services/rag.py` to handle `selection_only` mode (bypass retrieval, direct context injection)
- [X] T018 [US2] Update `/query` endpoint in `app/routers/query.py` to pass selection context to service

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

## Phase 5: User Story 3 - Provenance & Verification (Priority: P2)

**Goal**: Ensure all answers include clickable source citations for verification.

**Independent Test**: API response includes structured `provenance` data.

### Tests for User Story 3 ⚠️

- [X] T019 [P] [US3] Create unit test for provenance formatting in `tests/unit/test_provenance.py`

### Implementation for User Story 3

- [X] T020 [US3] Update `app/services/rag.py` to parse Cohere citations and format `Source` objects
- [X] T021 [US3] Ensure `app/schemas/query.py` response model supports rich provenance data

**Checkpoint**: All user stories should now be independently functional

## Phase 6: Admin & Maintenance (Cross-Cutting)

**Purpose**: System maintenance and reliability

- [X] T022 [P] Create `/admin/reindex` endpoint in `app/routers/admin.py` (calls ingestion service)
- [X] T023 [P] Implement deterministic hashing in `app/services/ingestion.py` to prevent duplicates
- [X] T024 [P] Register new routers (ingest, query, admin) in `main.py`

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - **US1 (Full-Book)**: Independent.
  - **US2 (Selected-Text)**: Extends US1 logic (can be parallelized but easier sequential).
  - **US3 (Provenance)**: Enhances output of US1/US2.

### Parallel Opportunities

- T001, T002, T003 (Setup) can run in parallel.
- T004, T005, T006, T007 (Foundational) can run in parallel.
- Tests (T008, T009, T016, T019) can be written in parallel with implementation if TDD is strictly followed, or by a separate QA role.

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1 & 2.
2. Complete Phase 3 (Ingestion + Global Query).
3. **STOP and VALIDATE**: Ensure the bot answers questions from the book.

### Incremental Delivery

1. Add US2 (Selected Text) -> Validate isolation.
2. Add US3 (Provenance) -> Validate citations.
3. Finalize Admin endpoints (Phase 6).
