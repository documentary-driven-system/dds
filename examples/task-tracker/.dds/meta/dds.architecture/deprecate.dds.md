---
id: meta-architecture-deprecate
type: meta
status: active
dependencies: [meta-architecture-rules]
last_updated: 2026-09-18
description: Machine-readable protocol for deprecating infrastructure, executing upward validation, downward cascade, and Tombstone pruning.
---

# SYSTEM_DIRECTIVE: ARCHITECTURE_DEPRECATION_AND_PRUNING_PROTOCOL

## [0] DEFINITION & SCOPE

This document instructs the EXECUTOR (System Architect, DevOps, or AI Agent) on EXACTLY how to safely remove a database schema, service, or global API contract from the `.dds/architecture/` domain.
Because `architecture` is the middle of the Truth Hierarchy, removing a document here requires UPWARD validation and triggers a DOWNWARD cascade. EXECUTOR MUST NEVER perform a standard physical `delete` operation.

## [1] THE TWO-WAY_DEPRECATION_GATE (PRE-FLIGHT CHECK)

Before archiving any architectural document, EXECUTOR MUST verify its standing in the Truth Hierarchy.

**STEP 1: UPWARD_VALIDATION (Product Check):**

1. RUN `python .dds/meta/scripts/dds.py impact <id> --up` to list the `product` documents this architectural element serves (its own `dependencies`). Manual fallback: read the `dependencies` list in the target frontmatter and check each product document's `status`.
2. IF any listed Product document is `status: active` AND that document is NOT the origin of a `CASCADE_MODE` run (a product deprecation that listed this element in its cascade set):
   - EXECUTOR MUST HALT the deprecation. Architecture CANNOT overrule Product.
   - EXECUTOR MUST report: `STATUS: BLOCKED. Infrastructure is mandated by [Product_Document_Link]. Deprecate the business rule first.`

**STEP 2: DOWNWARD_CASCADE (Modules Execution):**

1. IF Upward Validation passes (i.e., the business no longer needs this infrastructure), RUN `python .dds/meta/scripts/dds.py impact <id> --down` to compute the **cascade set**: every `module` document depending on this id, directly or transitively.
2. IF the cascade set is not empty:
   - EXECUTOR MUST apply `dds.modules/deprecate.dds.md` in `CASCADE_MODE` (members of the cascade set do not block each other), or `dds.modules/update.dds.md` where the module survives with reduced scope, to remove the obsolete code logic.
3. **EXECUTION ORDER:** retire the cascade set LEAVES-FIRST (modules first), then mutate this architecture document ([2]). No `active` document may depend on a `deprecated` id at any point (`schema.dds.md` [3]).

## [2] MUTATION_AND_RELOCATION_PROTOCOL

EXECUTOR MUST preserve the historical context of the retired infrastructure.

**EXECUTION_STEPS:**

1. OPEN target `.dds.md` file.
2. MUTATE frontmatter: `status: deprecated`.
3. APPEND frontmatter: `deprecated_date: [YYYY-MM-DD]`.
4. APPEND frontmatter: `original_path: [current_relative_path]`.
5. INSERT immediately after the frontmatter block: `> ⚠️ DEPRECATED: This database schema / infrastructure was retired on [Date].`
6. MOVE the file to `PATH: .dds/archive/architecture/[domain_name]/[file_name]`.

## [3] RECURSIVE_TREE_PRUNING_ROUTINE (TOMBSTONE PROTOCOL)

To prevent Dangling References (an executor searching for a data model or API that no longer exists), EXECUTOR MUST leave a "Tombstone" in the architectural index.

**PRUNING_STEPS:**

1. OPEN the deepest local index tree where the file resides.
2. LOCATE the line referencing the deprecated file.
3. **TOMBSTONE MUTATION:** DO NOT delete the line. Overwrite it using this exact syntax:
   `- [DEPRECATED -> .dds/archive/architecture/[folder_name]/[file_name]]: [Original Schema/Service] has been retired.`
4. IF ALL entries in a local tree become Tombstones (e.g., an entire microservice is shut down):
   - DO NOT delete the local tree. MOVE it to the mirrored path under `.dds/archive/` (`.dds/archive/architecture/[domain_name]/[domain_name].tree.dds.md`) and mutate its frontmatter like any deprecated document (`status: deprecated`, `deprecated_date`, `original_path`, the DEPRECATED banner). Its Tombstone lines keep pointing at the archived documents.
   - OPEN the parent tree one level up (`architecture.tree.dds.md`).
   - MUTATE the pointer to the local tree into a Tombstone: `- [DEPRECATED -> .dds/archive/architecture/[domain_name]/[domain_name].tree.dds.md]: This entire service domain has been retired.`

*Failure to execute the Two-Way Gate and leave Tombstones results in orphaned module documents and Dangling References. EXECUTOR MUST verify cascade integrity before task completion.*

**FINAL_CHECK:** After the whole cascade has completed and the Tombstones are written, RUN `python .dds/meta/scripts/dds.py check`. IF it fails, fix the reported errors before reporting completion.
`check` is EXPECTED to fail mid-cascade (a member already archived while a document that depends on it is still `active`); that failure enforces the leaves-first order. Run it only after the origin document has been mutated in [2]. NEVER un-deprecate a member to silence an intermediate failure.

# END_OF_DIRECTIVE
