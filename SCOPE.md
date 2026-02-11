# SynaptIQ Context Intelligence Platform — Project Scope

**Version**: 1.0 (Frozen Architecture)
**Date**: February 2026
**Author**: Dinesh Srivastava
**Status**: Draft

---

## 1. Executive Summary

SynaptIQ is a **Context Intelligence Platform** that delivers shared organizational understanding through observation, inference, and explainable reasoning. It is **local-first**, **non-intrusive**, and **human-authoritative** — providing context awareness across enterprise tools without orchestrating or controlling business processes.

The platform eliminates context silos by building an intelligent context graph from existing enterprise systems (ERP, CRM, HRMS, ticketing, email, wikis) while preserving their role as systems of record.

---

## 2. Project Overview

### 2.1 Vision
A production-grade, local-first system that provides shared organizational context across enterprise tools — advisory, explainable, and non-intrusive.

### 2.2 Architectural Objectives
- Eliminate context silos across enterprise systems
- Preserve existing systems of record
- Provide ownership, freshness, trust, and activity awareness
- Remain advisory, explainable, and non-intrusive
- Be deployable locally / on-prem first
- Minimize dependence on LLMs

### 2.3 Architecture Status
**Frozen** — 8-layer reference architecture locked.

---

## 3. Scope of Work

### 3.1 In-Scope: 8-Layer Architecture

#### Layer 1: Source Systems Layer (Read-Only)
- Connect to ERP, CRM, HRMS, ticketing systems
- Connect to email & chat tools
- Connect to local/shared file systems
- Connect to wikis and document repositories
- **Constraints**: Read-only access, no workflow execution, no data ownership transfer

#### Layer 2: Ingestion & Observation Layer
- Observe changes and activity across source systems
- Normalize inputs into structured events
- Provide reliable temporal ordering
- **Outputs**: Normalized events (create, modify, access, reference)

#### Layer 3: Signal Extraction & Enrichment Layer
- Convert events into actionable signals
- Detect references, mentions, and relationships
- Enrich with semantic and temporal hints
- **Signal Types**: Activity, Relationship, Lifecycle, Parallel-work

#### Layer 4: Context Graph Layer (Core)
- Build and maintain the authoritative representation of organizational context
- **Design Principles**: Append-only, Temporal, Explainable, Relationship-first
- **Node Types**: Artifact, Person, System, Concept, Activity, Decision
- **Relationship Types**: CREATED_BY, OWNED_BY, MODIFIED_BY, REFERENCES, DEPENDS_ON, WORKING_ON, DUPLICATES, CONFLICTS_WITH, SUPERSEDES, RECORDED_IN, RESULTED_IN
- All relationships timestamped and non-destructive

#### Layer 5: Trust, Freshness & Confidence Layer
- Compute freshness scores
- Infer ownership confidence
- Detect conflicts and duplicates
- Produce reliability signals
- **Outputs**: Confidence metrics only — never data changes

#### Layer 6: Intelligence & Reasoning Layer
- Deterministic rule engine
- Graph traversal & reasoning
- Lightweight LLM (optional, last-mile only)
- Answer contextual questions
- Perform impact analysis
- Generate explanations

#### Layer 7: Interaction Layer
- Context-aware search
- Natural language Q&A
- Embedded context panels
- Read-only APIs

#### Layer 8: Governance & Control Layer
- Role-based access control (RBAC)
- Context-aware permissions
- Full audit trail
- Explainability support
- Local-first deployment constraints

### 3.2 Explicit Non-Goals (Locked)
- No workflow orchestration
- No business process automation
- No system-of-record replacement
- No core dependency on external workflow tools (e.g., n8n)
- No heavy workflow engines
- No cloud-only AI APIs
- No large distributed data lakes
- No black-box automation

---

## 4. Context Graph Schema

### 4.1 Node Types

| Node Type | Description | Key Properties |
|-----------|-------------|----------------|
| **Artifact** | Any informational object | artifact_id, artifact_type (doc/record/ticket/email/file), source_system, title, created_at, last_modified_at, lifecycle_state |
| **Person** | User/employee | person_id, name, role, team, org_unit |
| **System** | Source system | system_id, system_type, system_name |
| **Concept** | Abstract org concepts | concept_id, concept_type (project/customer/product/policy), name |
| **Activity** | Tracked action | activity_id, activity_type (create/edit/review/discuss/approve), timestamp |
| **Decision** | Recorded decision | decision_id, decision_type (explicit/inferred), timestamp, rationale |

### 4.2 Relationship Types

