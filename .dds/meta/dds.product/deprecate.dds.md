---
id: meta-product-deprecate
type: meta
status: active
dependencies: [meta-product-rules]
last_updated: 2026-09-18
description: Machine-readable protocol for deprecating business logic, triggering the downward cascade, and executing Tombstone pruning.
---

# SYSTEM_DIRECTIVE: PRODUCT_DEPRECATION_AND_PRUNING_PROTOCOL

## [0] DEFINITION & SCOPE

This document instructs the EXECUTOR (AI Agent or Human) on EXACTLY how to safely remove a business requirement, Persona, or Epic from the `.dds/product/` domain.
Because `product` is the top of the Truth Hierarchy, removing a document here MUST trigger a cascade effect to clean up now-obsolete architecture and code documentation. EXECUTOR MUST NEVER perform a standard physical `delete` operation.

## [1] DOWNWARD_CASCADE_EXECUTION (PRE-FLIGHT IMPACT)

Unlike the `modules` tier, which halts if dependencies exist, a business decision to deprecate MUST be obeyed. However, EXECUTOR MUST NOT leave orphaned technical documents behind.

**CASCADE_ROUTINE:**

1. READ the target file's `id` from its frontmatter.
2. RUN `python .dds/meta/scripts/dds.py impact <id> --down` to compute the **cascade set**: every `architecture` and `module` document that depends on this id, directly or transitively. Manual fallback: follow `dependencies:` lists across `.dds/` (excluding `archive/`) until no new document appears.
3. IF the cascade set is not empty:
   - EXECUTOR MUST create a mandatory execution checklist containing every document in the cascade set.
   - EXECUTOR MUST apply the respective `deprecate.dds.md` protocols to those documents in `CASCADE_MODE` (members of the same cascade set, and this origin document, do not block them).
4. **EXECUTION ORDER:** the decision flows top-down, the execution runs LEAVES-FIRST: retire `modules` members first, then `architecture` members, and mutate this origin document LAST ([2]). No `active` document may depend on a `deprecated` id at any point (`schema.dds.md` [3]).
   - *Logic: If the business no longer requires a feature, the technical implementation of that feature is now technical debt and MUST be archived.*

## [2] MUTATION_AND_RELOCATION_PROTOCOL

EXECUTOR MUST preserve the historical context of the abandoned business strategy.

**EXECUTION_STEPS:**

1. OPEN target `.dds.md` file.
2. MUTATE frontmatter: `status: deprecated`.
3. APPEND frontmatter: `deprecated_date: [YYYY-MM-DD]`.
4. APPEND frontmatter: `original_path: [current_relative_path]`.
5. INSERT immediately after the frontmatter block: `> ⚠️ DEPRECATED: This business requirement/epic was abandoned on [Date].`
6. MOVE the file to `PATH: .dds/archive/product/[epic_or_global_name]/[file_name]`.

## [3] RECURSIVE_TREE_PRUNING_ROUTINE (TOMBSTONE PROTOCOL)

To prevent Dangling References, where an executor or stakeholder searches for abandoned business logic without understanding why it is missing, EXECUTOR MUST leave a "Tombstone".

**PRUNING_STEPS:**

1. OPEN the deepest local index tree where the file resides.
2. LOCATE the line referencing the deprecated file.
3. **TOMBSTONE MUTATION:** DO NOT delete the line. Overwrite it using this exact syntax:
   `- [DEPRECATED -> .dds/archive/product/[folder_name]/[file_name]]: [Original Business Strategy] has been abandoned.`
4. IF ALL entries in a local tree become Tombstones (i.e., an entire Epic is canceled):
   - DO NOT delete the local tree.
   - OPEN the parent tree one level up (`product.tree.dds.md`).
   - MUTATE the pointer to the local epic tree into a Tombstone: `- [DEPRECATED -> [local_tree_path]]: This entire Epic has been canceled.`

*Failure to execute the `CASCADE_ROUTINE` and leave Tombstones results in orphaned technical documents and Dangling References. EXECUTOR MUST verify cascade integrity before task completion.*

**FINAL_CHECK:** After the whole cascade has completed and the Tombstones are written, RUN `python .dds/meta/scripts/dds.py check`. IF it fails, fix the reported errors before reporting completion.
`check` is EXPECTED to fail mid-cascade (a member already archived while a document that depends on it is still `active`); that failure enforces the leaves-first order. Run it only after the origin document has been mutated in [2]. NEVER un-deprecate a member to silence an intermediate failure.

# END_OF_DIRECTIVE
