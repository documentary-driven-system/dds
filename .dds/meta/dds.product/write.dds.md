---
id: dds_product_write_protocol
version: 1.0.0
type: operational_directive
dependencies: [meta/dds.product/rules.dds.md]
priority: high
last_updated: 2026-04-12
description: RAG-optimized protocol for formatting, structuring, and indexing business requirements, user stories, and product epics.
---

# SYSTEM_DIRECTIVE: PRODUCT_WRITE_AND_INDEX_PROTOCOL

## [0] DEFINITION & SCOPE

This document instructs the EXECUTOR (AI Agent or Human) on EXACTLY how to create, format, and index a NEW document within the `.dds/product/` domain.
EXECUTOR MUST process operations sequentially: FOLDERIZE -> FORMAT (RAG-OPTIMIZED) -> RECURSIVE_INDEX -> PRE-FLIGHT_SELF_CORRECTION.

## [1] FLEXIBLE_FOLDERIZATION_PROTOCOL

Unlike the `modules` tier, the `product` tier supports both Global and Epic-specific documents.

1. **GLOBAL_DOCUMENTS:** High-level strategic files (e.g., `vision.dds.md`, `target-audience.dds.md`) MAY be placed directly in the root `.dds/product/` directory.
2. **EPIC_DOCUMENTS:** Specific business features or user journeys MUST be isolated in sub-directories.
   `TARGET_PATH` = `.dds/product/epics/[epic_name]/` (e.g., `product/epics/user-onboarding/`)
3. FILE_NAME = `[kebab-case-name].dds.md`

## [2] STRATEGIC_LINGUISTICS (MACHINE PERCEPTION)

To ensure semantic chunks retain absolute meaning without confusing the AI with implementation details, EXECUTOR MUST adhere to these STRICT rules:

1. **TECHNOLOGY_AGNOSTICISM (ABSOLUTE):** EXECUTOR MUST NOT mention specific coding languages, database types (e.g., SQL, MongoDB), or libraries (e.g., React, Tailwind). Use business terms: "Data Storage", "User Interface".
2. **THE PRONOUN BAN:** EXECUTOR MUST NEVER use vague pronouns ("It", "This", "They"). Always explicitly name the Persona or Feature.
3. **CONTEXT-BEARING HEADERS:** Headers MUST encapsulate the business context (e.g., `### [B2B_Dashboard] Success Metrics`).
4. **HEADER DEPTH LIMIT:** MAX H3 (`###`). Use bolding or bullet points for deeper hierarchies.

## [3] MANDATORY_STRUCTURED_TEMPLATE

Every new `.dds.md` file in the `product` domain MUST adhere to the following business-logic template.

**TEMPLATE:**

```markdown
---
id: product-[epic_or_global_name]
type: product
dependencies: []
last_updated: [YYYY-MM-DD]
status: active
---

# [PRODUCT/EPIC_NAME]: [TITLE]

## [0] BUSINESS_VISION_AND_VALUE
[1-2 sentences defining the ultimate business goal and the value it brings to the user or company. WHY are we building this?]

## [1] TARGET_PERSONAS
- **[Persona 1 Name]:** [Brief description of their needs and pain points].
- **[Persona 2 Name]:** [Brief description].

## [2] KEY_PERFORMANCE_INDICATORS (KPIs)
- [Metric 1]: [Target Goal - e.g., Increase user retention by 15%].
- [Metric 2]: [Target Goal].

## [3] USER_STORIES_AND_ACCEPTANCE_CRITERIA
<user_stories>
- **Story:** As a [Persona], I want to [Action], so that [Benefit].
- **Acceptance:** The system MUST allow [Outcome].
</user_stories>
```

## [4] RECURSIVE_INDEXING_ROUTINE

Whenever a NEW file or folder is created, EXECUTOR MUST update the index trees to maintain the global memory.

**INDEX_UPDATE_STEPS:**
IF a new GLOBAL document is created directly in `product/`:

   1. OPEN the main tree: `.dds/product/product.tree.dds.md`
   2. APPEND file path AND a 1-sentence strategic description.

IF a new EPIC folder/file is created:

   1. CREATE/OPEN local tree: `.dds/product/epics/[epic_name]/[epic_name].tree.dds.md`
   2. APPEND the file path and description.
   3. OPEN parent tree: `.dds/product/product.tree.dds.md`
   4. VERIFY/APPEND the pointer to the new epic tree using the syntax: `- [epics/[epic_name]/]: [1-sentence description]`
   5. VERIFY that `product.tree.dds.md` is linked in the Master Root Tree (`.dds/tree.dds.md`).

## [5] PRE-FLIGHT_SELF_CORRECTION (VALIDATION LOOP)

AFTER generating the document and BEFORE saving, EXECUTOR MUST perform a self-audit.

**VALIDATION_STEPS:**

1. **Scan for Tech-Agnosticism:** Does the text contain coding frameworks, DB schema names, or API endpoint routes? -> IF YES, rewrite into abstract business requirements.
2. **Scan for Pronouns:** Are there isolated pronouns ("It", "This")? -> IF YES, replace with exact nouns.
3. **Scan for KPIs:** Are the goals measurable? -> IF NO, refine the KPIs.

*Output: EXECUTOR returns `STATUS: VALIDATED` ONLY IF all checks pass.*

# END_OF_DIRECTIVE
