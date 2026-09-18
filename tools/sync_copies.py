#!/usr/bin/env python3
"""Refresh the copies that examples/task-tracker/ keeps of the template and the adapters.

The example is a consuming repository; it carries `.dds/meta/` and the installed adapters as copies.
`tests/test_examples.py` fails when they drift, and this script is the one-command fix. It is one-directional:
template -> example. An edit made inside the example's copies is overwritten; edit the template instead.

    python tools/sync_copies.py
"""
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EX = REPO / "examples" / "task-tracker"
A = REPO / "templates" / "adapters"

COPIES = [
    (REPO / ".dds" / ".gitignore", EX / ".dds" / ".gitignore"),
    (A / "AGENTS.md", EX / "AGENTS.md"),
    (A / "CLAUDE.md", EX / "CLAUDE.md"),
    (A / "skills" / "dds" / "SKILL.md", EX / ".claude" / "skills" / "dds" / "SKILL.md"),
    (A / "skills" / "dds" / "SKILL.md", EX / ".agents" / "skills" / "dds" / "SKILL.md"),
    (A / "claude-code" / "settings.json", EX / ".claude" / "settings.json"),
    (A / "git" / "pre-commit", EX / ".githooks" / "pre-commit"),
]


def main():
    meta_dst = EX / ".dds" / "meta"
    if meta_dst.exists():
        shutil.rmtree(meta_dst)
    shutil.copytree(REPO / ".dds" / "meta", meta_dst, ignore=shutil.ignore_patterns("__pycache__"))
    for src, dst in COPIES:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(src, dst)
    print("synced .dds/meta and %d adapter files into %s" % (len(COPIES), EX.relative_to(REPO).as_posix()))


if __name__ == "__main__":
    main()
