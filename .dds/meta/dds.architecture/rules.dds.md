---
id: dds_architecture_domain_rules
version: 1.0.0
type: domain_dispatcher
dependencies: [meta/manifesto.dds.md]
priority: high
last_updated: 2026-04-12
description: Operational routing and structural constraints for the Architecture (Infrastructure/Data) domain.
---

# SYSTEM_DIRECTIVE: ARCHITECTURE_DOMAIN_DISPATCHER

## [0] DEFINITION & SCOPE

This document is the Domain Dispatcher for the `architecture` tier.
EXECUTOR (System Architect, DevOps, or AI Agent) has been routed here because the task involves global tech stacks, database Entity-Relationship Diagrams (ERDs), infrastructure setup, security protocols, or global API contracts.
This document dictates HOW to handle operations within the `.dds/architecture/` directory.

## [1] DOMAIN_SPECIFIC_CONSTRAINTS (THE IRON LAWS OF ARCHITECTURE)

Before taking any action, EXECUTOR MUST acknowledge the following constraints specific to the `architecture` domain:

1. **THE MID-LEVEL AUTHORITY (TRUTH HIERARCHY):**
   The `architecture` tier obeys the `product` tier and dictates to the `modules` tier. EXECUTOR MUST NOT create architectural constraints that violate business requirements. Conversely, module-level code MUST strictly obey the data models defined here.
2. **ABSTRACT_IMPLEMENTATION (No Feature Logic):**
   EXECUTOR MUST document the *shape* of the system (e.g., "The User table has an email column") and the *boundaries* (e.g., "All APIs must use JWT"), but MUST NOT document feature-specific logic (e.g., "The login button triggers a specific query"). Feature logic belongs in `.dds/modules/`.
3. **HYBRID_FOLDERIZATION:**
   Similar to the `product` tier, `architecture` supports both global and scoped documents. Global constraints (e.g., `tech-stack.dds.md`, `database-schema.dds.md`) MAY reside in the root `.dds/architecture/`. Microservices or specific infrastructure domains MUST be isolated in sub-directories (e.g., `.dds/architecture/services/payment-gateway/`).

## [2] ACTION_ROUTING_MATRIX

EXECUTOR MUST evaluate the requested ACTION and follow ONE of the routing paths below to continue the operation.

**IF ACTION === "CREATE" (Defining a new DB schema, infrastructure, or global API):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.architecture/write.dds.md` to retrieve the architecture-specific template, diagramming rules, and indexing protocol.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

**IF ACTION === "UPDATE" (Modifying a database column, changing a tech stack, or updating an API):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.architecture/update.dds.md` to manage downward cascade analysis and schema versioning.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

**IF ACTION === "DELETE" or "DEPRECATE" (Retiring a database table or shutting down a service):**

- `NEXT_STEP`: EXECUTOR MUST read `.dds/meta/dds.architecture/deprecate.dds.md` to trigger the technical cascade destruction across the `modules` tier.
- *EXECUTOR MUST STOP reading this file and proceed to the target guide.*

# END_OF_DIRECTIVE
