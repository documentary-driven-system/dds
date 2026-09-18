---
id: meta-product-rules
type: meta
status: active
dependencies: [meta-manifesto]
last_updated: 2026-09-18
description: Operational routing and strategic constraints for the Product (Business/Requirements) domain.
---

# SYSTEM_DIRECTIVE: PRODUCT_DOMAIN_DISPATCHER

## [0] DEFINITION & SCOPE

This document is the Domain Dispatcher for the `product` tier.
EXECUTOR (AI Agent or Human) has been routed here because the task involves high-level business logic, market goals, user personas, revenue models, or product requirements (PRDs).
This document dictates HOW to handle operations within the `.dds/product/` directory.

## [1] DOMAIN_SPECIFIC_CONSTRAINTS (THE IRON LAWS OF PRODUCT)

Before taking any action, EXECUTOR MUST acknowledge the following constraints specific to the `product` domain:

1. **TECHNOLOGY_AGNOSTICISM:**
   EXECUTOR MUST NOT include technical implementation details (e.g., specific libraries, database schemas, or code snippets) in the `product` domain. Focus MUST remain on "What" the system does and "Why," not "How."
2. **STAKEHOLDER_CLARITY:**
   Documentation MUST be written in a language accessible to non-technical stakeholders while maintaining the "Machine Perception" standards (chunk-local referents, semantic clarity).
3. **TOP_OF_THE_RULE_HIERARCHY:**
   The `product` tier is the top of the Truth Hierarchy for RULES; non-negotiable constraints sit above every tier (manifesto [1].0). Any change here triggers a mandatory review of `architecture` and `modules` tiers to ensure downward alignment.
4. **FLEXIBLE_HIERARCHY:**
   Unlike the `modules` tier, the `product` tier allows high-level root documents (e.g., `vision.dds.md`) directly in the root directory if they represent global project goals. Folderization is only mandatory for complex feature sets or epics.
5. **KPIS_ARE_TARGETS:**
   A KPI is a measurable target, never a rule. EXECUTOR MUST NOT cite a KPI to override an `architecture` or `modules` rule, and MUST NEVER cite one against `product-constraints`; such a conflict is escalated to a human.

## [2] ACTION_ROUTING_MATRIX

EXECUTOR MUST evaluate the requested ACTION and follow ONE of the routing paths below to continue the operation.

**IF ACTION === "CREATE" (Defining a new business goal, requirement, or persona):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.product/write.dds.md` to retrieve the strategic template focused on KPIs and User Stories.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

**IF ACTION === "UPDATE" (Refining business logic or changing market direction):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.product/update.dds.md` to manage strategic versioning and cross-domain impact analysis.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

**IF ACTION === "DELETE" or "DEPRECATE" (A project goal or business feature is abandoned):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.product/deprecate.dds.md` to trigger the downward cascade across architecture and modules.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

# END_OF_DIRECTIVE
