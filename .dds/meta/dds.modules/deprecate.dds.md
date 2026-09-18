---
id: meta-modules-deprecate
type: meta
status: active
dependencies: [meta-modules-rules]
last_updated: 2026-09-18
description: Machine-readable protocol for deprecating modules, Tombstone tree pruning, and handling dependencies.
---

# SYSTEM_DIRECTIVE: DEPRECATION_AND_PRUNING_PROTOCOL

## [0] DEFINITION & SCOPE

This document instructs the EXECUTOR (AI Agent or Human) on EXACTLY how to safely remove a feature/module from the `.dds/modules/` domain without breaking the system's index (Memory Leak) or causing broken references (Dangling Pointers).
EXECUTOR MUST NEVER perform a standard physical `delete` operation.

## [1] DEPENDENCY_IMPACT_ANALYSIS (PRE-FLIGHT CHECK)

Before removing any document, EXECUTOR MUST verify if other active documents rely on it.

**IMPACT_ROUTINE:**

1. READ the target file's `id` from its frontmatter.
2. RUN `python .dds/meta/scripts/dds.py impact <id>` to list every active document whose `dependencies` contains this id. Manual fallback: search `dependencies:` lines across `.dds/`, excluding `archive/`.
3. IF dependents exist AND this deprecation is NOT running in `CASCADE_MODE`:
   - EXECUTOR MUST HALT the deprecation.
   - EXECUTOR MUST report: `STATUS: BLOCKED. Target is actively depended upon by [List_of_Files]. Update those files first.`
4. IF this deprecation IS running in `CASCADE_MODE` (triggered by a `product` or `architecture` deprecation):
   - Dependents INSIDE the cascade set (the upstream `impact --down` result) are retired in the same operation and DO NOT block.
   - Dependents OUTSIDE the cascade set still block: HALT and report as in step 3.
5. IF nothing blocks, proceed to [2].

## [2] MUTATION_AND_RELOCATION_PROTOCOL

EXECUTOR MUST preserve the historical context of the removed feature.

**EXECUTION_STEPS:**

1. OPEN target `.dds.md` file.
2. MUTATE frontmatter: `status: deprecated`.
3. APPEND frontmatter: `deprecated_date: [YYYY-MM-DD]`.
4. APPEND frontmatter: `original_path: [current_relative_path]`.
5. INSERT immediately after the frontmatter block: `> ⚠️ DEPRECATED: This module was removed from the system on [Date].`
6. MOVE the file to `PATH: .dds/archive/modules/[domain_name]/[file_name]`.

## [3] RECURSIVE_TREE_PRUNING_ROUTINE (TOMBSTONE PROTOCOL)

To prevent Dangling References, where an executor searches for a deleted file without understanding why it is missing, EXECUTOR MUST NOT completely erase the file's index. EXECUTOR MUST leave a "Tombstone".

**PRUNING_STEPS:**

1. OPEN the deepest local index tree where the file resides.
2. LOCATE the line referencing the deprecated file.
3. **TOMBSTONE MUTATION:** DO NOT delete the line. Overwrite it using this exact syntax:
   `- [DEPRECATED -> .dds/archive/modules/[domain_name]/[file_name]]: [Original Feature Name] has been removed.`
4. IF ALL entries in a local tree become Tombstones (i.e., no active features remain in that domain):
   - DO NOT delete the local tree.
   - OPEN the parent tree one level up.
   - MUTATE the pointer to the local tree into a Tombstone: `- [DEPRECATED -> [local_tree_path]]: All features in this domain are deprecated.`
   - REPEAT Step 4 RECURSIVELY up to the Master Root Tree if parent domains become entirely deprecated.

*Failure to leave Tombstones results in AI Agents attempting to read files that no longer exist (404 Context Error). EXECUTOR MUST verify tombstone integrity before task completion.*

**FINAL_CHECK:** After the whole cascade has completed and the Tombstones are written, RUN `python .dds/meta/scripts/dds.py check`. IF it fails, fix the reported errors before reporting completion.
`check` is EXPECTED to fail mid-cascade (a member already archived while a document that depends on it is still `active`); that failure enforces the leaves-first order. Run it only after the origin document has been mutated in [2]. NEVER un-deprecate a member to silence an intermediate failure.

# END_OF_DIRECTIVE
