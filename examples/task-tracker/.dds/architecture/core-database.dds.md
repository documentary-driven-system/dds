---
id: architecture-core-database
type: architecture
status: active
dependencies: [product-task-management, product-constraints]
last_updated: 2026-09-18
description: The users, tasks, and task_deletions tables in PostgreSQL with exact types and constraints.
---

# ARCHITECTURE: Core Database

## [0] CONTEXT_AND_ALIGNMENT
The core database stores users and tasks for the Task Management epic (`product-task-management`) under constraints C1, C2, and C4 of `product-constraints`.

## [1] TECH_STACK_AND_INFRASTRUCTURE
- **PostgreSQL:** 16.0 - Single primary; nightly logical backup retained 30 days.

## [2] DATA_MODELS_AND_SCHEMAS
<schema>
### [Core_DB] users
- `id` (UUIDv4) - PRIMARY KEY - Stable identifier; the row survives erasure in anonymised form (C2).
- `email` (VARCHAR(254)) - UNIQUE, NOT NULL - Login identifier; replaced by an opaque hash on erasure (C2).
- `password_hash` (VARCHAR(255)) - NOT NULL - Argon2id hash only (C1).
- `created_at` (TIMESTAMPTZ) - NOT NULL.

### [Core_DB] tasks
- `id` (UUIDv4) - PRIMARY KEY.
- `title` (VARCHAR(200)) - NOT NULL.
- `owner_id` (UUIDv4) - FOREIGN KEY users.id, NOT NULL.
- `due_date` (DATE) - NOT NULL.
- `status` (VARCHAR(16)) - NOT NULL - One of `open`, `done`.
- `created_by` (UUIDv4) - FOREIGN KEY users.id, NOT NULL.
- `created_at` (TIMESTAMPTZ) - NOT NULL.
- `completed_at` (TIMESTAMPTZ) - NULL until completion.
- `completed_by` (UUIDv4) - FOREIGN KEY users.id, NULL until completion.

### [Core_DB] task_deletions
- `task_id` (UUIDv4) - NOT NULL - Copy of the deleted task id (C4).
- `deleted_by` (UUIDv4) - NOT NULL.
- `deleted_at` (TIMESTAMPTZ) - NOT NULL - Rows older than 12 months are purged by a monthly job.
</schema>

## [3] GLOBAL_BOUNDARIES_AND_API_CONTRACTS
- Only the Tasks and Auth modules write to these tables; every other module reads through their APIs.
- A task deletion MUST insert its `task_deletions` row in the same transaction as the delete.

## Changelog
- [2026-09-18]: Promoted from draft after review.
