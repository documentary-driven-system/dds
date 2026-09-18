# DDS: The Product Tier (`.dds/product/`)

The human guide to the Product tier. The protocols in `.dds/meta/dds.product/` are the source of truth; this page explains them.

---

## 1. What lives here

The Product tier is the "Why": the vision, the personas, the KPIs, the epics with their user stories, and the non-negotiable constraints. Product Managers and Business Analysts own it; AI agents write to it only through the protocols.

The tier sits at the top of the hierarchy **for rules**. Above it sits one document that belongs to nobody's roadmap: `constraints.dds.md`.

## 2. The rules of the tier (`rules.dds.md`)

- **Technology agnosticism.** Product documents name no languages, databases, or frameworks. "Data Storage" and "User Interface" are the vocabulary; the "How" belongs to the lower tiers.
- **Stakeholder clarity.** A non-technical reader must be able to follow every document, while the writing conventions (context-bearing headers, referents named inside their section) keep each section readable on its own.
- **Top of the rule hierarchy.** A product rule overrides architecture and module rules; a change here triggers a review of both lower tiers. Constraints sit above even this tier.
- **Flexible folderization.** Global documents (`vision.dds.md`, `constraints.dds.md`, `target-personas.dds.md`) live in the tier root; epics live in `epics/<epic-name>/` with their own index tree.
- **KPIs are targets.** A KPI is measurable and never phrased as a rule. Nobody cites a KPI to override an architecture or module rule, and nobody cites one against a constraint; that conflict goes to a human.

## 3. Constraints (`constraints.dds.md`)

The document with the reserved id `product-constraints` lists security, legal and compliance, safety, and physical constraints as imperative rules, each with its source (a law, a standard, a contract, a policy). It is the one place where "increase conversion" can never win an argument. `gate: strict` requires this document to exist and be `active`; a fresh adoption writes it first, as a draft, and promotes it after legal or security review.

## 4. The lifecycle of a product document

### A. Creating (`write.dds.md`)

- Follow the template: business vision and value, personas, KPIs, user stories with acceptance criteria. The constraints document has its own variant.
- Frontmatter follows `schema.dds.md`: `id: product-<name>`, `dependencies: []` (the top tier depends on nothing), a one-sentence `description` the index tree shows.
- Index the document in its folder's tree; a new epic gets its own `epics/<epic>/<epic>.tree.dds.md` and a pointer from `product.tree.dds.md`.
- Finish with `python .dds/meta/scripts/dds.py check`.

### B. Updating (`update.dds.md`)

- Change only the section that changed; no full rewrites.
- Assess the downward impact: does the new requirement change a data model or an API (architecture)? a component's behaviour (modules)? Route those updates; `impact <id>` shows who depends on the document.
- Append a changelog line with the business reason. The changelog keeps ten entries; older ones stay in `git log`.
- If `locking: on` is set, take and release the lock through `dds.py lock` / `unlock`; never commit a lock.

### C. Retiring (`deprecate.dds.md`)

- A business decision to retire an epic is obeyed, but nothing is left orphaned: `impact <id> --down` computes the cascade set, every architecture and module document that depends on the epic, directly or transitively.
- The cascade runs leaves-first: module documents first, then architecture, the epic itself last, so no active document ever depends on a retired one. Members of the set do not block each other; a dependent outside the set blocks and is handled first.
- Each retired document gets `status: deprecated`, a date, its original path, a banner, and moves to `.dds/archive/product/...`. The tree line that named it becomes a Tombstone with the reason. An epic whose tree is now all Tombstones moves to the archive too, and `product.tree.dds.md` carries a Tombstone to it.
- `check` is expected to fail in the middle of a cascade; run it after the origin is mutated, and never un-retire a member to quiet an intermediate failure.

## 5. Before saving

1. Any technology named? Rewrite it as a business requirement.
2. Any pronoun whose subject is named outside its section? Name the subject.
3. Every KPI measurable, and none of them phrased as a rule?
4. `check` passes.

## 6. Getting started

AI agents start at `.dds/meta/manifesto.dds.md`. Product Managers start at `.dds/product/product.tree.dds.md` to see the current vision, constraints, and epics before writing a new one. `examples/task-tracker/.dds/product/` shows a filled tier, including a retired epic and its Tombstone.
