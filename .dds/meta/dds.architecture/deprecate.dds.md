---
id: dds_architecture_deprecation_protocol
version: 1.0.0
type: operational_directive
dependencies: [meta/dds.architecture/rules.dds.md]
priority: high
last_updated: 2026-04-12
description: Machine-readable protocol for deprecating infrastructure, executing upward validation, downward cascade destruction, and Tombstone pruning.
---

# SYSTEM_DIRECTIVE: ARCHITECTURE_DEPRECATION_AND_PRUNING_PROTOCOL

## [0] DEFINITION & SCOPE

This document instructs the EXECUTOR (System Architect, DevOps, or AI Agent) on EXACTLY how to safely remove a database schema, service, or global API contract from the `.dds/architecture/` domain.
Because `architecture` is the middle of the Truth Hierarchy, removing a document here requires UPWARD validation and triggers DOWNWARD cascade destruction. EXECUTOR MUST NEVER perform a standard physical `delete` operation.

## [1] THE TWO-WAY_DEPRECATION_GATE (PRE-FLIGHT CHECK)

Before archiving any architectural document, EXECUTOR MUST verify its standing in the Truth Hierarchy.

**STEP 1: UPWARD_VALIDATION (Product Check):**

1. SEARCH the `.dds/product/` directory to see if any active Epic or Business Requirement depends on this architectural element (e.g., Does a KPI require the data stored in this table?).
2. IF an active Product requirement exists:
   - EXECUTOR MUST HALT the deprecation. Architecture CANNOT overrule Product.
   - EXECUTOR MUST report: `STATUS: BLOCKED. Infrastructure is mandated by [Product_Document_Link]. Deprecate the business rule first.`

**STEP 2: DOWNWARD_CASCADE (Modules Execution):**

1. IF Upward Validation passes (i.e., the business no longer needs this infrastructure), SEARCH the `.dds/modules/` directory for any code modules depending on it.
2. IF dependent modules exist:
   - EXECUTOR MUST route tasks to apply the `deprecate.dds.md` or `update.dds.md` protocols to those lower-tier documents to remove the obsolete code logic.

## [2] MUTATION_AND_RELOCATION_PROTOCOL

EXECUTOR MUST preserve the historical context of the retired infrastructure.

**EXECUTION_STEPS:**

1. OPEN target `.dds.md` file.
2. MUTATE frontmatter: `status: deprecated`.
3. APPEND frontmatter: `deprecated_date: [YYYY-MM-DD]`.
4. APPEND frontmatter: `original_path: [current_relative_path]`.
5. PREPEND to the file content (Line 1): `> ⚠️ DEPRECATED: This database schema / infrastructure was retired on [Date].`
6. MOVE the file to `PATH: .dds/archive/architecture/[domain_name]/[file_name]`.

## [3] RECURSIVE_TREE_PRUNING_ROUTINE (TOMBSTONE PROTOCOL)

To prevent AI Agents from hallucinating about missing data models or APIs, EXECUTOR MUST leave a "Tombstone" in the architectural index.

**PRUNING_STEPS:**

1. OPEN the deepest local index tree where the file resides.
2. LOCATE the line referencing the deprecated file.
3. **TOMBSTONE MUTATION:** DO NOT delete the line. Overwrite it using this exact syntax:
   `- [DEPRECATED -> .dds/archive/architecture/[folder_name]/[file_name]] [Original Schema/Service] has been retired.`
4. IF ALL entries in a local tree become Tombstones (e.g., an entire microservice is shut down):
   - DO NOT delete the local tree.
   - OPEN the parent tree one level up (`architecture.tree.dds.md`).
   - MUTATE the pointer to the local tree into a Tombstone: `- [DEPRECATED -> [local_tree_path]] This entire service domain has been retired.`

*Failure to execute the Two-Way Gate and leave Tombstones results in database inconsistencies and memory leaks. EXECUTOR MUST verify cascade integrity before task completion.*

# END_OF_DIRECTIVE
