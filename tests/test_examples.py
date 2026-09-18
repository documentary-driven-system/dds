"""Tests for examples/task-tracker/: the filled reference repository.

Run from the repository root:
    python -m unittest discover -s tests -v
"""
import filecmp
import subprocess
import sys
import unittest
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
EX = REPO / "examples" / "task-tracker"
SCRIPT = EX / ".dds" / "meta" / "scripts" / "dds.py"


def run(*args):
    proc = subprocess.run([sys.executable, str(SCRIPT), "--root", str(EX)] + list(args),
                          cwd=str(EX), capture_output=True, text=True, encoding="utf-8")
    return proc.returncode, proc.stdout + proc.stderr


def same_tree(a, b, ignore=("__pycache__", ".locks")):
    """Byte-for-byte equality of two directory trees."""
    cmp = filecmp.dircmp(str(a), str(b), ignore=list(ignore))
    if cmp.left_only or cmp.right_only or cmp.diff_files or cmp.funny_files:
        return False, "only in %s: %s; only in %s: %s; differ: %s" % (a, cmp.left_only, b, cmp.right_only, cmp.diff_files)
    for sub in cmp.common_dirs:
        ok, why = same_tree(a / sub, b / sub, ignore)
        if not ok:
            return False, why
    return True, ""


class ReferenceTree(unittest.TestCase):
    def test_strict_gate_passes_without_warnings(self):
        code, out = run("check", "--gate")
        self.assertEqual(code, 0, out)
        self.assertIn("RESULT: PASS (0 warnings) [gate]", out)

    def test_every_code_file_is_governed(self):
        code, out = run("check", "--coverage")
        self.assertEqual(code, 0, out)
        self.assertIn("5/5 code files covered by module sources (100%)", out)

    def test_constraints_document_is_active_and_reserved(self):
        text = (EX / ".dds" / "product" / "constraints.dds.md").read_text(encoding="utf-8")
        self.assertIn("id: product-constraints", text)
        self.assertIn("status: active", text)
        for c in ("C1", "C2", "C3", "C4"):
            self.assertIn("**%s " % c, text)

    def test_cascade_left_three_tombstones_and_archived_trees(self):
        code, out = run("tree")
        self.assertEqual(code, 0, out)
        for target in (".dds/archive/product/epics/notifications/notifications.tree.dds.md",
                       ".dds/archive/architecture/email-gateway/email-gateway.tree.dds.md",
                       ".dds/archive/modules/notifications/notifications.tree.dds.md"):
            self.assertIn("DEPRECATED -> " + target, out)
            archived = (EX / target).read_text(encoding="utf-8")
            self.assertIn("status: deprecated", archived)
            self.assertIn("> ⚠️ DEPRECATED", archived)
        self.assertFalse((EX / "src" / "notifications").exists(), "retired code must be gone")

    def test_impact_reports_the_cascade_set(self):
        code, out = run("impact", "product-task-management", "--down")
        self.assertEqual(code, 0, out)
        self.assertIn("1\tarchitecture-core-database\tactive", out)
        self.assertIn("1\tmodules-tasks-create\tactive", out)
        self.assertIn("2\tmodules-auth-login\tactive", out, "login depends on the database that serves the epic")
        code, out = run("impact", "architecture-email-gateway", "--up")
        self.assertEqual(code, 0, out)
        self.assertIn("product-notifications\tdeprecated", out)

    def test_changelog_sits_exactly_at_the_cap(self):
        text = (EX / ".dds" / "modules" / "tasks" / "create-task.dds.md").read_text(encoding="utf-8")
        entries = [ln for ln in text.split("## Changelog", 1)[1].splitlines() if ln.startswith("- [")]
        self.assertEqual(len(entries), 10)
        code, out = run("check")
        self.assertNotIn("changelog has", out)


class CopiesStayIdentical(unittest.TestCase):
    def test_meta_is_the_template(self):
        ok, why = same_tree(REPO / ".dds" / "meta", EX / ".dds" / "meta")
        self.assertTrue(ok, why)

    def test_installed_adapters_are_the_templates(self):
        A = REPO / "templates" / "adapters"
        pairs = [
            (A / "AGENTS.md", EX / "AGENTS.md"),
            (A / "CLAUDE.md", EX / "CLAUDE.md"),
            (A / "skills" / "dds" / "SKILL.md", EX / ".claude" / "skills" / "dds" / "SKILL.md"),
            (A / "skills" / "dds" / "SKILL.md", EX / ".agents" / "skills" / "dds" / "SKILL.md"),
            (A / "claude-code" / "settings.json", EX / ".claude" / "settings.json"),
            (A / "git" / "pre-commit", EX / ".githooks" / "pre-commit"),
            (REPO / ".dds" / ".gitignore", EX / ".dds" / ".gitignore"),
        ]
        for src, dst in pairs:
            with self.subTest(dst=str(dst.relative_to(REPO))):
                self.assertTrue(filecmp.cmp(str(src), str(dst), shallow=False), "%s drifted from %s" % (dst, src))


if __name__ == "__main__":
    unittest.main(verbosity=2)
