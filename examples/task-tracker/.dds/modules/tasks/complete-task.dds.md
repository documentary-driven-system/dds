---
id: modules-tasks-complete
type: module
status: active
dependencies: [architecture-core-database, product-task-management]
sources: [src/tasks/complete.py, src/tasks/models.py]
last_updated: 2026-09-18
description: Authorisation, timestamps, and the 24-hour reopen window for TaskService.complete.
---

# TASKS: Complete Task

## [0] CONTEXT_AND_PURPOSE
The `TaskService.complete` and `TaskService.reopen` functions are responsible for closing a task and for undoing a closure within 24 hours, serving the second user story of `product-task-management`.

## [1] TECHNICAL_CONSTRAINTS
<constraints>
- `TaskService.complete` MUST accept the call only from the task owner or a user with the Team Lead role; every other caller receives HTTP 403.
- `TaskService.complete` MUST set `completed_at` to the database clock and `completed_by` to the JWT subject in the same update.
- `TaskService.reopen` MUST refuse a task completed more than 24 hours earlier with HTTP 409.
</constraints>

## [2] LOGIC_FLOW
1. `TaskService.complete` loads the task and checks the caller against `owner_id` and the Team Lead role.
2. `TaskService.complete` updates `status`, `completed_at`, and `completed_by` in one statement and returns HTTP 200.
3. `TaskService.reopen` clears `completed_at` and `completed_by` and sets `status = open` when the completion is younger than 24 hours.

## Changelog
- [2026-09-18]: Promoted from draft after review.
