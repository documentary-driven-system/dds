---
id: dds_modules_deprecation_protocol
version: 1.1.0
type: operational_directive
dependencies: [meta/dds.modules/rules.dds.md]
priority: high
last_updated: 2026-04-12
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
2. SEARCH the entire `.dds/` directory for any file containing this `id` in its `dependencies: []` array.
3. IF dependent files exist:
   - EXECUTOR MUST HALT the deprecation.
   - EXECUTOR MUST report: `STATUS: BLOCKED. Target is actively depended upon by [List_of_Files]. Update those files first.`
4. IF NO dependent files exist, proceed to [2].

## [2] MUTATION_AND_RELOCATION_PROTOCOL

EXECUTOR MUST preserve the historical context of the removed feature.

**EXECUTION_STEPS:**

1. OPEN target `.dds.md` file.
2. MUTATE frontmatter: `status: deprecated`.
3. APPEND frontmatter: `deprecated_date: [YYYY-MM-DD]`.
4. APPEND frontmatter: `original_path: [current_relative_path]`.
5. PREPEND to the file content (Line 1): `> ⚠️ DEPRECATED: This module was removed from the system on [Date].`
6. MOVE the file to `PATH: .dds/archive/modules/[domain_name]/[file_name]`.

## [3] RECURSIVE_TREE_PRUNING_ROUTINE (TOMBSTONE PROTOCOL)

To prevent hallucinations (Dangling References) where AI Agents search for deleted files without understanding why they are missing, EXECUTOR MUST NOT completely erase the file's index. EXECUTOR MUST leave a "Tombstone".

**PRUNING_STEPS:**

1. OPEN the deepest local index tree where the file resides.
2. LOCATE the line referencing the deprecated file.
3. **TOMBSTONE MUTATION:** DO NOT delete the line. Overwrite it using this exact syntax:
   `- [DEPRECATED -> .dds/archive/modules/[domain_name]/[file_name]] [Original Feature Name] has been removed.`
4. IF ALL entries in a local tree become Tombstones (i.e., no active features remain in that domain):
   - DO NOT delete the local tree.
   - OPEN the parent tree one level up.
   - MUTATE the pointer to the local tree into a Tombstone: `- [DEPRECATED -> [local_tree_path]] All features in this domain are deprecated.`
   - REPEAT Step 4 RECURSIVELY up to the Master Root Tree if parent domains become entirely deprecated.

*Failure to leave Tombstones results in AI Agents attempting to read files that no longer exist (404 Context Error). EXECUTOR MUST verify tombstone integrity before task completion.*

# END_OF_DIRECTIVE