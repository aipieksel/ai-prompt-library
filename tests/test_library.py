"""Structural and regression tests; these do not execute prompts with a model."""
from __future__ import annotations

import ast
from collections import Counter
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))
import library  # noqa: E402


class RepositoryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = library.load_entries(ROOT)
        cls.byid = {e.id: e for e in cls.entries}

    def test_catalog_covers_all_entries_once(self):
        catalog = json.loads((ROOT / "catalog.json").read_text())
        self.assertEqual(catalog["entry_count"], len(self.entries))
        self.assertEqual(catalog["counts"], dict(Counter(e.meta["type"] for e in self.entries)))
        self.assertEqual({e["id"] for e in catalog["entries"]}, set(self.byid))
        self.assertEqual(len(catalog["entries"]), len(self.entries))

    def test_generated_indexes_are_current(self):
        self.assertEqual(library.build(ROOT, self.entries, check=True), [])

    def test_generation_is_deterministic(self):
        self.assertEqual(library.generated_files(self.entries), library.generated_files(list(reversed(self.entries))))

    def test_local_links(self):
        self.assertEqual(library.check_links(ROOT), [])

    def test_all_entries_render_with_inputs(self):
        for entry in self.entries:
            with self.subTest(entry=entry.id):
                output = library.render(entry, {k: f"Example input for {k}" for k in entry.meta["inputs"]})
                self.assertFalse(library.TOKEN.search(output))
                self.assertTrue(output.strip())
                self.assertNotIn(library.START, output)

    def test_all_legacy_content_names_resolve(self):
        manifest = json.loads((ROOT / "docs/source-manifest.json").read_text())
        for row in manifest["files"]:
            with self.subTest(source=row["path"]):
                for target in row["targets"]:
                    self.assertTrue((ROOT / target).exists())
                if row["action"] != "replaced-navigation":
                    self.assertEqual(library.resolve(self.entries, row["path"]).path, row["targets"][0])

    def test_source_accounting(self):
        data = json.loads((ROOT / "docs/source-manifest.json").read_text())
        self.assertEqual(len(data["files"]), 75)
        self.assertEqual(len({row["path"] for row in data["files"]}), 75)
        self.assertEqual(Counter(row["action"] for row in data["files"]),
                         Counter({"revised-canonical": 68, "merged-exact-duplicate": 1, "replaced-navigation": 6}))

    def test_preserved_contract_anchors(self):
        fixtures = json.loads((ROOT / "tests/fixtures/preserved-contracts.json").read_text())
        for ident, phrases in fixtures.items():
            for phrase in phrases:
                with self.subTest(entry=ident, phrase=phrase):
                    self.assertIn(phrase, self.byid[ident].body)

    def test_no_truncated_legacy_tokens(self):
        for entry in self.entries:
            with self.subTest(entry=entry.id):
                self.assertNotRegex(entry.body, r"(?<!\{)\{[a-z][a-z_]{5,}\}(?!\})")
                self.assertNotIn("aco-markdown-to-balsamiq-wireframe", entry.meta["related"])

    def test_template_parses(self):
        entry = library.parse_entry(ROOT / "templates/prompt.md", ROOT)
        self.assertEqual(entry.id, "example-task")
        self.assertNotIn(entry.id, self.byid)

    def test_python310_syntax(self):
        for path in [ROOT / "tools/library.py", Path(__file__)]:
            ast.parse(path.read_text(), feature_version=(3, 10))

    def test_no_runtime_third_party_imports(self):
        tree = ast.parse((ROOT / "tools/library.py").read_text())
        for node in ast.walk(tree):
            names = [alias.name for alias in node.names] if isinstance(node, ast.Import) else [node.module] if isinstance(node, ast.ImportFrom) else []
            for name in names:
                self.assertIn(name.split(".")[0], sys.stdlib_module_names)

    def test_readme_counts_match(self):
        text = (ROOT / "README.md").read_text()
        counts = Counter(e.meta["type"] for e in self.entries)
        self.assertIn(f"{len(self.entries)} entries · {counts['prompt']} task prompts · {counts['modifier']} modifiers · {counts['reference']} wording references", text)

    def test_duplicate_voice_alias(self):
        result = library.resolve(self.entries, "design-system-scoring-implementation-mac-voice")
        self.assertEqual(result.id, "design-system-compliance-audit-and-fix")


class SearchRenderTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.entries = library.load_entries(ROOT)
        cls.entry = library.resolve(cls.entries, "codebase-first-implementation")

    def test_search_id_ranking(self):
        self.assertEqual(library.search(self.entries, "codebase-first-implementation")[0][1].id, self.entry.id)

    def test_search_phrase(self):
        self.assertTrue(library.search(self.entries, '"locked HTML"'))

    def test_search_all_terms_required(self):
        self.assertEqual(library.search(self.entries, "calendar nonexistingterm98765"), [])

    def test_search_case_insensitive(self):
        self.assertEqual(library.search(self.entries, "CALENDAR"), library.search(self.entries, "calendar"))

    def test_search_legacy_spelling(self):
        results = {e.id for _, e in library.search(self.entries, "pallete")}
        self.assertIn("research-palette-showcase", results)

    def test_search_empty_or_invalid_quote(self):
        for query in ("", "   ", '"unfinished'):
            with self.subTest(query=query), self.assertRaises(library.LibraryError):
                library.search(self.entries, query)

    def test_type_and_category_filters(self):
        result = library.select(self.entries, "content", "prompt")
        self.assertEqual({e.id for e in result}, {"content-audit", "content-update"})
        self.assertEqual(len(library.select(self.entries, entry_type="modifier")), 8)

    def test_missing_input_rejected(self):
        with self.assertRaisesRegex(library.LibraryError, "missing inputs"):
            library.render(self.entry, {"TASK": "Fix this"})

    def test_unknown_input_rejected(self):
        with self.assertRaisesRegex(library.LibraryError, "unknown inputs"):
            library.render(self.entry, {"TASK": "Fix", "PROJECT_CONTEXT": "Files", "OTHER": "Wrong"})

    def test_empty_input_rejected(self):
        with self.assertRaisesRegex(library.LibraryError, "cannot be empty"):
            library.render(self.entry, {"TASK": " ", "PROJECT_CONTEXT": "Files"})

    def test_substitution_is_not_recursive(self):
        output = library.render(self.entry, {"TASK": "Literal {{PROJECT_CONTEXT}}", "PROJECT_CONTEXT": "ACTUAL SOURCE"})
        self.assertIn("Literal {{PROJECT_CONTEXT}}", output)
        self.assertIn("ACTUAL SOURCE", output)

    def test_assignment_preserves_equals_and_unicode(self):
        self.assertEqual(library.collect_values(["TASK=a=b → ✓"], []), {"TASK": "a=b → ✓"})

    def test_duplicate_input_rejected(self):
        with self.assertRaises(library.LibraryError):
            library.collect_values(["TASK=a", "TASK=b"], [])

    def test_input_file_contents(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "source.md"
            p.write_text("Multiline\ncontext ✓", encoding="utf-8")
            self.assertEqual(library.collect_values([], [f"TASK={p}"])["TASK"], "Multiline\ncontext ✓")

    def test_export_includes_every_body(self):
        output = library.export_collection(self.entries)
        for entry in self.entries:
            self.assertIn(entry.body, output)
            self.assertIn(f"ID: `{entry.id}`", output)


class ParserAndFileTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.path = self.root / "modifiers/exact-output-format.md"
        self.path.parent.mkdir(parents=True)
        self.good = (ROOT / "modifiers/exact-output-format.md").read_text()
        self.path.write_text(self.good)

    def tearDown(self):
        self.tmp.cleanup()

    def malformed(self, content, pattern):
        self.path.write_text(content)
        with self.assertRaisesRegex(library.LibraryError, pattern):
            library.parse_entry(self.path, self.root)

    def test_duplicate_metadata_rejected(self):
        self.malformed(self.good.replace('title:', 'id: "another-id"\ntitle:', 1), "duplicate metadata")

    def test_missing_field_rejected(self):
        self.malformed(re.sub(r'^output:.*\n', '', self.good, flags=re.M), "missing metadata")

    def test_unknown_field_rejected(self):
        self.malformed(self.good.replace('title:', 'unknown: "x"\ntitle:', 1), "unknown or malformed")

    def test_non_json_metadata_rejected(self):
        self.malformed(self.good.replace('type: "modifier"', 'type: modifier'), "JSON notation")

    def test_invalid_enum_rejected(self):
        self.malformed(self.good.replace('type: "modifier"', 'type: "unknown"'), "unsupported type")

    def test_wrong_array_type_rejected(self):
        self.malformed(re.sub(r'^categories:.*$', 'categories: "coding"', self.good, flags=re.M), "array")

    def test_placeholder_mismatch_rejected(self):
        self.malformed(self.good.replace('{{OUTPUT_FORMAT}}', '{{MISSING_FORMAT}}'), "placeholders")

    def test_missing_boundary_rejected(self):
        self.malformed(self.good.replace(library.END, ''), "boundary markers")

    def test_incorrect_outer_fence_rejected(self):
        self.malformed(self.good.replace('````\n<!-- prompt:end -->', '```\n<!-- prompt:end -->'), "fence")

    def test_duplicate_ids_rejected(self):
        second = self.path.parent / "duplicate.md"
        second.write_text(self.good)
        with self.assertRaises(library.LibraryError):
            library.load_entries(self.root)

    def test_duplicate_bodies_rejected(self):
        second = self.path.parent / "another-entry.md"
        text = self.good.replace('id: "exact-output-format"', 'id: "another-entry"')
        text = re.sub(r'^aliases:.*$', 'aliases: []', text, flags=re.M)
        second.write_text(text)
        with self.assertRaisesRegex(library.LibraryError, "Duplicate prompt bodies"):
            library.load_entries(self.root)

    def test_overwrite_requires_force(self):
        output = self.root / "result.txt"
        library.save_output(output, "first")
        with self.assertRaises(library.LibraryError):
            library.save_output(output, "second")
        self.assertEqual(output.read_text(), "first")
        library.save_output(output, "second", force=True)
        self.assertEqual(output.read_text(), "second")

    def test_symlink_overwrite_rejected(self):
        target = self.root / "real.txt"
        target.write_text("safe")
        link = self.root / "link.txt"
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest("Symlinks unavailable in this environment")
        with self.assertRaises(library.LibraryError):
            library.save_output(link, "changed", force=True)
        self.assertEqual(target.read_text(), "safe")

    def test_link_checker_detects_missing_file(self):
        self.path.write_text('[Missing](missing.md)\n')
        self.assertTrue(library.check_links(self.root))

    def test_link_checker_ignores_fenced_examples(self):
        self.path.write_text('````text\n[Example](missing.md)\n```\n````\n')
        self.assertEqual(library.check_links(self.root), [])

    def test_link_checker_checks_anchors(self):
        self.path.write_text('# Title\n\n[Good](#title)\n[Bad](#missing)\n')
        self.assertEqual(len(library.check_links(self.root)), 1)

    def test_link_checker_rejects_escape(self):
        self.path.write_text('[Outside](../../../../outside.md)\n')
        self.assertIn('escapes', library.check_links(self.root)[0])


class CLITests(unittest.TestCase):
    def invoke(self, args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            status = library.main(args)
        return status, out.getvalue(), err.getvalue()

    def test_json_search(self):
        status, output, _ = self.invoke(["search", "calendar", "--json"])
        self.assertEqual(status, 0)
        self.assertTrue(json.loads(output))

    def test_show_unknown_returns_error(self):
        status, _, error = self.invoke(["show", "not-a-real-entry"])
        self.assertEqual(status, 2)
        self.assertIn("Unknown entry", error)

    def test_missing_render_input_returns_error(self):
        status, _, error = self.invoke(["render", "content-audit"])
        self.assertEqual(status, 2)
        self.assertIn("missing inputs", error)

    def test_read_only_build(self):
        status, _, _ = self.invoke(["build", "--check"])
        self.assertEqual(status, 0)

    def test_launch_from_another_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            run = subprocess.run([sys.executable, str(ROOT / "tools/library.py"), "list", "--type", "modifier", "--json"], cwd=tmp, text=True, capture_output=True, check=False)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertEqual(len(json.loads(run.stdout)), 8)

    def test_render_creates_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "rendered/task.md"
            status, _, error = self.invoke(["render", "content-audit", "--input", "CONTENT_FILES=original-test.md", "--output", str(p)])
            self.assertEqual(status, 0, error)
            self.assertIn("original-test.md", p.read_text())


if __name__ == "__main__":
    unittest.main()
