---
id: architecture-tech-stack
type: architecture
status: active
dependencies: [product-vision]
last_updated: 2026-09-18
description: Python, FastAPI, PostgreSQL, Docker Compose, and the global API boundaries.
---

# ARCHITECTURE: Tech Stack

## [0] CONTEXT_AND_ALIGNMENT
The TaskTracker tech stack serves the product vision (`product-vision`): a small-team tool that one engineer can run and that an AI agent can change safely.

## [1] TECH_STACK_AND_INFRASTRUCTURE
- **Python:** 3.12 - Application language for every module under `src/`.
- **FastAPI:** 0.115 - HTTP API layer.
- **PostgreSQL:** 16 - Primary relational database for users and tasks.
- **Docker Compose:** 2.x - Local and staging orchestration; one container per service.

## [2] DATA_MODELS_AND_SCHEMAS
<schema>
The tech stack document holds no tables; every schema lives in `architecture-core-database`.
</schema>

## [3] GLOBAL_BOUNDARIES_AND_API_CONTRACTS
- Every HTTP request except `POST /auth/login` MUST carry a valid Bearer JWT issued by the Auth module.
- Every service MUST log to stdout as JSON lines; no service writes log files.
- Every call to a third-party network API MUST be listed in `product-constraints` C3 review before the first deployment.

## Changelog
- [2026-09-18]: Promoted from draft after review.
