# Canonical entry format

[Home](../README.md) · [Template](../templates/prompt.md) · [Contributing](../CONTRIBUTING.md)

## File locations

Task: `prompts/<primary-category>/<subcategory>/<id>.md`  
Modifier: `modifiers/<id>.md`  
Wording reference: `references/wording/<id>.md`

IDs and subcategories use lowercase kebab-case. Titles can change without changing IDs. `README.md` files under these roots are generated indexes, not entries. Templates and documentation are outside the canonical roots.

## Metadata

Frontmatter is a deliberately restricted subset of YAML: each key occupies one line and every value uses JSON notation. This allows a dependency-free parser while keeping the file readable to YAML tools. Strings must be quoted; arrays must be on one line. Do not use YAML block scalars, unquoted booleans, anchors, tags, or multiline arrays.

| Field | Type | Meaning |
| --- | --- | --- |
| `id` | string | Stable, unique lookup key. |
| `title` | string | Human-readable task or reference name. |
| `type` | string | `prompt`, `modifier`, or `reference`. |
| `primary_category` | string | Main home: `design`, `coding`, `content`, or `business`. |
| `categories` | string array | Searchable category tags, including the primary category. |
| `subcategory` | string | Specific operation, such as `wireframes` or `style-transfer`. |
| `when_to_use` | string | Decision-oriented description, not merely a restated title. |
| `search_terms` | string array | Useful terms, synonyms, domain names, or accepted legacy spelling. |
| `inputs` | string array | All required substitution keys in the prompt body. |
| `output` | string | Concrete deliverable and important success/failure distinction. |
| `mode` | string | Task stage or operation; see below. |
| `capabilities` | string array | Required or conditional tools; these do not install tools. |
| `related` | string array | Existing canonical IDs for a nearby alternative or next step. |
| `aliases` | string array | Unique old IDs, filenames, or paths for local lookup. |

All fields are required. `inputs`, `capabilities`, `related`, and `aliases` may be empty arrays. Array members must be unique nonempty strings. Unknown fields and duplicate keys fail validation.

Supported modes: `audit`, `audit-and-edit`, `build`, `design`, `document`, `edit`, `extract`, `modify`, `plan`, `reference`, `research`, `research-and-build`, `verify`.

Supported capabilities: `archive-creation`, `authenticated-browser`, `browser`, `browser-when-available`, `code-execution`, `file-access`, `research`, `research-when-needed`, `vision`, `vision-when-needed`, `visual-inspection`. Extend the parser and tests deliberately when adding a capability.

## Page content

Use one title, a clear purpose, expected output, an input table with examples, the copy-ready block, usage notes, and relevant links. Put preservation requirements and other essential instructions **inside the prompt block**; notes outside it are not passed by the renderer.

The copyable body sits in an outer `text` fence with at least four backticks, between exactly one pair of boundary comments. The template demonstrates the structure. The outer fence must be longer than any backtick fence inside the body.

The renderer reads only this body. The metadata, surrounding fence, boundary comments, input table, and usage notes are not part of the rendered prompt.

## Placeholders

Use `{{UPPER_SNAKE_CASE}}` exclusively for input substitution. Every token in the body must appear in `inputs`, and every declared input must occur in the body. The same key may appear more than once.

Use `[descriptive output field]` for an example output schema, not a fake required user input. Keep code and CSS braces as normal source syntax. Optional source inputs still need a supplied value; use the literal text `None` rather than an empty string.

## Generated outputs

`tools/library.py build` derives `catalog.json`, `CATALOG.md`, and every canonical folder's `README.md` from the entry metadata and bodies. Generation is deterministic and has no timestamp churn. Each JSON record includes the canonical path and SHA-256 of the normalized copyable body.

`build --check` reports stale or missing outputs without writing them. The JSON catalog is a discovery interface; canonical Markdown remains the editable source. An on-demand single-file export is not another source of truth.

## Validation boundaries

Parsing checks required fields, types, enum values, paths, unique IDs and aliases, related IDs, copy boundaries, placeholder coverage, and exact duplicate bodies. Repository validation also checks generated outputs, local Markdown links outside fenced examples, and macOS metadata artifacts.

These checks are deliberately structural. They do not prove prompt effectiveness, inspect generated UI, verify external facts or URLs, or grant permission to use source material. Document actual task evaluations separately.
