---
id: dds_product_deprecation_protocol
version: 1.1.0
type: operational_directive
dependencies: [meta/dds.product/rules.dds.md]
priority: high
last_updated: 2026-04-12
description: Machine-readable protocol for deprecating business logic, triggering downward cascade destruction, and executing Tombstone pruning.
---

# SYSTEM_DIRECTIVE: PRODUCT_DEPRECATION_AND_PRUNING_PROTOCOL

## [0] DEFINITION & SCOPE

This document instructs the EXECUTOR (AI Agent or Human) on EXACTLY how to safely remove a business requirement, Persona, or Epic from the `.dds/product/` domain.
Because `product` is the absolute top of the Truth Hierarchy, removing a document here MUST trigger a cascade effect to clean up now-obsolete architecture and code documentation. EXECUTOR MUST NEVER perform a standard physical `delete` operation.

## [1] DOWNWARD_CASCADE_EXECUTION (PRE-FLIGHT IMPACT)

Unlike the `modules` tier, which halts if dependencies exist, a business decision to deprecate MUST be obeyed. However, EXECUTOR MUST NOT leave orphaned technical documents behind.

**CASCADE_ROUTINE:**

1. READ the target file's `id` from its frontmatter.
2. SEARCH the entire `.dds/` directory (specifically `architecture/` and `modules/`) for any file containing this `id` in its `dependencies: []` array.
3. IF dependent files exist in lower tiers:
   - EXECUTOR MUST create a mandatory execution checklist.
   - EXECUTOR MUST route tasks to apply the respective `deprecate.dds.md` protocols to those identified lower-tier documents.
   - *Logic: If the business no longer requires a feature, the technical implementation of that feature is now technical debt and MUST be archived.*

## [2] MUTATION_AND_RELOCATION_PROTOCOL

EXECUTOR MUST preserve the historical context of the abandoned business strategy.

**EXECUTION_STEPS:**

1. OPEN target `.dds.md` file.
2. MUTATE frontmatter: `status: deprecated`.
3. APPEND frontmatter: `deprecated_date: [YYYY-MM-DD]`.
4. APPEND frontmatter: `original_path: [current_relative_path]`.
5. PREPEND to the file content (Line 1): `> ⚠️ DEPRECATED: This business requirement/epic was abandoned on [Date].`
6. MOVE the file to `PATH: .dds/archive/product/[epic_or_global_name]/[file_name]`.

## [3] RECURSIVE_TREE_PRUNING_ROUTINE (TOMBSTONE PROTOCOL)

To prevent hallucinations where AI Agents or stakeholders search for abandoned business logic without understanding why it is missing, EXECUTOR MUST leave a "Tombstone".

**PRUNING_STEPS:**

1. OPEN the deepest local index tree where the file resides.
2. LOCATE the line referencing the deprecated file.
3. **TOMBSTONE MUTATION:** DO NOT delete the line. Overwrite it using this exact syntax:
   `- [DEPRECATED -> .dds/archive/product/[folder_name]/[file_name]] [Original Business Strategy] has been abandoned.`
4. IF ALL entries in a local tree become Tombstones (i.e., an entire Epic is canceled):
   - DO NOT delete the local tree.
   - OPEN the parent tree one level up (`product.tree.dds.md`).
   - MUTATE the pointer to the local epic tree into a Tombstone: `- [DEPRECATED -> [local_tree_path]] This entire Epic has been canceled.`

*Failure to execute the `CASCADE_ROUTINE` and leave Tombstones results in massive technical debt and memory leaks. EXECUTOR MUST verify cascade integrity before task completion.*

# END_OF_DIRECTIVE
