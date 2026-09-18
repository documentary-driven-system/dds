# AGENTS.md

This repository publishes the Documentation-Driven System (DDS): the `.dds/` template with its protocols under `.dds/meta/`, the validator `.dds/meta/scripts/dds.py`, the adapters under `templates/adapters/`, and the examples. There is no application code here; the specification is the product.

## Working here

1. Protocol text under `.dds/meta/` is the specification. A change there is a DDS version change: bump `dds_version` in `.dds/tree.dds.md` and `.dds/meta/manifesto.dds.md`, `DDS_VERSION` in `dds.py`, and `metadata.dds_version` in `templates/adapters/skills/dds/SKILL.md` together, then run `python tools/sync_copies.py` to refresh the copies under `examples/task-tracker/`; the tests check they all agree.
2. Every ENFORCED rule in `.dds/meta/schema.dds.md` has three parts: a code path in `dds.py`, a defect in `examples/broken/`, and a line in `examples/broken/EXPECTED.txt`. A rule is done when all three exist.
3. `examples/broken/` is invalid on purpose; its defects stay.
4. Before committing run `python .dds/meta/scripts/dds.py check --gate` and `python -m unittest discover -s tests`. Ready when both pass.

`templates/adapters/README.md` explains how a consuming repository installs the entry points and gates.
