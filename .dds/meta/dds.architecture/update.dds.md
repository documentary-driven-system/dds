---
id: dds_architecture_update_protocol
version: 1.0.0
type: operational_directive
dependencies: [meta/dds.architecture/rules.dds.md, meta/dds.architecture/write.dds.md]
priority: high
last_updated: 2026-04-12
description: Machine-readable protocol for atomic schema updates, two-way impact assessment, concurrency locking, and architectural versioning.
---

# SYSTEM_DIRECTIVE: ARCHITECTURE_UPDATE_AND_SYNC_PROTOCOL

## [0] DEFINITION & SCOPE

This document defines the strict lifecycle for modifying existing `.dds.md` files within the `.dds/architecture/` directory.
Because the `architecture` tier sits in the middle of the Truth Hierarchy, updates here have both upward constraints and downward cascading effects. EXECUTOR (System Architect, DevOps, or AI Agent) MUST execute these steps with extreme precision.

## [1] CONCURRENCY_CONTROL (LOCKING_PROTOCOL)

Before reading or writing architectural content, EXECUTOR MUST secure the target file.

**LOCK_ACQUISITION_ROUTINE:**

1. READ `status` field in the target file's YAML frontmatter.
2. IF `status` CONTAINS `locked_by_`, THEN EXECUTOR MUST ABORT operation and retry after a delay (Exponential Backoff).
3. IF `status` == `active`, THEN EXECUTOR MUST immediately overwrite it to `status: locked_by_[executor_id]`.
4. **LOCK_TIMEOUT_OVERRIDE:** IF `status` is locked, BUT the lock has been active for MORE THAN 40 MINUTES, EXECUTOR MAY forcefully overwrite the status to `locked_by_[new_executor_id]`.

## [2] ATOMIC_MUTATION_PROTOCOL

EXECUTOR is FORBIDDEN from rewriting the entire architecture document just to modify a single database column or API endpoint.

**MUTATION_CONSTRAINTS:**

- EXECUTOR MUST locate the exact Markdown header (`##` or `###`) corresponding to the changed data model, tech stack, or boundary.
- EXECUTOR MUST perform a localized `diff` update ONLY on that specific chunk.
- EXECUTOR MUST strictly apply the `ARCHITECTURAL_LINGUISTICS` (Exact Data Typing, Pronoun Ban) defined in `.dds/meta/dds.architecture/write.dds.md`.

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
- MUTATE `status` back to `active` (Releasing the lock).

**ACTION 2: Log Append & Rotation:**

1. LOCATE `## Changelog` at the bottom of the file (Create it if missing).
2. APPEND new entry: `- [YYYY-MM-DD]: [Brief description of the schema/infrastructure change].`
3. COUNT total entries in the Changelog.
4. IF total entries > 10:
   - EXTRACT the oldest entries (keeping only the 5 most recent).
   - MOVE extracted entries to `PATH: .dds/archive/changelogs/architecture/[domain_name]_history.dds.md`.
   - PREPEND a pointer link in the current file: `> [Archived logs moved to: archive/changelogs/...]`.

## [5] PRE-FLIGHT_SELF_CORRECTION

BEFORE releasing the lock, EXECUTOR MUST self-audit the modified chunks.

**VALIDATION_STEPS:**

1. **Feature Logic Leakage:** Did I accidentally introduce feature-specific logic (e.g., "how the login button works") into this structural document? -> IF YES, abstract it to pure boundaries and data shapes.
2. **Type Strictness:** Are the newly added database columns using exact data types (e.g., `VARCHAR(50)`, `BOOLEAN`)? -> IF NO, correct them.

*Output: EXECUTOR returns `STATUS: SYNC_COMPLETE` ONLY IF locks are released, Upward Checks pass, and Downward Tasks (if any) are created.*

# END_OF_DIRECTIVE
