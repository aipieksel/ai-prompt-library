# AI Prompt Library

Maintained by [aipieksel](https://github.com/aipieksel). Upstream credits and licenses remain with their respective authors.

**Practical prompts for designing interfaces, changing code, improving content, and planning integrations.**

## How the library is organized

Use this map before opening individual files. Every task prompt lives under `prompts/`, never at the repository root.

| Path | What it is | How to pick |
| --- | --- | --- |
| `prompts/design/` | Interface work: wireframes, style transfer, redesign, components, page builds, extraction, showcases, quality, handoff, dashboard migration | Start here for visual or HTML work |
| `prompts/coding/` | Codebase-first implementation, research-before-deciding, and rule/scoring logic | Start here for repository changes |
| `prompts/content/` | Copy audit and applying approved editorial feedback | Start here for writing, not layout |
| `prompts/business/` | Integration planning without writing code | Start here for stakeholder design, not implementation |
| `modifiers/` | Extra constraints you add to a task prompt | Never use a modifier as the only instruction |
| `references/wording/` | Phrase menus for describing a change | Never paste two opposite wording sheets together |
| `templates/prompt.md` | Schema for a new canonical entry | Use when adding a prompt, not when running one |
| `tools/library.py` | Search, render, validate, and rebuild catalogs | Optional; the Markdown files are usable on their own |

Filenames are lowercase kebab-case. Folder names match the category. Generated indexes (`CATALOG.md`, `catalog.json`, folder `README.md` files) come from `python3 tools/library.py build` — edit the canonical prompt files, then rebuild. Do not hand-edit those generated indexes.

This library turns recurring requests into reusable working briefs: what to inspect, what may change, what must remain intact, what to produce, and how to check the result. It is especially focused on design-system work—wireframes, reference-driven HTML, component exploration, faithful style transfer, showcases, and implementation review.

**68 entries · 55 task prompts · 8 modifiers · 5 wording references**

[Browse the catalog](CATALOG.md) · [Choose the right prompt](docs/choosing-a-prompt.md) · [Usage and search](docs/usage.md) · [Workflow recipes](docs/workflows.md)

## Start here

You do not need to install anything to use the prompts.

1. **Choose the operation.** Open the [catalog](CATALOG.md) and select a prompt by the result you need—not just by a matching keyword. Restyling a page and redesigning its structure are different operations.
2. **Supply the inputs.** Each entry has an input table with descriptions and examples. Replace every `{{UPPER_SNAKE_CASE}}` placeholder, and attach or provide access to the actual files it references. Enter `None` for an unavailable optional source.
3. **Copy the prompt block.** Paste only the copy-ready block into your assistant or agent. Do not include the repository metadata or the entire folder.
4. **Check the result.** Compare it with the prompt's output contract and your source requirements. A request to verify something is not evidence that verification happened.

For example, to fix an existing codebase, open [Codebase-First Implementation](prompts/coding/codebase-alignment/codebase-first-implementation.md), fill in `TASK` and `PROJECT_CONTEXT`, and supply the affected source and tests. To restyle an HTML page without changing its layout, start with [Apply Reference Style](prompts/design/style-transfer/apply-reference-style.md) instead of a redesign prompt.

## Find what you need

| Your goal | Start with |
| --- | --- |
| Plan structure before writing production code | [Wireframes](prompts/design/wireframes/README.md) |
| Apply a reference's style while preserving a target | [Style transfer](prompts/design/style-transfer/README.md) |
| Replace layout architecture or visual identity | [Redesign](prompts/design/redesign/README.md) |
| Explore component concepts or eight alternative directions | [Components](prompts/design/components/README.md) |
| Build a page, calendar, composer, or specified feature | [Page and feature builds](prompts/design/page-builds/README.md) |
| Extract visual rules or build a component showcase | [Extraction](prompts/design/extraction/README.md) · [Showcases](prompts/design/showcases/README.md) |
| Check publish readiness or design-system compliance | [Quality and compliance](prompts/design/quality/README.md) |
| Migrate a dashboard or document an approved interface | [Dashboard migration](prompts/design/dashboard-migration/README.md) · [Handoff](prompts/design/handoff/README.md) |
| Implement code, define rules, or compare technical options | [Coding](prompts/coding/README.md) |
| Audit copy or apply approved editorial feedback | [Content](prompts/content/README.md) |
| Plan how a business integration should work | [Business](prompts/business/README.md) |

The task collection contains **49 design prompts, 3 coding prompts, 2 content prompts, and 1 business prompt**. Categories describe the primary home; some entries also have cross-category tags.

### Three kinds of entry

**Task prompts** define a concrete job and deliverable. Choose one as the main instruction.

**[Modifiers](modifiers/README.md)** add a constraint such as minimal scope, safe file editing, no invention, or exact output formatting. Add only compatible modifiers; several prompts already include these boundaries.

**[Wording references](references/wording/README.md)** help describe what is wrong or what should change. They contain alternatives, not one combined task. Do not paste “preserve the structure” and “fundamentally redesign it” together.

## Search the library

**In the repository:** open [CATALOG.md](CATALOG.md) and use your browser's Find function. Every prompt, modifier, and reference folder also has a local index.

**With the optional local tool:** use Python 3.10 or later. No third-party Python packages, API keys, or model subscriptions are required by the tool.

```bash
python3 tools/library.py search "style transfer"
python3 tools/library.py search '"locked HTML"' --category design
python3 tools/library.py list --type modifier
python3 tools/library.py list --subcategory wireframes
```

Search covers IDs, titles, keywords, use cases, output descriptions, legacy aliases, and full prompt text. Separate words are AND-matched; quoted phrases stay together. It is a local text search, not a semantic model search. Add `--json` for machine-readable results.

**On GitHub:** scope code search to the published repository and narrow by path. See the [search guide](docs/usage.md#search-on-github) for examples and the official syntax reference.

### Render a prompt with your inputs

```bash
python3 tools/library.py render codebase-first-implementation \
  --input "TASK=Fix duplicate form submissions without changing the layout." \
  --input "PROJECT_CONTEXT=Attach the form component, submit handler, and relevant tests." \
  --output rendered/fix-submissions.md
```

Open the generated file, supply the referenced project material to your assistant, and run the prompt there. The renderer **does not execute the task or call a model**. Use `--input-file KEY=path` to insert a local text file's contents. Existing outputs are not overwritten unless you add `--force`.

To print an unfilled prompt without its surrounding documentation:

```bash
python3 tools/library.py show apply-reference-style --body-only
```

## Keep source roles clear

In a reference-driven build, different files can control different things:

| Source | Usually controls |
| --- | --- |
| Approved content or scope | Copy, required sections, facts, links, SEO, and product boundaries |
| Approved wireframe | Structure, grouping, hierarchy, and component placement |
| Design reference | Colors, typography, spacing, components, and visual treatment |
| Existing target implementation | Unrelated content, working behavior, hooks, and architecture |

The selected prompt defines the exact precedence. Do not resolve conflicting sources by silently removing content or inventing functionality. [The choosing guide](docs/choosing-a-prompt.md) explains the differences between similar prompts.

## Repository structure

```text
prompt-library/
├── README.md                  # Purpose, quick start, navigation, and search
├── CATALOG.md                 # Generated, linked catalog of all 68 entries
├── catalog.json               # Generated metadata for tools and dashboards
├── prompts/
│   ├── design/                # Wireframes, restyling, builds, extraction, QA
│   ├── coding/                # Implementation, logic, and research decisions
│   ├── content/               # Audit and approved update workflows
│   └── business/              # Integration planning
├── modifiers/                 # Reusable constraints for a main task
├── references/wording/         # Vocabulary and copyable feedback lines
├── docs/                      # Usage, choosing, workflows, schema, and review
├── templates/prompt.md        # Starting point for a new entry
├── tools/library.py           # Search, show, render, build, validate, export
├── tests/                     # Standard-library test suite
└── .github/                   # Validation workflow and contribution support
```

Each canonical entry has one home. The catalog and folder indexes are generated from those files; there is no second manually maintained collection to drift out of sync.

Need the entire collection in one file for an external tool? Generate it when needed:

```bash
python3 tools/library.py export --output exports/prompt-library.md
```

## Common workflows

**Content:** audit the original copy → approve specific findings → apply the matching feedback → review the updated copy and change summary.

**Page delivery:** approve content and wireframe → implement with the reference design system → assess the actual HTML → apply approved issues → check the rendered result.

**Design systems:** extract the supplied images → consolidate the design contract → build a showcase → implement components → audit compliance against atomic requirements.

Use the [workflow recipes](docs/workflows.md) for linked prompts, expected handoff files, and approval boundaries. Do not run the whole library as one instruction.

## Maintain and validate

After editing or adding a canonical entry:

```bash
python3 tools/library.py build
python3 tools/library.py validate
python3 -m unittest discover -s tests -v
```

For a read-only freshness check, run `python3 tools/library.py build --check`. The included GitHub Actions workflow runs the repository checks on pushes and pull requests.

Validation checks metadata, unique IDs and aliases, required placeholders, related entries, duplicate bodies, canonical paths, local documentation links, generated indexes, and macOS metadata debris. It does **not** prove that a model will follow a prompt, verify external links, or benchmark generated applications.

## Adapt responsibly

Use an assistant with the capabilities a prompt actually requires: file access, image understanding, a browser, code execution, or archive creation. A Markdown file does not install those tools or authorize access to accounts.

Do not paste secrets, private customer data, or account credentials into public examples. VPS-specific prompts include specialized constraints and illustrative product examples; they are not statements about a provider's current products, availability, pricing, or proof.

## Contribute and publish

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding another variant. Preserve stable IDs, explain the distinct use case, declare all inputs, and regenerate the indexes.

Migrating from the original collection? The [file-by-file migration map](docs/migration.md) accounts for all 75 original Markdown files; old filenames also resolve through the local tool.

**Licensing:** owner-original material is [MIT](LICENSE).
