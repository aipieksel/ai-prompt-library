#!/usr/bin/env python3
"""Browse, validate, render, and index the prompt library using Python's standard library.

This tool only reads/writes local files. It never calls an AI model, executes prompt
contents, opens a network connection, or changes a remote repository.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shlex
import sys
import tempfile
from dataclasses import dataclass
from typing import Any, Sequence
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
ENTRY_ROOTS = ("prompts", "modifiers", "references")
START, END = "<!-- prompt:start -->", "<!-- prompt:end -->"
TOKEN = re.compile(r"\{\{([A-Z][A-Z0-9_]*)\}\}")
ID = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
TYPES = {"prompt", "modifier", "reference"}
CATEGORIES = {"design", "coding", "business", "content"}
MODES = {"audit", "audit-and-edit", "build", "design", "document", "edit", "extract",
         "modify", "plan", "reference", "research", "research-and-build", "verify"}
CAPABILITIES = {"archive-creation", "authenticated-browser", "browser", "browser-when-available",
                "code-execution", "file-access", "research", "research-when-needed",
                "vision", "vision-when-needed", "visual-inspection"}
FIELDS = ("id", "title", "type", "primary_category", "categories", "subcategory", "when_to_use",
          "search_terms", "inputs", "output", "mode", "capabilities", "related", "aliases")
ARRAY_FIELDS = {"categories", "search_terms", "inputs", "capabilities", "related", "aliases"}
LABELS = {
    "design": "Design", "coding": "Coding", "business": "Business", "content": "Content",
    "style-transfer": "Style transfer", "redesign": "Redesign", "components": "Components",
    "wireframes": "Wireframes", "showcases": "Showcases", "quality": "Quality and compliance",
    "page-builds": "Page and feature builds", "dashboard-migration": "Dashboard migration",
    "extraction": "Visual extraction", "handoff": "Implementation handoff",
    "agent-quality": "Agent quality", "code-quality": "Code quality",
    "codebase-alignment": "Codebase alignment", "integration-planning": "Integration planning",
    "editing": "Content editing", "wording": "Wording references",
    "modifiers": "Modifiers", "references": "References", "prompts": "Task prompts",
}


class LibraryError(ValueError):
    """An actionable library/input error, reported without a traceback by the CLI."""


@dataclass(frozen=True)
class Entry:
    path: str
    meta: dict[str, Any]
    body: str

    @property
    def id(self) -> str:
        return self.meta["id"]

    def record(self) -> dict[str, Any]:
        return {**self.meta, "path": self.path,
                "prompt_sha256": hashlib.sha256(self.body.encode("utf-8")).hexdigest()}


def parse_entry(path: Path, root: Path) -> Entry:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        raise LibraryError(f"{path}: missing opening metadata separator")
    try:
        stop = lines.index("---", 1)
    except ValueError as exc:
        raise LibraryError(f"{path}: missing closing metadata separator") from exc
    meta: dict[str, Any] = {}
    for number, line in enumerate(lines[1:stop], 2):
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        if not separator or key not in FIELDS:
            raise LibraryError(f"{path}:{number}: unknown or malformed metadata key {key!r}")
        if key in meta:
            raise LibraryError(f"{path}:{number}: duplicate metadata key {key}")
        try:
            meta[key] = json.loads(value.strip())
        except json.JSONDecodeError as exc:
            raise LibraryError(f"{path}:{number}: values must use JSON notation (also valid YAML)") from exc
    missing = set(FIELDS) - meta.keys()
    if missing:
        raise LibraryError(f"{path}: missing metadata fields: {', '.join(sorted(missing))}")
    for key in FIELDS:
        value = meta[key]
        if key in ARRAY_FIELDS:
            if not isinstance(value, list) or any(not isinstance(v, str) or not v.strip() for v in value):
                raise LibraryError(f"{path}: {key} must be an array of nonempty strings")
            if len(value) != len(set(value)):
                raise LibraryError(f"{path}: duplicate values in {key}")
        elif not isinstance(value, str) or not value.strip():
            raise LibraryError(f"{path}: {key} must be a nonempty string")
    if not ID.fullmatch(meta["id"]) or not ID.fullmatch(meta["subcategory"]):
        raise LibraryError(f"{path}: id and subcategory must use lowercase kebab-case")
    if meta["type"] not in TYPES or meta["primary_category"] not in CATEGORIES:
        raise LibraryError(f"{path}: unsupported type or primary category")
    if not set(meta["categories"]) <= CATEGORIES or meta["primary_category"] not in meta["categories"]:
        raise LibraryError(f"{path}: categories must include the valid primary category")
    if meta["mode"] not in MODES or not set(meta["capabilities"]) <= CAPABILITIES:
        raise LibraryError(f"{path}: unsupported mode or capability")
    if any(not re.fullmatch(r"[A-Z][A-Z0-9_]*", k) for k in meta["inputs"]):
        raise LibraryError(f"{path}: input names must use UPPER_SNAKE_CASE")
    if text.count(START) != 1 or text.count(END) != 1 or text.index(START) >= text.index(END):
        raise LibraryError(f"{path}: require one ordered pair of prompt boundary markers")
    block = text.split(START, 1)[1].split(END, 1)[0].strip().splitlines()
    if len(block) < 3 or not re.fullmatch(r"`{4,}text", block[0]):
        raise LibraryError(f"{path}: prompt must be in an outer text fence of at least four backticks")
    fence = block[0][:-4]
    if block[-1] != fence:
        raise LibraryError(f"{path}: prompt fence is not closed correctly")
    body = "\n".join(block[1:-1]).strip() + "\n"
    if not body.strip():
        raise LibraryError(f"{path}: prompt body is empty")
    if set(TOKEN.findall(body)) != set(meta["inputs"]):
        raise LibraryError(f"{path}: body placeholders do not match declared inputs")
    return Entry(path.relative_to(root).as_posix(), meta, body)


def load_entries(root: Path = ROOT) -> list[Entry]:
    result: list[Entry] = []
    for folder in ENTRY_ROOTS:
        base = root / folder
        if base.exists():
            for path in sorted(base.rglob("*.md")):
                if path.name != "README.md":
                    if path.is_symlink():
                        raise LibraryError(f"Entry files cannot be symlinks: {path}")
                    result.append(parse_entry(path, root))
    if not result:
        raise LibraryError("No canonical entries found")
    ids: dict[str, str] = {}
    names: dict[str, str] = {}
    hashes: dict[str, str] = {}
    for entry in result:
        if entry.id in ids:
            raise LibraryError(f"Duplicate id {entry.id}: {entry.path} and {ids[entry.id]}")
        ids[entry.id] = entry.path
        for name in [entry.id, *entry.meta["aliases"]]:
            if name in names and names[name] != entry.id:
                raise LibraryError(f"Ambiguous id/alias {name}: {entry.id} and {names[name]}")
            names[name] = entry.id
        digest = hashlib.sha256(entry.body.encode()).hexdigest()
        if digest in hashes:
            raise LibraryError(f"Duplicate prompt bodies: {entry.id} and {hashes[digest]}")
        hashes[digest] = entry.id
        typ = entry.meta["type"]
        expected = (f"prompts/{entry.meta['primary_category']}/{entry.meta['subcategory']}/{entry.id}.md"
                    if typ == "prompt" else f"modifiers/{entry.id}.md" if typ == "modifier"
                    else f"references/wording/{entry.id}.md")
        if entry.path != expected:
            raise LibraryError(f"Path does not match metadata: {entry.path}; expected {expected}")
    for entry in result:
        for target in entry.meta["related"]:
            if target not in ids or target == entry.id:
                raise LibraryError(f"{entry.path}: missing or self-referential related id {target}")
    return sorted(result, key=lambda entry: entry.id)


def resolve(entries: Sequence[Entry], name: str) -> Entry:
    normalized = name.replace("\\", "/")
    for entry in entries:
        if normalized in [entry.id, entry.path, *entry.meta["aliases"]]:
            return entry
    raise LibraryError(f"Unknown entry {name!r}. Use 'search' or 'list' to find an ID.")


def select(entries: Sequence[Entry], category: str | None = None,
           entry_type: str | None = None, subcategory: str | None = None) -> list[Entry]:
    return [e for e in entries if (category is None or category in e.meta["categories"])
            and (entry_type is None or entry_type == e.meta["type"])
            and (subcategory is None or subcategory == e.meta["subcategory"])]


def search(entries: Sequence[Entry], query: str) -> list[tuple[int, Entry]]:
    try:
        terms = [term.casefold() for term in shlex.split(query) if term.strip()]
    except ValueError as exc:
        raise LibraryError(f"Invalid search query: {exc}") from exc
    if not terms:
        raise LibraryError("Search requires at least one nonempty word or quoted phrase")
    matches: list[tuple[int, Entry]] = []
    for entry in entries:
        fields = [(entry.id, 20), (entry.meta["title"], 12),
                  (" ".join(entry.meta["search_terms"]), 8), (entry.meta["when_to_use"], 5),
                  (" ".join(entry.meta["aliases"]), 4), (entry.meta["output"], 3),
                  (entry.body, 1)]
        fields = [(text.casefold(), weight) for text, weight in fields]
        if all(any(term in text for text, _ in fields) for term in terms):
            score = sum(weight for term in terms for text, weight in fields if term in text)
            matches.append((score, entry))
    return sorted(matches, key=lambda pair: (-pair[0], pair[1].id))


def render(entry: Entry, values: dict[str, str]) -> str:
    required = set(entry.meta["inputs"])
    missing, unknown = required - values.keys(), values.keys() - required
    problems: list[str] = []
    if missing:
        problems.append("missing inputs: " + ", ".join(sorted(missing)))
    if unknown:
        problems.append("unknown inputs: " + ", ".join(sorted(unknown)))
    if any(not value.strip() for value in values.values()):
        problems.append("input values cannot be empty; use None for an absent optional source")
    if problems:
        raise LibraryError("; ".join(problems))
    # One substitution pass: inserted text is data, never interpreted as a template or code.
    return TOKEN.sub(lambda match: values[match.group(1)], entry.body)


def collect_values(inputs: Sequence[str], input_files: Sequence[str]) -> dict[str, str]:
    result: dict[str, str] = {}
    for items, read_file in ((inputs, False), (input_files, True)):
        for item in items:
            key, separator, value = item.partition("=")
            if not separator or not re.fullmatch(r"[A-Z][A-Z0-9_]*", key):
                raise LibraryError(f"Expected KEY=value or KEY=path; received {item!r}")
            if key in result:
                raise LibraryError(f"Input {key} was supplied more than once")
            result[key] = Path(value).read_text(encoding="utf-8") if read_file else value
    return result


def save_output(path: Path, text: str, force: bool = False) -> None:
    if path.is_symlink():
        raise LibraryError(f"Refusing to overwrite a symlink: {path}")
    path.parent.mkdir(parents=True, exist_ok=True)
    if not force:
        try:
            with path.open("x", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
        except FileExistsError as exc:
            raise LibraryError(f"Output exists: {path}; choose another path or add --force") from exc
    else:
        if path.exists() and not path.is_file():
            raise LibraryError(f"Output is not a regular file: {path}")
        fd, temp_name = tempfile.mkstemp(prefix=".prompt-library-", dir=path.parent)
        try:
            with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(text)
            os.replace(temp_name, path)
        finally:
            Path(temp_name).unlink(missing_ok=True)


def label(value: str) -> str:
    return LABELS.get(value, value.replace("-", " ").capitalize())


def link_from(source: str, target: str) -> str:
    return os.path.relpath(target, Path(source).parent).replace("\\", "/")


def escape_cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def entry_table(entries: Sequence[Entry], source: str) -> str:
    text = "| Entry | Use it to | Type |\n| --- | --- | --- |\n"
    for entry in sorted(entries, key=lambda e: e.meta["title"].casefold()):
        text += (f"| [{escape_cell(entry.meta['title'])}]({link_from(source, entry.path)}) "
                 f"| {escape_cell(entry.meta['when_to_use'])} | {entry.meta['type']} |\n")
    return text


def generated_files(entries: Sequence[Entry]) -> dict[str, str]:
    counts = {typ: sum(e.meta["type"] == typ for e in entries) for typ in sorted(TYPES)}
    catalog = {"schema_version": 1, "entry_count": len(entries), "counts": counts,
               "entries": [entry.record() for entry in sorted(entries, key=lambda e: e.id)]}
    result = {"catalog.json": json.dumps(catalog, ensure_ascii=False, indent=2) + "\n"}
    intro = "<!-- Generated by tools/library.py build. Edit canonical entry files, not this index. -->\n\n"
    text = intro + "# Prompt catalog\n\n"
    text += (f"{len(entries)} entries: **{counts['prompt']} task prompts**, **{counts['modifier']} modifiers**, "
             f"and **{counts['reference']} wording references**.\n\n"
             "[Choosing a prompt](docs/choosing-a-prompt.md) · [Search and usage](docs/usage.md) "
             "· [Workflow recipes](docs/workflows.md) · [Machine-readable catalog](catalog.json)\n\n"
             "Task prompts are grouped by their primary category; cross-category tags remain searchable. "
             "Modifiers add constraints to a task. References are menus of wording, not tasks to run whole.\n\n")
    for category in ("design", "coding", "business", "content"):
        group = [e for e in entries if e.meta["type"] == "prompt" and e.meta["primary_category"] == category]
        if not group:
            continue
        text += f"## {label(category)}\n\n"
        for sub in sorted({e.meta['subcategory'] for e in group}):
            text += f"### {label(sub)}\n\n" + entry_table([e for e in group if e.meta['subcategory'] == sub], "CATALOG.md") + "\n"
    for typ in ("modifier", "reference"):
        text += f"## {'Modifiers' if typ == 'modifier' else 'Wording references'}\n\n"
        text += entry_table([e for e in entries if e.meta["type"] == typ], "CATALOG.md") + "\n"
    result["CATALOG.md"] = text.rstrip() + "\n"
    # Every canonical folder gets a deterministic, locally linked navigation page.
    folders: set[str] = set()
    for entry in entries:
        parent = Path(entry.path).parent
        while str(parent) != ".":
            folders.add(parent.as_posix())
            parent = parent.parent
    for folder in sorted(folders):
        destination = f"{folder}/README.md"
        group = [e for e in entries if e.path.startswith(folder + "/")]
        title = label(Path(folder).name)
        text = intro + f"# {title}\n\n{len(group)} entries in this folder and its subfolders.\n\n"
        if folder == "modifiers":
            text += "Append compatible instructions to a concrete task. They do not define a task by themselves.\n\n"
        if folder.startswith("references"):
            text += "Select relevant wording; do not run conflicting alternatives as one prompt.\n\n"
        text += (f"[Full catalog]({link_from(destination, 'CATALOG.md')}) · "
                 f"[Choosing a prompt]({link_from(destination, 'docs/choosing-a-prompt.md')})\n\n")
        text += entry_table(group, destination)
        result[destination] = text.rstrip() + "\n"
    return result


def build(root: Path, entries: Sequence[Entry], check: bool = False) -> list[str]:
    changed = []
    for relative, expected in generated_files(entries).items():
        path = root / relative
        actual = path.read_text(encoding="utf-8") if path.exists() else None
        if actual != expected:
            changed.append(relative)
            if not check:
                save_output(path, expected, force=True)
    return changed


def prose_without_fences(text: str) -> str:
    result = []
    active: str | None = None
    for line in text.splitlines():
        match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if active:
            if match and match[1][0] == active[0] and len(match[1]) >= len(active):
                active = None
            continue
        if match:
            active = match[1]
            continue
        result.append(line)
    return "\n".join(result)


def anchors(text: str) -> set[str]:
    seen: dict[str, int] = {}
    result: set[str] = set()
    for line in prose_without_fences(text).splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*$", line)
        if not match:
            continue
        heading = re.sub(r"<[^>]+>", "", match[1]).casefold()
        base = re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")
        count = seen.get(base, 0)
        result.add(base if not count else f"{base}-{count}")
        seen[base] = count + 1
    result.update(re.findall(r'\bid=["\']([^"\']+)["\']', text))
    return result


def check_links(root: Path) -> list[str]:
    errors: list[str] = []
    for path in sorted(root.rglob("*.md")):
        if any(part in {".git", "__pycache__", "rendered", "exports", "private"} for part in path.relative_to(root).parts):
            continue
        text = prose_without_fences(path.read_text(encoding="utf-8"))
        for target in re.findall(r"(?<!!)\[[^\]\n]+\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
            target = target.strip("<>")
            url = urlsplit(target)
            if url.scheme or url.netloc:
                continue  # External network links are intentionally not checked.
            destination = (path.parent / unquote(url.path)).resolve() if url.path else path.resolve()
            if not destination.is_relative_to(root.resolve()):
                errors.append(f"{path.relative_to(root)}: link escapes the repository: {target}")
            elif not destination.exists():
                errors.append(f"{path.relative_to(root)}: broken local link: {target}")
            elif url.fragment and destination.is_file() and destination.suffix == ".md":
                if unquote(url.fragment) not in anchors(destination.read_text(encoding="utf-8")):
                    errors.append(f"{path.relative_to(root)}: missing Markdown heading: {target}")
    return errors


def validate(root: Path, entries: Sequence[Entry]) -> list[str]:
    errors = check_links(root)
    errors += [f"Generated file is stale or missing: {p}; run 'build'" for p in build(root, entries, check=True)]
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if ".git" in relative.parts:
            continue
        if path.name == ".DS_Store" or path.name.startswith("._") or "__MACOSX" in relative.parts:
            errors.append(f"OS metadata artifact: {relative}")
    return errors


def export_collection(entries: Sequence[Entry]) -> str:
    text = ("# Prompt library export\n\nGenerated from canonical entry files. Edit those sources, "
            "not this export. References contain alternative wording; do not execute them as one task.\n\n")
    for entry in entries:
        fence = "`" * max(4, max((len(m[0]) for m in re.finditer(r"^`+", entry.body, re.M)), default=0) + 1)
        text += (f"## {entry.meta['title']}\n\nID: `{entry.id}` · Type: {entry.meta['type']}\n\n"
                 f"Source: `{entry.path}`\n\n{fence}text\n{entry.body}{fence}\n\n")
    return text


def make_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Repository root (default: parent of tools/)")
    sub = parser.add_subparsers(dest="command", required=True)
    for command in ("list", "search"):
        child = sub.add_parser(command, help="List entries" if command == "list" else "Search metadata and full prompt text")
        if command == "search":
            child.add_argument("query", help="Words are AND-matched; wrap a phrase in quotes inside the query")
        child.add_argument("--category", choices=sorted(CATEGORIES))
        child.add_argument("--type", choices=sorted(TYPES), dest="entry_type")
        child.add_argument("--subcategory")
        child.add_argument("--limit", type=int, default=None)
        child.add_argument("--json", action="store_true", dest="as_json")
    show = sub.add_parser("show", help="Print an entry's full page or only its copy-ready body")
    show.add_argument("id", help="Canonical ID, canonical path, or a legacy alias")
    show.add_argument("--body-only", action="store_true")
    rendering = sub.add_parser("render", help="Replace declared inputs in a single local substitution pass")
    rendering.add_argument("id")
    rendering.add_argument("--input", action="append", default=[], metavar="KEY=VALUE")
    rendering.add_argument("--input-file", action="append", default=[], metavar="KEY=PATH")
    rendering.add_argument("--output", type=Path)
    rendering.add_argument("--force", action="store_true", help="Replace an existing output file")
    generating = sub.add_parser("build", help="Regenerate catalog.json, CATALOG.md, and folder indexes")
    generating.add_argument("--check", action="store_true", help="Fail if generated outputs differ; do not write")
    sub.add_parser("validate", help="Check metadata, IDs, aliases, inputs, duplicates, local links, indexes, and OS debris")
    exporting = sub.add_parser("export", help="Create a single-file collection on demand")
    exporting.add_argument("--output", type=Path, required=True)
    exporting.add_argument("--force", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = make_parser()
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        entries = load_entries(root)
        if args.command in {"list", "search"}:
            chosen = select(entries, args.category, args.entry_type, args.subcategory)
            ranked = search(chosen, args.query) if args.command == "search" else [(0, e) for e in chosen]
            if args.limit is not None:
                if args.limit < 1:
                    raise LibraryError("--limit must be at least 1")
                ranked = ranked[:args.limit]
            if args.as_json:
                records = [{**e.record(), **({"search_score": score} if args.command == "search" else {})} for score, e in ranked]
                print(json.dumps(records, ensure_ascii=False, indent=2))
            else:
                for _, entry in ranked:
                    print(f"{entry.id} [{entry.meta['type']}; {entry.meta['primary_category']}/{entry.meta['subcategory']}]\n"
                          f"  {entry.meta['when_to_use']}\n  {entry.path}")
                if not ranked:
                    print("No matching entries. Try fewer words, a synonym, or a broader category.")
        elif args.command == "show":
            entry = resolve(entries, args.id)
            print(entry.body if args.body_only else (root / entry.path).read_text(encoding="utf-8"), end="")
        elif args.command == "render":
            rendered = render(resolve(entries, args.id), collect_values(args.input, args.input_file))
            if args.output:
                save_output(args.output, rendered, args.force)
                print(f"Created {args.output}")
            else:
                print(rendered, end="")
        elif args.command == "build":
            changed = build(root, entries, args.check)
            if args.check and changed:
                print("Stale generated files:\n" + "\n".join(changed), file=sys.stderr)
                return 1
            print(f"{'Checked' if args.check else 'Built'} indexes for {len(entries)} entries; {len(changed)} file(s) differ.")
        elif args.command == "validate":
            errors = validate(root, entries)
            if errors:
                print("Validation failed:\n" + "\n".join(errors), file=sys.stderr)
                return 1
            print(f"PASS: {len(entries)} entries; metadata, paths, aliases, inputs, related IDs, duplicate bodies, local links, generated indexes, and OS metadata checks.")
        elif args.command == "export":
            save_output(args.output, export_collection(entries), args.force)
            print(f"Exported {len(entries)} entries to {args.output}")
    except (LibraryError, OSError, UnicodeError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
