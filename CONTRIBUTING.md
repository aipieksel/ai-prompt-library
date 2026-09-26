# Contributing

A useful contribution makes a task easier to choose, execute, or verify. A new title around the same instruction is not automatically a new prompt.

## Before adding a file

Search the catalog and full prompt text. Improve an existing entry when the input/output contract is the same. Add a variant only when it changes a meaningful boundary, source arrangement, output, or workflow stage. Explain that distinction in `when_to_use`, usage notes, and related links.

Choose one entry type: a task prompt, a modifier, or a wording reference. Keep one canonical home, and use category tags rather than duplicate files for cross-category discovery.

## Write and structure the entry

Start from [templates/prompt.md](templates/prompt.md) and follow [the format specification](docs/prompt-format.md). Use a stable lowercase kebab-case ID and filename. Supply every metadata field using the supported JSON-valued YAML notation.

Define the task, source roles, scope boundaries, inputs, expected deliverables, missing-input behavior, and proportionate verification. Use precise action verbs. Preserve concrete examples and constraints; remove conversational history, pressure language, unsupported certainty, and repeated directions.

Do not add hidden requirements or silently change what an existing prompt authorizes. Keep approximate, inferred, sample, and verified information distinct. Do not put credentials, private customer information, or unapproved commercial claims in examples. Use a dated primary source when documenting a version-sensitive external fact.

## Validate the change

```bash
python3 tools/library.py build
python3 tools/library.py validate
python3 -m unittest discover -s tests -v
```

Include the generated catalog and folder-index changes in the same commit. Do not hand-edit those generated files. Check that the updated prompt renders with representative inputs and that related prompts still lead to the correct stage.

For a behavior-changing prompt edit, record the old and new instruction, why the change is needed, and any preserved requirements that could regress. For actual model evaluations, record the input, model/tool environment, output, criteria, and failures; do not label a structural lint check as a prompt-quality benchmark.

## Pull request checklist

- [ ] The entry has a distinct, correctly classified purpose and declared inputs.
- [ ] Scope, source precedence, output, and verification do not contradict one another.
- [ ] Useful source requirements and examples are preserved or changes are explained.
- [ ] IDs, aliases, related links, and generated indexes are correct.
- [ ] Local checks passed; model evaluations are reported separately, if performed.
- [ ] No private data or unsupported authorship, licensing, or product claims were added.

Stable IDs should not change for a title edit. When an ID must change, retain its old name in `aliases`, update related IDs and docs, and explain the migration. Alias lookup does not redirect old hosted URLs.
