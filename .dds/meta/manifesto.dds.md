---
id: dds_master_manifesto
version: 2.0.0
type: root_dispatcher
priority: absolute_override
last_updated: 2026-04-11
description: Root routing protocol and global constitution for the Documentary Driven System (.dds/).
---

# SYSTEM_DIRECTIVE: DDS_MASTER_DISPATCHER

## [0] DEFINITION & SCOPE
This document is the Root Dispatcher for the Documentary Driven System (`.dds/`). 
It does NOT contain formatting, updating, or writing rules. Its SOLE purpose is to evaluate the user intent and route the EXECUTOR (AI Agent or Human) to the correct Domain Rule Set.
EXECUTOR MUST start every operation by evaluating this matrix.

## [1] DOMAIN_ROUTING_MATRIX
When EXECUTOR receives a task to read, create, or update documentation, EXECUTOR MUST evaluate the `context` and follow ONE of the routing paths below.

**IF context CONTAINS (Business Logic OR Market Goals OR User Personas OR Epics):**
- `TARGET_DOMAIN` = `product`
- `NEXT_ACTION`: EXECUTOR MUST read `.dds/meta/dds.product/rules.dds.md`
- *EXECUTOR MUST STOP reading this manifesto and follow instructions in the target file.*

**IF context CONTAINS (Global Tech Stack OR Database Schemas OR System Infrastructure OR Global API Contracts):**
- `TARGET_DOMAIN` = `architecture`
- `NEXT_ACTION`: EXECUTOR MUST read `.dds/meta/dds.architecture/rules.dds.md`
- *EXECUTOR MUST STOP reading this manifesto and follow instructions in the target file.*

**IF context CONTAINS (Specific Application Features OR Code Logic OR UI Components OR Isolated Modules):**
- `TARGET_DOMAIN` = `modules`
- `NEXT_ACTION`: EXECUTOR MUST read `.dds/meta/dds.modules/rules.dds.md`
- *EXECUTOR MUST STOP reading this manifesto and follow instructions in the target file.*

## [2] CORE_CONSTITUTION (GLOBAL LAWS)
Regardless of the target domain, these global laws apply universally across the entire system:

1. **SINGLE SOURCE OF TRUTH (SSoT):** Code MUST NOT dictate business or architectural logic. The `.dds/` directory is the absolute authority. If code contradicts `.dds/`, the code is considered a bug.
2. **TRUTH_HIERARCHY (CONFLICT RESOLUTION):** IF contradictions exist between domains, EXECUTOR MUST apply this priority: `product` rules OVERRIDE `architecture` rules. `architecture` rules OVERRIDE `modules` rules.
3. **THRESHOLD_BASED_SYNC:** Git commits or Deployments MUST NOT be executed unless all corresponding `.dds/` files are updated to reflect the physical changes in the system (Strict Sync).

# END_OF_DIRECTIVE