# Documentary Driven System (DDS)

**The Universal Open-Source Infrastructure for Machine-Perceptible & Enterprise-Grade Documentation:**

---

## 1. Introduction: What is DDS?

The **Documentary Driven System (DDS)** is a universal, open-source documentation infrastructure designed for modern, high-complexity software projects. It bridges the critical gap between human developers, product managers, and Artificial Intelligence (AI) agents.

Unlike traditional documentation that quickly becomes outdated or scattered, DDS operates as a **State Machine**. It is a structured, deterministically routed, and hierarchical framework that ensures documentation is the absolute Single Source of Truth (SSoT) for the entire lifecycle of a project—from business vision to database schemas and modular code logic.

DDS is built on the principle of **Machine Perception (RAG-Optimization)**. Every rule, template, and directory is strictly formatted so that Large Language Models (LLMs) can read, update, and validate the system without hallucination or context loss, while remaining perfectly legible to human engineers.

## 2. The Core Philosophy

DDS operates on four unbreakable laws:

### I. The Single Source of Truth (SSoT)

Code does not dictate business logic; DDS dictates code. If the physical codebase contradicts the `.dds/` documentation, the codebase is considered to contain a bug. DDS is the ultimate authority on how the system should behave.

### II. The Truth Hierarchy (Conflict Resolution)

In large organizations, departments often clash. DDS resolves conflicts through a strict top-down hierarchy:
**`Product > Architecture > Modules`**

* **Product:** The "Why" (Business goals, user needs) overrides everything.
* **Architecture:** The "Where" (Infrastructure, database) obeys Product, but overrides Modules.
* **Modules:** The "How" (Code, UI, logic) obeys both Architecture and Product.

### III. Threshold-Based Synchronization

A physical project deployment or Git Commit cannot proceed unless the corresponding `.dds/` files have been updated to reflect the new reality. Documentation and code evolve in perfect atomic sync.

### IV. The Cascade Effect (Two-Way Execution)

DDS is a living system. A change at the top (`Product`) triggers an automatic **Downward Cascade**, forcing updates in database schemas and code modules. Conversely, attempting to delete infrastructure (`Architecture`) triggers an **Upward Validation** check against business rules before execution is allowed.

## 3. The Global Architecture & Distributed Memory

The DDS framework utilizes a distributed memory model. It is anchored by a global entry point for AI crawlers, followed by isolated, highly specialized domains within the `.dds/` root directory.

```text
/ (Project Root)
├── llms.txt                    # The Global AI Entry Point (Crawler Guide)
└── .dds/
    ├── meta/                   # The System Brain: Dispatchers, rules, and templates.
    │   └── manifesto.dds.md    # The Master Routing Protocol.
    ├── product/                # The Business Core: Epics, user stories, KPIs.
    │   └── product.tree.dds.md # Local index for the Product domain.
    ├── architecture/           # The Foundation: DB schemas, tech stack, APIs.
    │   └── arch.tree.dds.md    # Local index for the Architecture domain.
    ├── modules/                # The Implementation: Feature logic, state management.
    │   └── modules.tree.dds.md # Local index for the Modules domain.
    ├── archive/                # The Graveyard: Deprecated features and rotated logs.
    └── tree.dds.md             # The Master Root Index (Links all domain trees).
```

### 3.1. The Meta Tier (`.dds/meta/`)

This is the operational rulebook. It contains the **Master Dispatcher** (`manifesto.dds.md`), routing users and AI agents to the correct domain based on their intent.

### 3.2. The Product Tier (`.dds/product/`)

Owned by Product Managers and Business Analysts. This tier defines target audiences, revenue models, and strict business constraints. It is strictly technology-agnostic.
👉 *For detailed operational protocols, refer to:* **`dds-product.md`**

### 3.3. The Architecture Tier (`.dds/architecture/`)

Owned by System Architects and DevOps. This tier defines the global technological boundaries, database ERDs, security protocols, and microservice communications.
👉 *For detailed operational protocols, refer to:* **`dds-architecture.md`**

### 3.4. The Modules Tier (`.dds/modules/`)

Owned by Software Engineers and Coder AI Agents. This tier houses the specific logic for application features (e.g., Auth, Cart, Payment) and exact functional constraints.
👉 *For detailed operational protocols, refer to:* **`dds-modules.md`**

## 4. Advanced System Mechanics

DDS is engineered to survive the chaos of enterprise scaling and multi-agent AI environments. It includes built-in defense mechanisms:

* **YAML Frontmatter (The System Heartbeat):** Every `.dds.md` file begins with a strict YAML block dictating its `id`, `status`, `dependencies`, and `last_updated` state. This makes cross-referencing machine-readable.
* **Pre-Flight Self-Correction (Validation Loop):** Before saving any document, AI agents must run a self-audit (e.g., *"Did I use vague pronouns? Is this header too deep?"*). This guarantees zero context degradation over time.
* **Concurrency Control (File Locking):** Prevents race conditions by locking files (`status: locked_by_[id]`) when an AI or human is updating a document, complete with a 40-minute timeout safeguard.
* **Distributed Tree Indexing:** Prevents "orphaned" knowledge. The indexing is recursive and distributed; every folder has its own `.tree.dds.md`, which links upward to the Master Root Tree.
* **The Tombstone Protocol:** Deleted features are not erased; they leave a "Tombstone" pointer to the archive. This prevents AI agents from experiencing "Dangling References" (404 Context Errors) and explains *why* a feature is gone.
* **Log Rotation:** To protect LLM Context Windows from token overflow, file changelogs automatically rotate to the `.dds/archive/` directory once they exceed a 10-entry threshold.
* **RAG-Optimized Linguistics:** Strict linguistic constraints (e.g., The Pronoun Ban, Maximum H3 Header Depth) ensure that text chunking for Vector Databases yields 100% semantic accuracy.

## 5. Open Source & Contribution

DDS is a living, open-source standard. It is designed to be forked, customized, and integrated into any tech stack. Whether you are a solo developer trying to maintain sanity, or an enterprise managing a swarm of autonomous AI coding agents, DDS provides the foundational memory your project needs to thrive.
