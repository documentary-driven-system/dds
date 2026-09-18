---
id: modules-tasks-create
type: module
status: active
dependencies: [architecture-core-database, product-task-management]
sources: [src/tasks/create.py, src/tasks/models.py]
last_updated: 2026-09-18
description: Validation, ownership, and insertion rules for TaskService.create.
---

# TASKS: Create Task

## [0] CONTEXT_AND_PURPOSE
The `TaskService.create` function is responsible for turning a validated request into one `tasks` row within the Tasks domain boundary, serving the first user story of `product-task-management`.

## [1] TECHNICAL_CONSTRAINTS
<constraints>
- `TaskService.create` MUST reject a request whose `title` is empty or longer than 200 characters, or whose `due_date` is missing (HTTP 422 listing every failing field).
- `TaskService.create` MUST set `created_by` to the JWT subject and `created_at` to the database clock; the request body carries neither.
- `TaskService.create` MUST write exactly one `tasks` row per idempotency key; a client retry with the same key returns the existing task.
</constraints>

## [2] LOGIC_FLOW
1. `TaskService.create` validates the payload against the `tasks` schema (`architecture-core-database`) and returns HTTP 422 on failure.
2. `TaskService.create` resolves `owner_id`; an unknown owner returns HTTP 404.
3. `TaskService.create` inserts the row with `status = open` and returns the task with HTTP 201.

## Changelog
- [2026-09-18]: Promoted from draft after review.
- [2026-09-15]: Title limit aligned with `tasks.title VARCHAR(200)` (`architecture-core-database`).
- [2026-09-12]: Idempotency key constraint added after duplicate tasks appeared on client retries.
- [2026-09-09]: `created_by` now taken from the JWT subject instead of the request body.
- [2026-09-05]: HTTP 404 for an unknown owner replaces the former HTTP 422.
- [2026-09-02]: Due date in the past is allowed; the late list handles it (`product-vision` story 1).
- [2026-08-28]: Validation errors list every failing field instead of the first one.
- [2026-08-22]: Draft reverse-documented from `src/tasks/create.py` during adoption.
- [2026-08-20]: Owner resolution moved before validation of the due date.
- [2026-08-18]: Document created as `status: draft`.
