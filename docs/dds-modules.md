# DDS: The Modules Tier (`.dds/modules/`)

**The Engineer’s Guide to Feature-Level Documentation and Machine Perception:**

---

## 1. Introduction

Welcome to the **Modules Tier** of the Documentary Driven System (DDS).

If the Product tier is the "Why" and the Architecture tier is the "Where," the **Modules tier is the "How."** This directory is owned by Software Engineers and Autonomous Coding Agents. It houses the granular, feature-specific documentation of the application—covering everything from UI component logic to state management and data validation rules.

This guide explains how to read, write, update, and deprecate modular documentation within the `.dds/` framework.

## 2. The Iron Laws of the Modules Tier

To maintain a pristine, hallucination-free Single Source of Truth (SSoT), all contributors (human and AI) must strictly adhere to three foundational laws:

### I. Modular Integrity (No 1:1 File Mapping)

Do not create a `.dds.md` file for every single `.ts` or `.css` file in your codebase. DDS documents **Logical Features**, not source files. For example, the UI, logic, and style files for a user login should all be governed by a single document: `.dds/modules/auth/login.dds.md`.

### II. Strict Folderization (No Root Clutter)

Never place a feature document directly in the `.dds/modules/` root. Every document must reside in a domain-specific folder (e.g., `modules/payment/`). For complex features, nested sub-domains are encouraged (e.g., `modules/payment/stripe/`).

### III. Hierarchical Obedience

The Modules tier sits at the bottom of the DDS Truth Hierarchy. Module rules **must never** contradict the global API contracts defined in the Architecture tier, nor the business goals defined in the Product tier.

## 3. The Lifecycle of a Module Document

The Modules tier operates on a strict, deterministically routed lifecycle. Whether you are creating a new feature or deleting an old one, there is an exact protocol to follow.

### A. Creating a New Module (`write.dds.md`)

When documenting a new feature, contributors must use **RAG-Optimized Linguistics (Machine Perception)**. This ensures that when an AI parses the document, it understands the context perfectly, even if the text is chunked into small pieces.

* **The Pronoun Ban:** Never use vague pronouns ("It", "This", "They"). Always name the subject explicitly (e.g., "The `AuthButton` component...").
* **Context-Bearing Headers:** Headers must contain the feature name (e.g., `### [Login_Form] Error Handling`).
* **Depth Limit (Max H3):** Do not use headers deeper than `###`. Deep nesting breaks vector search chunking.
* **Recursive Indexing:** Every new file must be registered in its local `tree.dds.md`, which links to the parent tree, all the way up to the Master Root Tree.

### B. Updating an Existing Module (`update.dds.md`)

Code changes rapidly, and documentation must keep pace without breaking the system.

* **Concurrency Control (File Locking):** Before editing, contributors lock the file (`status: locked_by_[user/agent]`). If an agent crashes during an update, a **40-Minute Timeout Override** ensures the file does not remain deadlocked forever.
* **Atomic Updates:** Do not rewrite the entire file. Use targeted, localized `diff` updates to modify only the relevant semantic chunks.
* **Log Rotation:** To prevent AI memory overflow (Token Limit breaches), file changelogs are automatically rotated. Once a document exceeds 10 update logs, the oldest entries are moved to the `.dds/archive/` directory.

### C. Deprecating a Module (`deprecate.dds.md`)

Features die, but their memory must be managed safely to prevent AI hallucinations.

* **Dependency Pre-Flight:** Before deletion, the system checks if other active modules depend on the target feature.
* **The Tombstone Protocol:** Never physically delete an index line from a tree. Instead, leave a "Tombstone" (e.g., `- [DEPRECATED -> archive_link] Feature X removed`). This tells the AI *why* a file is missing, preventing Dangling References and 404 Context Errors.

## 4. Reverse Documentation (Code to Abstraction)

When updating a module because of a codebase change, contributors must translate physical code back into abstract constraints.

* **Anti-Pattern:** "Added `if (user.age < 18) return false` to `auth.ts`." *(Too tied to source code)*
* **DDS Standard:** "System MUST block authentication for users under 18 years old." *(Universal business logic)*

## 5. Getting Started

If you are an AI Agent, read the `.dds/meta/manifesto.dds.md` to begin routing.
If you are a human developer, find the module you are working on in the Master Root Tree (`.dds/tree.dds.md`) and ensure your code perfectly reflects the written constraints.

Welcome to deterministic, enterprise-grade engineering.
