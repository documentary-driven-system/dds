---
id: dds_writing_guide
version: 1.1.0
type: system_directive
dependencies: [meta/dds-core-manifesto.dds.md]
priority: high
last_updated: 2026-04-11
description: Machine-readable routing, indexing, folderization, and modularization rules for DDS documents.
---

# SYSTEM_DIRECTIVE: WRITING_ROUTING_AND_MODULARIZATION_PROTOCOL

## [0] DEFINITION & SCOPE
This document instructs the EXECUTOR (Documentation Architect AI / Human) on how to categorize, folderize, modularize, format, and index a NEW document within the DDS. 
EXECUTOR MUST process operations sequentially: ROUTE -> FOLDERIZE/MODULARIZE -> FORMAT -> INDEX.

## [1] DIRECTORY_ROUTING & FOLDERIZATION_LOGIC
EXECUTOR MUST evaluate the `input_context` against the `ROUTING_MATRIX` and assign the correct `TARGET_PATH`. 

**ROUTING_MATRIX:**
IF `input_context` CONTAINS (business goals OR target audience OR user stories OR revenue models)
   `BASE_PATH` = `.1dc/product/`
ELSE IF `input_context` CONTAINS (database schemas OR global tech stack OR security protocols OR folder structures)
   `BASE_PATH` = `.1dc/architecture/`
ELSE IF `input_context` CONTAINS (a specific application feature OR a distinct logical module OR UI components tied to an action)
   `BASE_PATH` = `.1dc/modules/`

**FOLDERIZATION_CONSTRAINT (STRICT):**
EXECUTOR MUST NOT place feature documents directly into `BASE_PATH`. 
Every distinct domain MUST have its own sub-directory.
`TARGET_PATH` = `[BASE_PATH]/[domain_name]/` 
*(Example: A document about 'User Login' MUST be placed in `.1dc/modules/auth/` NOT `.1dc/modules/`)*

## [2] MODULARIZATION_PROTOCOL (FOR COMPLEX DOMAINS)
IF a domain (e.g., `auth`) contains extensive details, multiple sub-features, or exceeds the optimal LLM context chunk limit, EXECUTOR MUST NOT write a single monolithic file. EXECUTOR MUST apply the `SPLIT_ROUTINE`.

**SPLIT_ROUTINE:**
1. CREATE dedicated sub-folder: `[BASE_PATH]/[domain_name]/`
2. SPLIT context into isolated `.dds.md` files based on logical separation.
   *(Example: `modules/auth/login.dds.md`, `modules/auth/oauth.dds.md`, `modules/auth/jwt-strategy.dds.md`)*
3. CREATE a local `tree.dds.md` for that specific sub-folder to index its internal files.

## [3] FILE_STRUCTURE_TEMPLATE
Every `.dds.md` file MUST adhere strictly to the following template.
EXECUTOR MUST NOT omit the YAML frontmatter.

**MANDATORY_TEMPLATE:**
```markdown
---
id: [domain_name]-[feature_name]
type: [product | architecture | module]
dependencies: [relative_paths_to_related_dds_files]
last_updated: [YYYY-MM-DD]
status: active
---

# [Module or Feature Name]

## 1. Context & Purpose
- [1-2 sentences defining what this is and WHY it exists.]

## 2. Constraints & Business Rules
- [Strict rule 1]
- [Strict rule 2]

## 3. Technical Implementation Details
- [Data structures, state management, abstract logic. NO RAW SOURCE CODE unless critical for algorithm demonstration.]
```

## [4] LINGUISTIC_STANDARDS (SYNTAX)
EXECUTOR MUST generate content using these constraints to optimize for LLM Context Windows:
- FORBIDDEN: Conversational filler, metaphors, passive voice.
- REQUIRED: Imperative verbs, absolute statements (e.g., "System MUST...", "Module handles X").
- REQUIRED: Use bulleted lists and Markdown headers (`##`, `###`) to create semantic chunks for precise RAG retrieval.

## [5] HIERARCHICAL_TREE_INDEXING (CRITICAL)
Whenever a NEW file or folder is created, EXECUTOR MUST update the index trees to prevent "orphaned" knowledge.

**INDEX_UPDATE_ROUTINE:**
IF a new file is added to an existing sub-folder:
   1. OPEN local tree: `[TARGET_PATH]/[domain_name].tree.dds.md`
   2. APPEND file path and description.
IF a new sub-folder is created:
   1. CREATE local tree: `[TARGET_PATH]/[domain_name].tree.dds.md`
   2. OPEN parent tree: `[BASE_PATH]/[BASE_PATH_NAME].tree.dds.md`
   3. APPEND pointer to the new sub-folder's tree.

*Failure to execute `INDEX_UPDATE_ROUTINE` results in a fatal memory leak. EXECUTOR MUST verify tree chains before task completion.*

# END_OF_DIRECTIVE