"""Hygiene tests for the human-facing prose: README.md, docs/, and the READMEs under templates/ and examples/.

Run from the repository root:
    python -m unittest discover -s tests -v
"""
import re
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
PROSE = [REPO / "README.md", REPO / "AGENTS.md", REPO / "templates" / "adapters" / "README.md",
         REPO / "examples" / "task-tracker" / "README.md", REPO / "examples" / "broken" / "README.md"] + \
        sorted((REPO / "docs").glob("*.md"))

# mechanisms that were removed or renamed, and claims the project no longer makes
FORBIDDEN = [
    ("llms.txt", "removed: a website convention, not read by repository agents"),
    ("Documentary", "the name is Documentation-Driven System"),
    ("Pronoun Ban", "renamed: chunk-local referents"),
    ("log rotation", "removed: changelogs are capped, older entries stay in git log"),
    ("automatically rotate", "removed: changelogs are capped"),
    ("locked_by_", "legacy lock value; locks are locked_by + locked_at"),
    ("hallucination", "say Dangling Reference or drift; no hallucination claims"),
    ("enterprise-grade", "marketing register"),
    ("deterministic", "routing is precedence-based, not deterministic"),
    ("zero context", "marketing register"),
    ("guarantee", "no guarantees are made"),
    ("unbreakable", "marketing register"),
    ("battle-tested", "unprovable claim"),
    ("production-ready", "unprovable claim"),
    ("state-of-the-art", "unprovable claim"),
    ("best-in-class", "unprovable claim"),
]

LINK = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")

# exact phrases that may mention an otherwise forbidden word (provenance must name the old slug)
ALLOWED_LITERALS = ["Renamed from `documentary-driven-system`"]


class Wording(unittest.TestCase):
    def test_no_removed_mechanisms_or_marketing_claims(self):
        hits = []
        for path in PROSE:
            text = path.read_text(encoding="utf-8")
            for literal in ALLOWED_LITERALS:
                text = text.replace(literal, "")
            for phrase, why in FORBIDDEN:
                for m in re.finditer(re.escape(phrase), text, flags=re.I):
                    line = text.count("\n", 0, m.start()) + 1
                    hits.append("%s:%d: %r (%s)" % (path.relative_to(REPO).as_posix(), line, phrase, why))
        self.assertEqual(hits, [], "\n" + "\n".join(hits))


class Links(unittest.TestCase):
    def test_relative_links_resolve(self):
        missing = []
        for path in PROSE:
            text = path.read_text(encoding="utf-8")
            for m in LINK.finditer(text):
                target = m.group(1)
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (path.parent / target).exists() and not (REPO / target).exists():
                    missing.append("%s -> %s" % (path.relative_to(REPO).as_posix(), target))
        self.assertEqual(missing, [], "\n" + "\n".join(missing))


class Disclosure(unittest.TestCase):
    """An evaluator searching README for telemetry or network behaviour must find an explicit statement, not silence."""

    def test_readme_states_telemetry_network_and_write_behaviour(self):
        text = (REPO / "README.md").read_text(encoding="utf-8").lower()
        for word in ("telemetry", "network", "credentials", "what it writes", "turning a gate off"):
            self.assertIn(word, text, "README must state its %s behaviour explicitly" % word)


class Consistency(unittest.TestCase):
    def test_docs_name_the_current_version(self):
        script = (REPO / ".dds" / "meta" / "scripts" / "dds.py").read_text(encoding="utf-8")
        version = re.search(r'^DDS_VERSION = "([^"]+)"', script, re.M).group(1)
        for path in (REPO / "README.md", REPO / "docs" / "dds-main.md"):
            self.assertIn(version, path.read_text(encoding="utf-8"), "%s does not mention dds_version %s" % (path.name, version))

    def test_every_tier_guide_points_at_the_protocols_and_the_example(self):
        for tier in ("product", "architecture", "modules"):
            text = (REPO / "docs" / ("dds-%s.md" % tier)).read_text(encoding="utf-8")
            self.assertIn(".dds/meta/dds.%s/" % tier, text)
            self.assertIn("examples/task-tracker/.dds/%s/" % tier, text)
            self.assertIn("check", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