| Relationship | Direction | Description |
|-------------|-----------|-------------|
| CREATED_BY | Artifact → Person | Who created it |
| OWNED_BY | Artifact → Person | Current owner |
| MODIFIED_BY | Artifact → Person | Who modified it |
| REFERENCES | Artifact → Artifact/Concept | Cross-references |
| DEPENDS_ON | Artifact → Artifact | Dependencies |
| WORKING_ON | Person → Artifact/Concept | Active work |
| DUPLICATES | Artifact ↔ Artifact | Duplicate detection |
| CONFLICTS_WITH | Artifact ↔ Artifact | Conflicting info |
| SUPERSEDES | Artifact → Artifact | Version succession |
| RECORDED_IN | Activity → System | Activity source |
| RESULTED_IN | Decision → Artifact | Decision outcomes |

---

## 5. Technology Stack (Local-First)

### 5.1 Core Principles
- Runs on a single machine or on-prem cluster
- No mandatory cloud services
- Replaceable components
- Open standards

### 5.2 Proposed Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Ingestion** | Python watchdog, Redpanda/NATS | File watching, event bus |
| **Context Graph** | Neo4j Community / ArangoDB | Graph storage & traversal |
| **Signal Processing** | Python, custom rules | Deterministic inference |
| **Embeddings** | SentenceTransformers | Semantic processing |
| **Vector Store** | FAISS (local) | Similarity search |
| **LLM** | Ollama (qwen2.5-coder, llama3.1) | Optional last-mile reasoning |
| **API** | FastAPI | REST + event subscriptions |
| **UI** | React | Web interface |
| **Extensions** | Browser/IDE plugins | Context panels |
| **Auth** | Local IAM / LDAP | Access control |
| **Audit** | Append-only event logs | Governance trail |

---

## 6. Deliverables and Milestones

### Phase 1: Foundation
- [ ] Project structure and repository setup
- [ ] Development environment configuration
- [ ] Context Graph schema implementation (Neo4j/ArangoDB)
- [ ] Basic ingestion pipeline (file system watcher)
- [ ] Event bus setup (NATS/Redpanda)

### Phase 2: Core Intelligence
- [ ] Signal extraction engine
- [ ] Trust & freshness scoring system
- [ ] Deterministic rule engine
- [ ] Graph traversal & reasoning module
- [ ] Relationship detection pipeline

### Phase 3: Integration Layer
- [ ] Source system connectors (ERP, CRM, ticketing, email)
- [ ] FastAPI service layer
- [ ] Read-only REST APIs
- [ ] Event subscription endpoints

### Phase 4: Interaction & UI
- [ ] Context-aware search engine
- [ ] Natural language Q&A interface
- [ ] React web dashboard
- [ ] Embedded context panels (browser/IDE)

### Phase 5: Governance & Production
- [ ] RBAC implementation
- [ ] Audit trail system
- [ ] Explainability module
- [ ] Local deployment packaging
- [ ] Performance optimization
- [ ] Production hardening

---

## 7. Assumptions and Constraints

### Assumptions
- Source systems expose read-only APIs or file-based exports
- Local infrastructure (Mac Mini / on-prem server) is available
- Enterprise source systems are accessible from the deployment environment
- Team has access to enterprise system documentation

### Constraints
- Architecture is **frozen** — no structural changes without formal review
- **Local-first** — no mandatory cloud dependencies
- **Read-only** — platform never writes back to source systems
- **Advisory only** — no autonomous actions or workflow execution
- LLM usage is **optional and last-mile only**

---

## 8. Risks and Mitigation

| Risk | Impact | Mitigation |
|------|--------|------------|
| Source system API changes | High | Adapter pattern, version-pinned connectors |
| Graph database performance at scale | Medium | Partitioning, index optimization, benchmarking |
| Signal noise / false relationships | Medium | Confidence scoring, human-in-the-loop validation |
| LLM hallucination in reasoning | Low | Deterministic rules first, LLM as last resort only |
| Data privacy / access control | High | RBAC, local-only deployment, audit logging |

---

## 9. Acceptance Criteria

- All 8 architectural layers implemented and independently testable
- Context graph correctly maps relationships across 3+ source systems
- Trust/freshness scores computed and explainable
- Natural language queries return accurate context with source attribution
- Full audit trail for all graph operations
- Deployable on a single local machine without cloud dependencies
- Sub-second response time for context lookups
- RBAC enforced across all interaction points

---

## 10. Architecture Statement

> This reference architecture defines a **Context Intelligence Platform** that delivers shared organizational understanding through observation, inference, and explainable reasoning — while remaining non-intrusive, local-first, and human-authoritative.

**Architecture Status: FROZEN**

---

*SynaptIQ Context Intelligence Platform — Dinesh Srivastava — February 2026*
