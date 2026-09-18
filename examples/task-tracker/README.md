# examples/task-tracker

A fictional small-team task tracker with a **filled** `.dds/`. Every DDS mechanism appears at least once, and the tree passes the strict gate, so this folder is the reference for what a governed repository looks like after adoption.

What to look at:

| Mechanism | Where |
|---|---|
| Non-negotiable constraints above every tier | `.dds/product/constraints.dds.md` (C1-C4); `gate: strict` in `.dds/tree.dds.md` requires it |
| Product > architecture > modules dependencies by id | `dependencies:` in `architecture/core-database.dds.md` and `modules/tasks/create-task.dds.md` |
| Code governed by module documents | `sources:` globs; `check --coverage` reports 5/5 files covered |
| A completed deprecation cascade, leaves-first | Notifications epic (`archive/product/…`) → email gateway (`archive/architecture/…`) → digest module (`archive/modules/…`), three Tombstones in the live trees, `src/notifications/` gone |
| Changelog at the 10-entry cap | `modules/tasks/create-task.dds.md` |
| Installed adapters | `AGENTS.md`, `CLAUDE.md`, `.claude/skills/dds/`, `.agents/skills/dds/`, `.claude/settings.json`, `.githooks/pre-commit` |

Run from this folder:

```bash
python .dds/meta/scripts/dds.py check --gate --coverage
python .dds/meta/scripts/dds.py tree
python .dds/meta/scripts/dds.py impact product-task-management --down
python .dds/meta/scripts/dds.py impact architecture-core-database
```

Two things worth knowing before you copy the pattern:

- `.dds/tree.dds.md` sets `gate: strict` because `product-constraints` is active and coverage is 100%. A fresh adoption starts at `gate: warn` (`adopt.dds.md` [1].3); the copied `.githooks/pre-commit` applies whichever value the tree holds once `git config core.hooksPath .githooks` is set.
- `impact product-task-management --down` lists `modules-auth-login` at depth 2. That is correct, not a bug: Login depends on `architecture-core-database`, and the database serves the epic, so retiring the epic touches everything that stands on the database.

`.dds/meta/` here is a byte-for-byte copy of the template at the repository root; `python tools/sync_copies.py` refreshes it and `tests/test_examples.py` fails when the two drift. The application code under `src/` is illustrative: it is never run and its imports are not installed.
