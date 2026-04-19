---
id: dds_update_guide
version: 1.1.0
type: system_directive
dependencies: [meta/dds-core-manifesto.dds.md, meta/dds-writing-guide.dds.md]
priority: high
last_updated: 2026-04-11
description: Machine-readable protocols for modifying, syncing, validating, locking, and log-rotating existing DDS documents.
---

# SYSTEM_DIRECTIVE: UPDATE_AND_SYNC_PROTOCOL

## [0] DEFINITION & SCOPE
This document defines the strict lifecycle for modifying existing `.dds.md` files. 
EXECUTOR (Coder AI / Prompt Engineer / Human) MUST adhere to the `CONCURRENCY_CONTROL` and `READ_BEFORE_WRITE` sequences to prevent race conditions and context hallucination.

## [1] THE_UPDATE_LIFECYCLE
For any system change triggering `SYNC_STATUS = REQUIRED`, EXECUTOR MUST complete the following sequential pipeline:

1. `ACQUIRE_LOCK`: Check and claim target `.dds.md` files to prevent concurrent edits.
2. `EVALUATE_IMPACT`: Identify all cross-domain `.dds.md` files affected.
3. `EXECUTE_READ`: Load the current state of the locked files.
4. `EXECUTE_MUTATE`: Apply ATOMIC changes to specific semantic chunks.
5. `UPDATE_METADATA_AND_LOGS`: Mutate timestamps, rotate logs, and restore lock status.
6. `VALIDATE_SYNC`: Confirm Cross-Domain Integrity.

## [2] CONCURRENCY_CONTROL (LOCKING_PROTOCOL)
Before executing any reading or writing of the core content, EXECUTOR MUST secure the file.

**LOCK_ACQUISITION_ROUTINE:**
1. READ `status` field in the target file's YAML frontmatter.
2. IF `status` CONTAINS `locked_by_`, THEN EXECUTOR MUST ABORT operation and retry after a delay.
3. IF `status` == `active`, THEN EXECUTOR MUST immediately overwrite it to `status: locked_by_[executor_id]`.

## [3] READ_BEFORE_WRITE_PROTOCOL
EXECUTOR is FORBIDDEN from performing full-file overwrites (blind replacement).

**MUTATION_CONSTRAINTS:**
- EXECUTOR MUST locate the specific Markdown header (`##` or `###`) related to the change.
- EXECUTOR MUST perform a localized `diff` update (Atomic Update).
- EXECUTOR MUST NOT delete historical constraints unless they actively contradict the new logic.

## [4] REVERSE_DOCUMENTATION_ROUTINE
When code changes dictate documentation updates (Code -> Docs), EXECUTOR MUST translate implementation details into abstract rules.

**TRANSLATION_RULES:**
- BAD: "Added `if (user.age < 18) return false` to `auth.ts`."
- GOOD: "System MUST block authentication for users under 18 years old."

**SYNTAX_AND_FORMAT_DEPENDENCY:**
EXECUTOR MUST strictly follow the `LINGUISTIC_STANDARDS` defined in `meta/dds-writing-guide.dds.md`.

## [5] METADATA_AND_CHANGELOG_MUTATION (WITH LOG ROTATION)
Every modification MUST leave an audit trail, but MUST NOT overflow the Context Window.

**ACTION 1: Frontmatter Restoration**
- UPDATE `last_updated: [YYYY-MM-DD]` to current execution date.
- MUTATE `status` back to `active` (Releasing the lock acquired in Step 2).

**ACTION 2: Log Append & Rotation (Context Optimization)**
1. LOCATE `## Changelog` at the bottom of the file.
2. APPEND new entry: `- [YYYY-MM-DD]: [Brief description of change].`
3. COUNT total entries in the Changelog.
4. IF total entries > 10 (THRESHOLD_EXCEEDED):
   - EXTRACT the oldest entries (keeping only the 5 most recent).
   - MOVE extracted entries to `PATH: .1dc/archive/changelogs/[unique_doc_id]_history.dds.md`.
   - PREPEND a pointer link in the current file: `> [Archived logs moved to: archive/changelogs/...]`.

## [6] CROSS_DOMAIN_COMMIT_GATE (PRE-FLIGHT CHECK)
Before authorizing a VCS/Git Commit, EXECUTOR MUST run the `INTEGRITY_CHECK`.

**INTEGRITY_CHECK_ROUTINE:**
IF the update modifies a shared data model (e.g., Database Schema):
   1. Did EXECUTOR lock and update `architecture/data-models.dds.md`? -> IF NO, BLOCK COMMIT.
   2. Did EXECUTOR lock and update the corresponding `modules/[domain_name].dds.md`? -> IF NO, BLOCK COMMIT.
   3. Are `status` fields reverted to `active` on ALL affected files? -> IF NO, BLOCK COMMIT.

*Output: EXECUTOR returns `STATUS: SYNC_COMPLETE` only if all dependencies are mutually resolved and locks are released.*

# END_OF_DIRECTIVE