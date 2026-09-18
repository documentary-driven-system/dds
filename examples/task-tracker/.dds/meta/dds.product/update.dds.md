---
id: meta-product-update
type: meta
status: active
dependencies: [meta-product-rules, meta-product-write]
last_updated: 2026-09-18
description: Machine-readable protocol for atomic business logic updates, downward impact analysis, and a capped changelog.
---

# SYSTEM_DIRECTIVE: PRODUCT_UPDATE_AND_SYNC_PROTOCOL

## [0] DEFINITION & SCOPE

This document defines the strict lifecycle for modifying existing `.dds.md` files within the `.dds/product/` directory.
Because the `product` tier sits at the top of the Truth Hierarchy, updates here cascade downward. EXECUTOR (AI Agent or Human) MUST execute these steps with extreme precision.

## [1] CONCURRENCY_CONTROL (LOCKING_PROTOCOL)

Before reading or writing strategic content, EXECUTOR MUST secure the target file.

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

EXECUTOR is FORBIDDEN from rewriting the entire product document just to change one metric.

**MUTATION_CONSTRAINTS:**

- EXECUTOR MUST locate the exact Markdown header (`##` or `###`) corresponding to the changed KPI, Persona, or User Story.
- EXECUTOR MUST perform a localized `diff` update ONLY on that specific chunk.
- EXECUTOR MUST strictly apply the `STRATEGIC_LINGUISTICS` (Tech-Agnosticism, chunk-local referents) defined in `.dds/meta/dds.product/write.dds.md`.

## [3] DOWNWARD_IMPACT_ASSESSMENT (CASCADE EFFECT) - CRITICAL

A change in business logic MUST reflect in the underlying technical tiers. EXECUTOR MUST NOT consider the update complete until the impact is evaluated.

**ASSESSMENT_ROUTINE:**

1. **Evaluate Architecture:** Does the new business requirement (e.g., "Support 1 million concurrent users") require a change in data models, infrastructure, or global APIs?
   -> IF YES: EXECUTOR MUST route a task to update the relevant `.dds/architecture/` documents.
2. **Evaluate Modules:** Does the new User Story or Acceptance Criteria change how a specific UI component or backend function behaves?
   -> IF YES: EXECUTOR MUST route a task to update the relevant `.dds/modules/` documents.

## [4] METADATA_AND_CHANGELOG_MUTATION (CHANGELOG CAP)

Every strategic pivot MUST leave an audit trail, optimized for LLM Context Windows.

**ACTION 1: Frontmatter Restoration:**

- UPDATE `last_updated: [YYYY-MM-DD]` to the current execution date.
- RUN `python .dds/meta/scripts/dds.py unlock <target_file>` (removes `locked_by` and `locked_at`). Manual fallback: delete both fields.

**ACTION 2: Log Append (Capped):**

1. LOCATE `## Changelog` at the bottom of the file (Create it if missing).
2. APPEND new entry: `- [YYYY-MM-DD]: [Brief description of the strategy/KPI change].`
3. IF the Changelog now holds MORE THAN 10 entries, REMOVE the oldest entries until 10 remain. Removed entries stay available through `git log -- <file>`; `dds.py check` warns above 10.

## [5] PRE-FLIGHT_SELF_CORRECTION

BEFORE releasing the lock, EXECUTOR MUST self-audit the modified chunks.

**VALIDATION_STEPS:**

1. Did I accidentally introduce technical jargon (e.g., API, SQL, React) into the business document? -> IF YES, abstract it.
2. Did I successfully document the "Why" behind the change in the Changelog? -> IF NO, add the business justification.

**FINAL_CHECK:** RUN `python .dds/meta/scripts/dds.py check` after the lock is released ([4] ACTION 1). IF it fails, fix the reported errors before reporting `SYNC_COMPLETE`.

*Output: EXECUTOR returns `STATUS: SYNC_COMPLETE` ONLY IF locks are released and Downward Impact Tasks (if any) are created.*

# END_OF_DIRECTIVE
