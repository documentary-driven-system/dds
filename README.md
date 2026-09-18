![DDS Banner](docs/dds-banner.png)

# DDS — Documentation-Driven System

A `.dds/` directory that describes what a system does, protocols that tell people and AI agents how to change that description, and a script that refuses a commit when the description is inconsistent.

DDS is for repositories where humans and AI coding agents work side by side over a long time. Agents start every session with no memory; a repository that keeps its behaviour written down in one governed place gives every session the same starting point, and the commit gate keeps that place from drifting.

Not to be confused with the OMG Data Distribution Service, which shares the acronym.

## What is in the box

| Part | Where | What it does |
|---|---|---|
| Three tiers of documents | `.dds/product/`, `.dds/architecture/`, `.dds/modules/` | Why the system exists, where it runs, how each feature behaves. Each tier obeys the one above it. |
| Non-negotiable constraints | `.dds/product/constraints.dds.md` | Security, legal, safety, physical rules that no tier, KPI, or business goal overrides. |
| Protocols | `.dds/meta/` | The constitution and routing (`manifesto.dds.md`), one schema (`schema.dds.md`), a brownfield adoption protocol (`adopt.dds.md`), and write / update / deprecate rules per tier. |
| Validator | `.dds/meta/scripts/dds.py` | `check` (schema, ids, dependencies, index trees, tombstones, locks), `impact` (dependency graph), `lock` / `unlock`, `tree`. Standard library only. |
| Adapters | `templates/adapters/` | `AGENTS.md`, `CLAUDE.md`, an Agent Skill, a Claude Code hook, a git pre-commit hook, a CI job. These are what make an agent read `.dds/` at all. |
| Examples | `examples/task-tracker/`, `examples/broken/` | A filled repository that passes the strict gate, and a deliberately invalid tree that the validator must reject. |

## When to use DDS, and when not to

Use it when the repository will live for years, more than one person or more than one AI agent changes it, the cost of "nobody remembers why this works this way" is real, and business rules and technical decisions need an explicit order of precedence.

Skip it for a prototype, a weekend project, or a single-maintainer tool. Three tiers of documentation cost more than they return there; an `AGENTS.md` with a paragraph of conventions is the right size.

## Why this and not a shorter thing

| Alternative | Good at | Does not do |
|---|---|---|
| `AGENTS.md` / `CLAUDE.md` alone | Always-on conventions in one file | No tiers, no lifecycle for retired features, no check |
| `CONTEXT.md` + ADRs (e.g. grill-with-docs) | Shared vocabulary and decision records, very light | No order of precedence between decisions, no dependency graph |
| Spec-driven tools (Spec Kit, Kiro, OpenSpec) | Spec → plan → tasks for one feature at a time | The spec ends with the feature; no persistent system description, no deprecation trail |
| DDS | A persistent, tiered description with a deprecation lifecycle and an impact graph, checked at commit | Semantic verification: `check` validates structure, not whether the code does what the document says |

DDS composes with the first two: the adapters *are* an `AGENTS.md` and a skill, and ADR-style entries fit a document's changelog.

## Quick start

**New repository**

1. Copy `.dds/` from this repository into yours (it ships empty: protocols, the script, three empty tier indexes).
2. Copy the adapters your tools read; `templates/adapters/README.md` maps each agent to its files. `AGENTS.md` (+ `CLAUDE.md`) and the skill under `.claude/skills/dds/` and `.agents/skills/dds/` cover Claude Code, Codex, Cursor, Copilot, and Gemini CLI.
3. Write `.dds/product/constraints.dds.md` and `.dds/product/vision.dds.md` following `.dds/meta/dds.product/write.dds.md`, and list both in `.dds/product/product.tree.dds.md`; an unlisted document fails the gate.
4. Run the gate: `python .dds/meta/scripts/dds.py check --gate`.

**Existing codebase**

Follow `.dds/meta/adopt.dds.md`: documents start as `status: draft` (the code is the reference while a document is a draft), `check --coverage` shows which code no document governs yet, humans commit under `gate: warn` until coverage is good enough, and agents are held to the strict gate from the first day.

## A day with DDS

1. Before changing code, a schema, an API, or documentation, the agent (or you) reads `.dds/meta/manifesto.dds.md` and follows the tier protocol it routes to.
2. The change lands in code and in the governing document before the commit.
3. `python .dds/meta/scripts/dds.py check --gate` runs from the git hook, the agent hook, or CI. A failing gate is fixed, not bypassed.
4. Retiring a feature runs `impact <id> --down` for the cascade set, archives the documents leaves-first, and leaves Tombstones in the index trees so nobody searches for a file that no longer exists.

`python .dds/meta/scripts/dds.py --help` lists the commands. `examples/task-tracker/` shows the result of all of this on a small fictional app, including a completed retirement.

## Repository layout

```text
.dds/                     the template a consuming repository copies (empty tiers, protocols, script)
templates/adapters/       entry points and commit gates per agent, with install notes
examples/task-tracker/    filled reference repository; passes `check --gate` with 0 warnings
examples/broken/          invalid tree; every expected error is listed and tested
tests/                    unit tests for the script, the adapters, and the examples
tools/sync_copies.py      refreshes the copies the example keeps of the template and adapters
docs/                     human-facing guides: overview and one guide per tier
```

## Status

- `v1.0.0` is the original release of the idea as prose. The current line is `dds_version: 2.0.0`, unreleased: a single schema, a validator, adapters, and examples. It breaks the 1.0 frontmatter.
- Verified here: the template and the example pass the strict gate; `examples/broken/` reports every expected error; the test suite under `tests/` passes under Git Bash and PowerShell; the Claude Code hook command exits 2 on a failing tree; the git pre-commit blocks under `gate: strict` and warns under `gate: warn` in a real repository; the skill passes `skills-ref validate`.
- Verified only on paper: the Claude Code hook's `if` pattern match (see `templates/adapters/README.md` for the one-command live check); Python 3.8 support (in the CI matrix, not run locally); the Vale rules.
- Not provided: semantic verification of code against documents. `check` proves structure and consistency; whether the code does what the document says is still a review.

## Development

`python -m unittest discover -s tests` runs everything: the validator against the template and `examples/broken/`, the adapters (including the hook command and a real git pre-commit), the reference example, and the prose hygiene checks. `python tools/sync_copies.py` refreshes the example's copies after a template change.

## Documentation

- Overview: [docs/dds-main.md](docs/dds-main.md)
- Product tier: [docs/dds-product.md](docs/dds-product.md) · Architecture tier: [docs/dds-architecture.md](docs/dds-architecture.md) · Modules tier: [docs/dds-modules.md](docs/dds-modules.md)
- Constitution and routing: [.dds/meta/manifesto.dds.md](.dds/meta/manifesto.dds.md) · Schema: [.dds/meta/schema.dds.md](.dds/meta/schema.dds.md) · Adoption: [.dds/meta/adopt.dds.md](.dds/meta/adopt.dds.md)
- Tier protocols: `.dds/meta/dds.product/`, `.dds/meta/dds.architecture/`, `.dds/meta/dds.modules/` — each with `rules`, `write`, `update`, `deprecate`
- Installing the adapters: [templates/adapters/README.md](templates/adapters/README.md)

## License

MIT — see [LICENSE](LICENSE).
