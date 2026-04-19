---
id: dds_modules_update_protocol
version: 1.4.0
type: operational_directive
dependencies: [meta/dds.modules/rules.dds.md, meta/dds.modules/write.dds.md]
priority: high
last_updated: 2026-04-12
description: Machine-readable protocol for atomic updates, concurrency locking with 40-minute timeout, reverse-documentation, and log rotation.
---

# SYSTEM_DIRECTIVE: MODULES_UPDATE_AND_SYNC_PROTOCOL

## [0] DEFINITION & SCOPE

This document defines the strict lifecycle for modifying existing `.dds.md` files within the `.dds/modules/` directory.
EXECUTOR (AI Agent or Human) MUST adhere to the `CONCURRENCY_CONTROL` and `ATOMIC_UPDATE` sequences to prevent race conditions, deadlocks, and context destruction.

## [1] CONCURRENCY_CONTROL (LOCKING_PROTOCOL)

Before reading or writing content, EXECUTOR MUST secure the target file to prevent multiple agents from modifying it simultaneously.

**LOCK_ACQUISITION_ROUTINE:**

1. READ `status` field in the target file's YAML frontmatter.
2. IF `status` CONTAINS `locked_by_`, THEN EXECUTOR MUST ABORT operation and retry after a delay (Exponential Backoff).
3. IF `status` == `active`, THEN EXECUTOR MUST immediately overwrite it to `status: locked_by_[executor_id]`.
4. **LOCK_TIMEOUT_OVERRIDE:** IF `status` is locked, BUT the lock has been active for MORE THAN 40 MINUTES (indicating a crashed executor or disconnected agent), EXECUTOR MAY forcefully overwrite the status to `locked_by_[new_executor_id]`.

## [2] ATOMIC_READ_BEFORE_WRITE_PROTOCOL

EXECUTOR is FORBIDDEN from performing full-file overwrites (blind replacement).

**MUTATION_CONSTRAINTS:**

- EXECUTOR MUST locate the specific Markdown header (`##` or `###`) related to the specific code/logic change.
- EXECUTOR MUST perform a localized `diff` update (Atomic Update) ONLY on the relevant semantic chunk.
- EXECUTOR MUST NOT delete historical constraints unless they actively contradict the new codebase logic.

## [3] REVERSE_DOCUMENTATION_ROUTINE (CODE TO ABSTRACTION)

When codebase changes dictate documentation updates, EXECUTOR MUST translate implementation details into abstract business/technical rules.

**TRANSLATION_RULES:**

- BAD: "Added `if (user.age < 18) return false` to `auth.ts`."
- GOOD: "System MUST block authentication for users under 18 years old."

**LINGUISTIC_DEPENDENCY:**
EXECUTOR MUST strictly apply the `RAG_OPTIMIZED_LINGUISTICS` (Pronoun Ban, Context-Bearing Headers) defined in `.dds/meta/dds.modules/write.dds.md`.

## [4] METADATA_AND_CHANGELOG_MUTATION (WITH LOG ROTATION)

Every modification MUST leave an audit trail, but MUST NOT overflow the LLM Context Window.

**ACTION 1: Frontmatter Restoration:**

- UPDATE `last_updated: [YYYY-MM-DD]` to the current execution date.
- MUTATE `status` back to `active` (Releasing the lock acquired in Step 1).

**ACTION 2: Log Append & Rotation (Context Optimization):**

1. LOCATE `## Changelog` at the bottom of the file (Create it if missing).
2. APPEND new entry: `- [YYYY-MM-DD]: [Brief description of the logic change].`
3. COUNT total entries in the Changelog.
4. IF total entries > 10:
   - EXTRACT the oldest entries (keeping only the 5 most recent).
   - MOVE extracted entries to `PATH: .dds/archive/changelogs/[domain_name]/[file_name]_history.dds.md`.
   - PREPEND a pointer link in the current file: `> [Archived logs moved to: archive/changelogs/...]`.

## [5] CROSS_DOMAIN_INTEGRITY_GATE

Before concluding the update, EXECUTOR MUST verify if the module logic change impacts higher-level architecture.

**INTEGRITY_CHECK:**
IF the module update alters a Database Schema requirement or a Global API Contract:

- EXECUTOR MUST apply the `CONCURRENCY_CONTROL` protocol to the relevant file in `.dds/architecture/` and update it accordingly to maintain the Truth Hierarchy.

*Output: EXECUTOR returns `STATUS: SYNC_COMPLETE` ONLY IF all locks are released and cross-domain dependencies are resolved.*

# END_OF_DIRECTIVE