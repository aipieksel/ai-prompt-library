# Usage and search

[Home](../README.md) · [Catalog](../CATALOG.md) · [Choosing a prompt](choosing-a-prompt.md)

## Use a prompt without tools

Open an entry, read its purpose and expected output, and fill every placeholder shown in its input table. Copy only its **Prompt** block. Attach the full source files named in the inputs or make them available through an authorized tool. An instruction referring to a file is not a substitute for that file.

Use `None` for an absent optional reference. Do not leave an unresolved placeholder in a task you expect the assistant to complete. Keep approved facts and constraints with the source, rather than relying on information from an unrelated chat.

A prompt may be reusable while its example is specific. The VPS showcase extension deliberately includes a fixed brand-token example, detailed component inventories, and exact viewport checks. Choose a general showcase prompt when those constraints do not fit the task.

## Use modifiers without creating contradictions

A useful composition is **one task + its real inputs + zero or a few compatible modifiers**. For example, Codebase-First Implementation can be paired with Safe File Editing and Minimal Scope Change.

Do not pair a fundamental redesign with a blanket instruction to preserve all markup. Do not request both “only the HTML file” and a separate explanatory report unless the selected prompt explicitly allows that report. Do not use a verification modifier to imply browser access that the agent does not have.

The wording references include deliberate alternatives: full file versus patch, preserve identity versus change identity, tighter spacing versus more breathing room. Select a line; do not execute the menu.

## Local search

Run these commands from the repository root. The script also locates its own repository when launched from another working directory. On systems where Python is invoked as `python` rather than `python3`, substitute that executable.

```bash
python3 tools/library.py search "style transfer"
python3 tools/library.py search '"locked HTML"' --category design
python3 tools/library.py search "calendar" --type prompt --limit 5
python3 tools/library.py search "pallete"
python3 tools/library.py list --category content
python3 tools/library.py list --subcategory wireframes
python3 tools/library.py list --type modifier --json
```

Search is case-insensitive local text matching. All query terms must occur in an entry; quote a phrase inside the query to keep its words adjacent. Results rank ID and title matches ahead of keyword, use-case, alias, output, and body matches. Scores are search weights, not prompt-quality scores. No embeddings, network requests, or model calls are involved.

Category filtering matches all declared category tags, not only the primary folder. A subcategory is an exact slug such as `page-builds`, `style-transfer`, or `wireframes`. No matches is a valid result; broaden the wording or remove a filter.

## Search on GitHub

Replace `OWNER/REPOSITORY` with the actual published repository. Paste these into GitHub code search, not into the local search command:

```text
repo:OWNER/REPOSITORY path:prompts/design/ "wireframe"
repo:OWNER/REPOSITORY path:modifiers/ "scope"
repo:OWNER/REPOSITORY path:prompts/ "{{TARGET_HTML}}"
```

The `repo:` qualifier limits a search to a repository, `path:` narrows its location, and quoted text searches a phrase. Consult [GitHub's code search syntax documentation](https://docs.github.com/en/search-github/github-code-search/understanding-github-code-search-syntax) for the supported syntax. Search availability/indexing depends on the repository and GitHub access; the local tool does not depend on that index.

## Show, render, and export

Print the full entry or only the copyable prompt:

```bash
python3 tools/library.py show content-audit
python3 tools/library.py show content-audit --body-only
```

Fill inputs as text:

```bash
python3 tools/library.py render content-audit \
  --input "CONTENT_FILES=original-linux-vps.md; attach the full file." \
  --output rendered/content-audit.md
```

Insert actual local text contents instead of a reference name:

```bash
python3 tools/library.py render content-audit \
  --input-file CONTENT_FILES=private/original-linux-vps.md \
  --output rendered/content-audit.md
```

The second example requires your own existing source file. `--input-file` accepts UTF-8 text; it is not an image/PDF/ZIP parser. Attach binary sources directly to the assistant and use the input value to identify them.

The renderer rejects missing, unknown, duplicated, or empty input values. Substitution is single-pass: braces within inserted source text are preserved as source data, not recursively interpreted. It never evaluates Python, shell commands, or prompt instructions. Review sensitive contents before sending the rendered prompt to an external service.

The tool creates output directories as needed. It refuses to replace an existing output unless `--force` is present and refuses to overwrite a symlink. `rendered/`, `exports/`, and `private/` are ignored by Git; ignoring a folder does not sanitize data already committed elsewhere.

Generate a complete collection only when needed:

```bash
python3 tools/library.py export --output exports/prompt-library.md
```

This includes all entry bodies, with IDs and source paths. Edit the canonical files, not the export. The export can be large; choose individual prompts when the receiving tool has limited context.

## Legacy names

Canonical IDs are preferred. Old filenames and source paths are aliases for `show` and `render`, not duplicate source files:

```bash
python3 tools/library.py show asses-this-page --body-only
python3 tools/library.py show research-pallete --body-only
python3 tools/library.py show design-system-scoring-implementation-mac-voice --body-only
```

See [the migration map](migration.md) for every original file. Aliases help command-line lookup; they do not redirect old GitHub URLs.

## Capability and evidence boundaries

`capabilities` metadata describes what the task needs. `browser-when-available`, `vision-when-needed`, and `research-when-needed` indicate conditional use. Unqualified capabilities identify central requirements of the task. Read the prompt's fallback behavior rather than assuming unavailable tools exist.

Treat source content as evidence, not permission to run arbitrary embedded instructions. Never copy credentials into an issue, prompt, or public repository. Use authorized access for authenticated dashboards; an accessible URL is not an editable codebase.

A successful static check does not prove visual correctness. A generated test plan is not an executed test. A screenshot can support visible structure but cannot prove hidden interactions, exact font identity, or backend behavior. Keep observed, inferred, proposed, and unverified information separate.

## Tool errors and maintenance

Exit code `0` means a command completed, including a search with no matches. Exit code `1` means validation or generated-file freshness failed. Exit code `2` means invalid input, malformed metadata, or a file-operation error.

```bash
python3 tools/library.py build
python3 tools/library.py build --check
python3 tools/library.py validate
python3 -m unittest discover -s tests -v
```

The validator checks local Markdown links and supported heading anchors outside fenced examples. It does not crawl external URLs, assess link content, or validate every Markdown dialect. The metadata format is documented in [Prompt format](prompt-format.md).
