# DDS: The Architecture Tier (`.dds/architecture/`)

The human guide to the Architecture tier. The protocols in `.dds/meta/dds.architecture/` are the source of truth; this page explains them.

---

## 1. What lives here

The Architecture tier is the "Where": the tech stack, the data models with exact types, the infrastructure, the security boundaries, and the global API contracts. System Architects and DevOps own it. The tier obeys the Product tier and dictates to the Modules tier.

## 2. The rules of the tier (`rules.dds.md`)

- **Mid-level authority.** An architecture document never contradicts a product requirement or a constraint; module documents obey the data models and boundaries defined here.
- **Shape, not feature logic.** The tier documents *what the system is made of* ("the `users` table has an `email` column", "every request carries a JWT"), not how a feature behaves ("the login button triggers a query"). Feature behaviour belongs to modules.
- **Hybrid folderization.** System-wide documents (`tech-stack.dds.md`, `core-database.dds.md`) live in the tier root; a service or integration with its own scope lives in `architecture/<service>/` with its own index tree.

## 3. The lifecycle of an architecture document

### A. Creating (`write.dds.md`)

- Follow the template: context and alignment (which product requirement this serves), tech stack and infrastructure, data models and schemas, global boundaries and API contracts.
- Exact data types: `VARCHAR(255)`, `UUIDv4`, `TIMESTAMPTZ`, never "text" or "a number".
- Frontmatter follows `schema.dds.md`: `id: architecture-<name>`, `dependencies:` holding the **ids** of the product documents the architecture serves (never paths; `impact` resolves them), a one-sentence `description`.
- Index the document in its folder's tree; finish with `python .dds/meta/scripts/dds.py check`.

### B. Updating (`update.dds.md`)

Two-way impact, because the tier sits in the middle:

- **Upward check.** Does the change break a product requirement or a constraint? Then the update stops; architecture does not overrule product. The requirement is renegotiated first.
- **Downward cascade.** Does the change alter how modules must behave (a renamed column, a changed contract)? `impact <id>` lists the dependents; route their updates.
- Change only the affected section; append a changelog line (ten entries, older ones in `git log`); if `locking: on`, lock and unlock through `dds.py`.

### C. Retiring (`deprecate.dds.md`)

- **Upward validation.** `impact <id> --up` shows which product documents the element serves. If one is still `active`, the retirement is blocked, unless that document is itself the origin of the cascade that reached this element.
- **Downward cascade.** `impact <id> --down` computes the module documents that depend on the element; they are retired in `CASCADE_MODE` (members do not block each other) or updated where the module survives with reduced scope.
- Leaves-first: modules first, this document last. The retired document moves to `.dds/archive/architecture/...` with a banner and its original path; the tree line becomes a Tombstone with the reason; a service folder whose tree is now all Tombstones moves to the archive as well.
- `check` is expected to fail mid-cascade; it passes again once the origin is mutated.

## 4. Before saving

1. Any feature behaviour in here? Move it to the module document.
2. Every column typed exactly?
3. Every pronoun's subject named inside its section?
4. Does this document still serve an active product requirement, and does its `dependencies:` say which one?
5. `check` passes.

## 5. Getting started

AI agents start at `.dds/meta/manifesto.dds.md`. Architects start at `.dds/architecture/architecture.tree.dds.md` to see the current stack and schemas before defining a new one. `examples/task-tracker/.dds/architecture/` shows a filled tier with exact types and a retired service.
