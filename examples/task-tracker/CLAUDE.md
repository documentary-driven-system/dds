@AGENTS.md

## Claude Code

- `.claude/settings.json` runs the DDS gate (`dds.py check --gate`) before `git commit …` and `git -C <path> commit …`. When it blocks, fix the reported errors and commit again.
- Use plan mode for changes under `.dds/product/` and `.dds/architecture/`; those tiers cascade downward.
