# DDS: The Product Tier (`.dds/product/`)

**The Strategist’s Guide to Business Logic, Epics, and Machine Perception:**

---

## 1. Introduction

Welcome to the **Product Tier** of the Documentary Driven System (DDS).

If the Architecture tier is the "Where" and the Modules tier is the "How," the **Product tier is the "Why."** This directory is the absolute top of the Truth Hierarchy. Owned by Product Managers, Business Analysts, and AI Strategy Agents, this tier houses the business vision, user personas, Key Performance Indicators (KPIs), and detailed User Stories.

This guide explains how to define and manage business requirements within the `.dds/` framework to ensure perfectly aligned technical execution.

## 2. The Iron Laws of the Product Tier

Because the Product tier sits at the apex of the system, every decision made here ripples downward. Contributors must adhere to three foundational laws:

### I. Absolute Technology Agnosticism

The Product tier documents **Business Value**, not technical implementation. You must never mention specific coding languages, database structures (e.g., SQL), or frameworks (e.g., React) in this directory. Speak in terms of "Data Storage," "User Interface," and "Business Rules."

### II. The Downward Cascade (Absolute Authority)

The Product tier is the ultimate authority. If a business requirement changes here, it instantly renders conflicting Architecture or Module documents invalid. Product dictates Architecture; Architecture dictates Modules.

### III. Flexible Folderization

Unlike lower tiers, the Product tier allows for high-level, global documents (e.g., `vision.dds.md`, `target-personas.dds.md`) to sit directly in the root `.dds/product/` directory. Only specific, complex feature sets (Epics) require isolated sub-directories (e.g., `.dds/product/epics/user-onboarding/`).

## 3. The Lifecycle of a Product Document

Managing business logic in DDS requires deterministic routing to ensure AI agents and human developers never lose context.

### A. Creating Business Requirements (`write.dds.md`)

When defining a new Epic or global strategy, contributors use **RAG-Optimized Linguistics** to ensure perfect machine perception:

* **Structured Epics:** Documents follow a strict template detailing Business Vision, Target Personas, KPIs, and Agile User Stories (*"As a [Persona], I want to [Action], so that [Benefit]"*).
* **The Pronoun Ban:** Vague pronouns ("It", "This") are forbidden. Always explicitly name the feature or persona.
* **Header Constraints:** To maintain vector search integrity, headers must contain context (e.g., `### [Payment_Epic] Acceptance Criteria`) and never exceed `###` (H3) in depth.

### B. Updating the Strategy (`update.dds.md`)

Pivoting a business strategy requires extreme precision to prevent technical misalignment.

* **Downward Impact Assessment:** When a KPI or User Story is updated, the system mandates a cascade check: *Does this business change require a database update? Does it change a UI component?* Corresponding tasks must be routed to the lower tiers.
* **Atomic Updates & Log Rotation:** Updates are localized to specific semantic chunks. To protect AI token limits, changelogs are automatically rotated to the `.dds/archive/` once they exceed the entry threshold.

### C. Abandoning an Epic (`deprecate.dds.md`)

When a business idea is canceled, its technical debt must be ruthlessly purged.

* **Cascade Destruction:** Unlike the Modules tier, which stops if dependencies exist, deleting a Product document *triggers* the deletion of all technical documents that depended on it. If the "Why" is dead, the "How" must die too.
* **The Tombstone Protocol:** Abandoned strategies are moved to the archive, and a "Tombstone" pointer is left in the Master Index (e.g., `- [DEPRECATED -> archive_link] Crypto payment epic abandoned.`). This ensures AI agents know *why* a feature was canceled.

## 4. Pre-Flight Self-Correction

DDS requires all contributors (especially AI agents) to perform a self-audit before saving a Product document:

1. Is the text completely free of technical jargon and coding frameworks?
2. Are the KPIs explicitly measurable?
3. Are there any isolated pronouns that could confuse an LLM?

## 5. Getting Started

If you are an AI Agent, read the `.dds/meta/manifesto.dds.md` to begin routing.
If you are a Product Manager, start by reviewing `.dds/product/product.tree.dds.md` to understand the current global strategy before defining a new Epic.

Welcome to strategy executed with absolute deterministic precision.
