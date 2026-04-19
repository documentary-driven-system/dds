---
id: dds_modules_domain_rules
version: 1.0.0
type: domain_dispatcher
dependencies: [meta/manifesto.dds.md]
priority: high
last_updated: 2026-04-11
description: Operational routing and strict constraints for the Modules (Code/Feature) domain.
---

# SYSTEM_DIRECTIVE: MODULES_DOMAIN_DISPATCHER

## [0] DEFINITION & SCOPE

This document is the Domain Dispatcher for the `modules` tier.
EXECUTOR (AI Agent or Human) has been routed here by the Master Manifesto because the current task involves specific application features, code logic, UI components, or isolated modules.
This document dictates HOW to handle operations within the `.dds/modules/` directory.

## [1] DOMAIN_SPECIFIC_CONSTRAINTS (THE IRON LAWS OF MODULES)

Before taking any action, EXECUTOR MUST acknowledge the following constraints specific to the `modules` domain:

1. **MODULAR_INTEGRITY (No 1:1 File Mapping):**
   EXECUTOR MUST NOT create a `.dds.md` file for every single source code file (e.g., `login.tsx` -> `login.dds.md` is FORBIDDEN).
   EXECUTOR MUST document based on LOGICAL FEATURES (e.g., UI, logic, and style files for 'Login' all map to a single `.dds/modules/auth/login.dds.md`).
2. **STRICT_FOLDERIZATION:**
   EXECUTOR MUST NOT place any file directly in the `.dds/modules/` root. Every feature MUST reside inside a sub-folder representing its domain (e.g., `.dds/modules/[feature_name]/`).
3. **HIERARCHICAL_OBEDIENCE:**
   Module documentation represents the lowest level of the Truth Hierarchy. EXECUTOR MUST NOT write logic here that contradicts `architecture` or `product` rules.

## [2] ACTION_ROUTING_MATRIX

EXECUTOR MUST evaluate the requested ACTION and follow ONE of the routing paths below to continue the operation.

**IF ACTION === "CREATE" (User wants to document a new feature/module):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.modules/write.dds.md` to get the module-specific Markdown template and folderization rules.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

**IF ACTION === "UPDATE" (Code has changed, or a feature logic needs modification):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.modules/update.dds.md` to learn how to acquire file locks, perform atomic updates, and manage the changelog.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

**IF ACTION === "DELETE" or "DEPRECATE" (A feature is removed from the codebase):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.modules/deprecate.dds.md` to execute dependency checks, safe relocation, and tree pruning.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

# END_OF_DIRECTIVE