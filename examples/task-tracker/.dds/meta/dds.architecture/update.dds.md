---
id: meta-architecture-update
type: meta
status: active
dependencies: [meta-architecture-rules, meta-architecture-write]
last_updated: 2026-09-18
description: Machine-readable protocol for atomic schema updates, two-way impact assessment, concurrency locking, and architectural versioning.
---

# SYSTEM_DIRECTIVE: ARCHITECTURE_UPDATE_AND_SYNC_PROTOCOL

## [0] DEFINITION & SCOPE

This document defines the strict lifecycle for modifying existing `.dds.md` files within the `.dds/architecture/` directory.
Because the `architecture` tier sits in the middle of the Truth Hierarchy, updates here have both upward constraints and downward cascading effects. EXECUTOR (System Architect, DevOps, or AI Agent) MUST execute these steps with extreme precision.

## [1] CONCURRENCY_CONTROL (LOCKING_PROTOCOL)

Before reading or writing architectural content, EXECUTOR MUST secure the target file.

**LOCK_ACQUISITION_ROUTINE:**

1. RUN `python .dds/meta/scripts/dds.py lock <target_file> --by <executor_id>`.
   - The script writes `locked_by: <executor_id>` and `locked_at: <UTC ISO-8601 timestamp>` into the frontmatter.
   - IF the file is already locked by another executor AND the lock is younger than 40 minutes, the script exits with `STATUS: LOCKED_BY <other_id> (<age> min)`. EXECUTOR MUST ABORT and retry after a delay (Exponential Backoff).
   - IF the lock is older than 40 minutes (crashed executor or disconnected agent), the script takes the lock over and reports `STATUS: LOCK_TAKEN_OVER`.
2. MANUAL FALLBACK (script unavailable): READ `locked_by` and `locked_at` from the frontmatter; apply the same 40-minute rule by comparing `locked_at` with the current UTC time; write both fields yourself.
3. **NEVER COMMIT A LOCK:** `locked_by` and `locked_at` are transient. `dds.py check --gate` (the commit gate) fails while any lock is present; plain `check` lists locks as INFO.
4. This section applies ONLY when `.dds/tree.dds.md` sets `locking: on` (default `off`). The script acquires the real mutex through an exclusive-create sidecar in gitignored `.dds/.locks/` and mirrors it into the frontmatter; the manual fallback has no atomicity guarantee, so two executors racing within the same second may both believe they hold the lock.
5. **SCOPE OF A LOCK:** a lock coordinates executors that share ONE working copy (several agents or people on the same checkout). Uncommitted frontmatter never reaches another clone; across clones, isolate work with branches.

## [2] ATOMIC_MUTATION_PROTOCOL

EXECUTOR is FORBIDDEN from rewriting the entire architecture document just to modify a single database column or API endpoint.

**MUTATION_CONSTRAINTS:**

- EXECUTOR MUST locate the exact Markdown header (`##` or `###`) corresponding to the changed data model, tech stack, or boundary.
- EXECUTOR MUST perform a localized `diff` update ONLY on that specific chunk.
- EXECUTOR MUST strictly apply the `ARCHITECTURAL_LINGUISTICS` (Exact Data Typing, chunk-local referents) defined in `.dds/meta/dds.architecture/write.dds.md`.

## [3] TWO-WAY_IMPACT_ASSESSMENT (THE MIDDLE-CHILD PROTOCOL) - CRITICAL

A change in data models or infrastructure MUST be validated against business goals and pushed down to the codebase.

**ASSESSMENT_ROUTINE:**

1. **UPWARD_CHECK (Product Tier Validation):** Does this infrastructure change (e.g., dropping a table, changing a third-party API) violate an existing Business Requirement or KPI defined in `.dds/product/`?
   -> IF YES: EXECUTOR MUST HALT the update. Architecture CANNOT overrule Product. The business requirement must be updated first.
2. **DOWNWARD_CASCADE (Modules Tier Execution):** Does this schema or API contract change affect how specific code modules behave? (e.g., A column name changed from `userId` to `user_id`).
   -> IF YES: EXECUTOR MUST route a task to update the relevant `.dds/modules/` documents to reflect the new data shape.

## [4] METADATA_AND_CHANGELOG_MUTATION (SCHEMA VERSIONING)

Every architectural shift MUST leave an audit trail to track database and infrastructure evolution.

**ACTION 1: Frontmatter Restoration:**

- UPDATE `last_updated: [YYYY-MM-DD]` to the current execution date.
- RUN `python .dds/meta/scripts/dds.py unlock <target_file>` (removes `locked_by` and `locked_at`). Manual fallback: delete both fields.

**ACTION 2: Log Append (Capped):**

1. LOCATE `## Changelog` at the bottom of the file (Create it if missing).
2. APPEND new entry: `- [YYYY-MM-DD]: [Brief description of the schema/infrastructure change].`
3. IF the Changelog now holds MORE THAN 10 entries, REMOVE the oldest entries until 10 remain. Removed entries stay available through `git log -- <file>`; `dds.py check` warns above 10.

## [5] PRE-FLIGHT_SELF_CORRECTION

BEFORE releasing the lock, EXECUTOR MUST self-audit the modified chunks.

**VALIDATION_STEPS:**

1. **Feature Logic Leakage:** Did I accidentally introduce feature-specific logic (e.g., "how the login button works") into this structural document? -> IF YES, abstract it to pure boundaries and data shapes.
2. **Type Strictness:** Are the newly added database columns using exact data types (e.g., `VARCHAR(50)`, `BOOLEAN`)? -> IF NO, correct them.

**FINAL_CHECK:** RUN `python .dds/meta/scripts/dds.py check` after the lock is released ([4] ACTION 1). IF it fails, fix the reported errors before reporting `SYNC_COMPLETE`.

*Output: EXECUTOR returns `STATUS: SYNC_COMPLETE` ONLY IF locks are released, Upward Checks pass, and Downward Tasks (if any) are created.*

# END_OF_DIRECTIVE
