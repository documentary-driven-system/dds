---
id: dds_product_update_protocol
version: 1.0.0
type: operational_directive
dependencies: [meta/dds.product/rules.dds.md, meta/dds.product/write.dds.md]
priority: high
last_updated: 2026-04-12
description: Machine-readable protocol for atomic business logic updates, downward impact analysis, and strategic log rotation.
---

# SYSTEM_DIRECTIVE: PRODUCT_UPDATE_AND_SYNC_PROTOCOL

## [0] DEFINITION & SCOPE

This document defines the strict lifecycle for modifying existing `.dds.md` files within the `.dds/product/` directory.
Because the `product` tier sits at the absolute top of the Truth Hierarchy, updates here have massive cascading effects. EXECUTOR (AI Agent or Human) MUST execute these steps with extreme precision.

## [1] CONCURRENCY_CONTROL (LOCKING_PROTOCOL)

Before reading or writing strategic content, EXECUTOR MUST secure the target file.

**LOCK_ACQUISITION_ROUTINE:**

1. READ `status` field in the target file's YAML frontmatter.
2. IF `status` CONTAINS `locked_by_`, THEN EXECUTOR MUST ABORT operation and retry after a delay (Exponential Backoff).
3. IF `status` == `active`, THEN EXECUTOR MUST immediately overwrite it to `status: locked_by_[executor_id]`.
4. **LOCK_TIMEOUT_OVERRIDE:** IF `status` is locked, BUT the lock has been active for MORE THAN 40 MINUTES, EXECUTOR MAY forcefully overwrite the status to `locked_by_[new_executor_id]`.

## [2] ATOMIC_MUTATION_PROTOCOL

EXECUTOR is FORBIDDEN from rewriting the entire product document just to change one metric.

**MUTATION_CONSTRAINTS:**

- EXECUTOR MUST locate the exact Markdown header (`##` or `###`) corresponding to the changed KPI, Persona, or User Story.
- EXECUTOR MUST perform a localized `diff` update ONLY on that specific chunk.
- EXECUTOR MUST strictly apply the `STRATEGIC_LINGUISTICS` (Tech-Agnosticism, Pronoun Ban) defined in `.dds/meta/dds.product/write.dds.md`.

## [3] DOWNWARD_IMPACT_ASSESSMENT (CASCADE EFFECT) - CRITICAL

A change in business logic MUST reflect in the underlying technical tiers. EXECUTOR MUST NOT consider the update complete until the impact is evaluated.

**ASSESSMENT_ROUTINE:**

1. **Evaluate Architecture:** Does the new business requirement (e.g., "Support 1 million concurrent users") require a change in data models, infrastructure, or global APIs?
   -> IF YES: EXECUTOR MUST route a task to update the relevant `.dds/architecture/` documents.
2. **Evaluate Modules:** Does the new User Story or Acceptance Criteria change how a specific UI component or backend function behaves?
   -> IF YES: EXECUTOR MUST route a task to update the relevant `.dds/modules/` documents.

## [4] METADATA_AND_CHANGELOG_MUTATION (LOG ROTATION)

Every strategic pivot MUST leave an audit trail, optimized for LLM Context Windows.

**ACTION 1: Frontmatter Restoration:**

- UPDATE `last_updated: [YYYY-MM-DD]` to the current execution date.
- MUTATE `status` back to `active` (Releasing the lock).

**ACTION 2: Log Append & Rotation:**

1. LOCATE `## Changelog` at the bottom of the file (Create it if missing).
2. APPEND new entry: `- [YYYY-MM-DD]: [Brief description of the strategy/KPI change].`
3. COUNT total entries in the Changelog.
4. IF total entries > 10:
   - EXTRACT the oldest entries (keeping only the 5 most recent).
   - MOVE extracted entries to `PATH: .dds/archive/changelogs/product/[epic_name]_history.dds.md`.
   - PREPEND a pointer link in the current file: `> [Archived logs moved to: archive/changelogs/...]`.

## [5] PRE-FLIGHT_SELF_CORRECTION

BEFORE releasing the lock, EXECUTOR MUST self-audit the modified chunks.

**VALIDATION_STEPS:**

1. Did I accidentally introduce technical jargon (e.g., API, SQL, React) into the business document? -> IF YES, abstract it.
2. Did I successfully document the "Why" behind the change in the Changelog? -> IF NO, add the business justification.

*Output: EXECUTOR returns `STATUS: SYNC_COMPLETE` ONLY IF locks are released and Downward Impact Tasks (if any) are created.*

# END_OF_DIRECTIVE
