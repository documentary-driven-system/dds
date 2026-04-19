---
id: dds_core_manifesto
version: 1.0.0
type: system_directive
priority: absolute_override
last_updated: 2026-04-11
description: Machine-readable core protocol for Documentary Driven System (DDS).
---

# SYSTEM_DIRECTIVE: DDS_CORE_PROTOCOL

## [0] DEFINITION & SCOPE
This document defines the absolute operational constraints of the Documentary Driven System (DDS). 
EXECUTOR (AI Agent or Human) MUST validate all operations against these rules. DDS is the Single Source of Truth (SSoT). Code DOES NOT dictate logic; DDS dictates code.

## [1] DIRECTORY_MAPPING (.1dc/)
EXECUTOR MUST restrict all documentation files to the following paths based on CONTENT_TYPE:

- `PATH: .1dc/meta/`
  - CONTENT_TYPE: System configurations, routing logic, tree indexes, structural templates.
- `PATH: .1dc/product/`
  - CONTENT_TYPE: Business logic, user requirements (PRD), abstract goals.
- `PATH: .1dc/architecture/`
  - CONTENT_TYPE: Infrastructure, tech stack, database schemas, global API contracts.
- `PATH: .1dc/modules/`
  - CONTENT_TYPE: Feature-specific logic, isolated domain implementations.
- `PATH: .1dc/archive/`
  - CONTENT_TYPE: Deprecated or deleted documentation.

## [2] EXECUTION_RULES (THE CONSTITUTION)

### RULE_01: THRESHOLD_BASED_SYNC
Before executing ACTION: GIT_COMMIT, EXECUTOR MUST evaluate changes against the THRESHOLD_MATRIX.

**THRESHOLD_MATRIX:**
IF `changes` INCLUDE (
   Database schema modification OR
   API contract / Endpoint mutation OR
   Business logic / Calculation update OR
   Addition/Removal of a feature module
) THEN:
   `SYNC_STATUS` = REQUIRED. EXECUTOR MUST update relevant .dds.md files before commit.
ELSE IF `changes` INCLUDE ONLY (
   Cosmetic changes (UI/CSS/Colors) OR
   Refactoring without I/O mutation OR
   Typo fixes in code
) THEN:
   `SYNC_STATUS` = SKIPPED. Commit proceeds without DDS updates.

### RULE_02: MODULAR_INTEGRITY
- FORBIDDEN: 1:1 mapping of source code files to DDS files (e.g., `app.ts` -> `app.dds.md` is INVALID).
- REQUIRED: N:1 mapping based on logical features (e.g., `login.ts`, `auth.css`, `jwt.ts` -> `modules/auth.dds.md`).

### RULE_03: CROSS_DOMAIN_INTEGRITY (TRANSACTIONAL UPDATE)
IF EXECUTOR updates a feature that spans multiple domains (e.g., UI + DB), 
THEN EXECUTOR MUST perform an ATOMIC UPDATE across all impacted DDS files.
*Constraint: Partial DDS updates are invalid and cause SYSTEM_FAILURE.*

### RULE_04: TRUTH_HIERARCHY (CONFLICT RESOLUTION)
IF a contradiction exists between multiple DDS files, EXECUTOR MUST resolve it using the following strict priority:
`PRIORITY: [product/] > [architecture/] > [modules/]`
*Action: The lower-priority document MUST be overwritten to match the higher-priority document.*

### RULE_05: DEPRECATION_PROTOCOL
IF a feature is removed from the codebase, EXECUTOR MUST NOT physically delete the corresponding DDS file.
EXECUTOR MUST execute the following operation:
1. MOVE file to `PATH: .1dc/archive/`
2. MUTATE frontmatter: `status: deprecated`
3. APPEND frontmatter: `original_path: [previous_filepath]`

## [3] REFERENCE_POINTERS
For implementation details, EXECUTOR MUST retrieve secondary guidelines:
- FOR Creation/Indexing: EXECUTE_READ -> `meta/writing-guide.dds.md`
- FOR Modification/Syncing: EXECUTE_READ -> `meta/update-guide.dds.md`

# END_OF_DIRECTIVE