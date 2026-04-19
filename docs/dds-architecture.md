# DDS: The Architecture Tier (`.dds/architecture/`)

**The Architect’s Guide to Infrastructure, Data Models, and Machine Perception:**

---

## 1. Introduction

Welcome to the **Architecture Tier** of the Documentary Driven System (DDS).

If the Product tier is the "Why" and the Modules tier is the "How," the **Architecture tier is the "Where and the Boundaries."** Owned by System Architects, DevOps Engineers, and DBA AI Agents, this directory houses the foundational blueprints of the system: Database Entity-Relationship Diagrams (ERDs), global API contracts, CI/CD pipelines, and the global technology stack.

This guide explains how to define and manage structural requirements within the `.dds/` framework, ensuring that the system's infrastructure perfectly bridges business goals with feature implementation.

## 2. The Iron Laws of the Architecture Tier

The Architecture tier is the "Middle Child" of the DDS Truth Hierarchy. It must balance upward constraints with downward enforcement. Contributors must adhere to three foundational laws:

### I. The Mid-Level Authority (Two-Way Obedience)

The Architecture tier obeys the Product tier and dictates to the Modules tier. You cannot create an architectural constraint (e.g., dropping a database table) that violates a business requirement. Conversely, all code written in the Modules tier must strictly obey the data models and API boundaries defined here.

### II. Abstract Implementation (No Feature Logic)

This tier documents the *shape* of the data and the *boundaries* of the system. You must never document feature-specific logic here (e.g., "The submit button queries this table and shows a success toast"). Keep the focus strictly on data types, schemas, and infrastructure rules. Feature logic belongs in the Modules tier.

### III. Hybrid Folderization

The Architecture tier supports both global and scoped documentation. System-wide documents (e.g., `tech-stack.dds.md`, `global-security.dds.md`) may sit directly in the root `.dds/architecture/` directory. Specific microservices or third-party integrations must be isolated in sub-directories (e.g., `.dds/architecture/payment-gateway/`).

## 3. The Lifecycle of an Architecture Document

Managing infrastructure in DDS requires deterministic routing and extreme caution to prevent cascading failures across the system.

### A. Designing New Infrastructure (`write.dds.md`)

When defining a new schema or service, contributors use **RAG-Optimized Linguistics** to ensure perfect machine perception:

* **Exact Data Typing:** Vague terms like "text" or "number" are forbidden. You must use explicit, platform-agnostic or specific types (e.g., `VARCHAR(255)`, `UUIDv4`, `Float64`).
* **The Pronoun Ban:** Vague pronouns ("It", "This") are forbidden. Always explicitly name the table, column, or service.
* **Context-Bearing Headers:** Headers must encapsulate the domain context (e.g., `### [User_Auth] Database Schema`) and never exceed `###` (H3) in depth to maintain vector search integrity.

### B. Updating Schemas & Contracts (`update.dds.md`)

Updating a database column or changing an API endpoint requires a strict **Two-Way Impact Assessment**:

* **Upward Check:** Does this structural change violate an existing Product KPI or Business Rule? If yes, the update is blocked until the business rule is renegotiated.
* **Downward Cascade:** Does this schema change affect existing code? If yes, the system automatically routes update tasks to the corresponding Modules documents.
* **Concurrency & Logging:** Updates are locked during execution (with a 40-minute timeout safeguard). Changelogs are strictly maintained to track schema versioning and are automatically rotated to the archive to protect AI token limits.

### C. Retiring Infrastructure (`deprecate.dds.md`)

When a database table or microservice is shut down, its removal must be handled surgically.

* **The Two-Way Deprecation Gate:** Infrastructure cannot be deleted if an active Product document still requires it. If cleared by Product, the deprecation triggers a cascade destruction of dependent code in the Modules tier.
* **The Tombstone Protocol:** Retired schemas are moved to the archive, and a "Tombstone" pointer is left in the Master Index (e.g., `- [DEPRECATED -> archive_link] Legacy Auth DB retired.`). This ensures AI agents do not hallucinate about missing tables.

## 4. Pre-Flight Self-Correction

DDS requires all contributors (especially AI agents) to perform a self-audit before saving an Architecture document:

1. **Feature Logic Leakage:** Did I accidentally include UI or specific function behavior in this document? (If yes, move it to Modules).
2. **Type Strictness:** Are all database columns defined with exact data types?
3. **Hierarchy Alignment:** Does this architecture serve a documented business goal?

## 5. Getting Started

If you are an AI Agent, read the `.dds/meta/manifesto.dds.md` to begin routing.
If you are a System Architect, start by reviewing `.dds/architecture/architecture.tree.dds.md` to understand the current global infrastructure before defining a new schema.

Welcome to structurally sound, machine-readable engineering.
