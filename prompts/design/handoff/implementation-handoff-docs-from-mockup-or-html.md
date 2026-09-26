---
id: "implementation-handoff-docs-from-mockup-or-html"
title: "Create an Implementation Handoff"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "handoff"
when_to_use: "Document an approved mockup or HTML interface as three build-ready Markdown specifications"
search_terms: ["implementation-handoff-docs-from-mockup-or-html", "design", "handoff"]
inputs: ["APPROVED_SOURCES", "PROJECT_CONTEXT"]
output: "project-spec.md, project-design.md, and project-design-system.md, separately and in that order."
mode: "document"
capabilities: ["file-access", "vision-when-needed"]
related: ["image-to-design-system-extraction-extended", "implement-spec-into-existing-html-with-design-system", "design-system-compliance-audit-and-fix"]
aliases: ["design/implementation-handoff-docs-from-mockup-or-html.md", "implementation-handoff-docs-from-mockup-or-html.md"]
---

# Create an Implementation Handoff

Document an approved mockup or HTML interface as three build-ready Markdown specifications.

**Type:** prompt · **Mode:** document · **ID:** `implementation-handoff-docs-from-mockup-or-html`

**Expected output:** project-spec.md, project-design.md, and project-design-system.md, separately and in that order.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{APPROVED_SOURCES}}` | Approved mockups, screenshots, HTML, or relevant component files. | approved-dashboard.png and dashboard.html |
| `{{PROJECT_CONTEXT}}` | Product brief, behavior requirements, constraints, and optional design reference; None if absent. | dashboard-brief.md and design.md |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Approved visual or HTML sources:
{{APPROVED_SOURCES}}

Brief, constraints, and optional existing design-system reference:
{{PROJECT_CONTEXT}}

You will receive one or more source inputs for a product, feature, interface, dashboard, app screen, or website section.

Source inputs:
- Current mockup, screenshot, HTML file, prototype, or generated UI.
- Original task brief, redesign brief, feature request, content file, or product notes.
- Optional design reference or design-system file.

Task:
Create a complete implementation handoff package so another agent can build the interface accurately without guessing.

Use the mockup or HTML as the source of truth for what the interface looks like.
Use the original task/brief as the source of truth for what the interface must do.
Use any design-system or reference file as the source of truth for visual rules and constraints.

Return exactly these three Markdown files:

1. project-spec.md
2. project-design.md
3. project-design-system.md

Do not write implementation code. Do not redesign the interface. Do not invent unrelated features. Document the approved interface clearly enough that an implementation agent can recreate it accurately.

## File 1: project-spec.md

Create the functional specification.

Include:

- project objective
- product/interface purpose
- primary users
- core user goals
- screens/views/sections
- required features
- data/content requirements
- user flows
- interactions
- states
- edge cases
- validation rules
- accessibility requirements
- responsive requirements
- implementation notes
- acceptance criteria

This file should explain what must be built and how it should behave.

## File 2: project-design.md

Create the design implementation guide.

Include:

- layout structure
- section-by-section breakdown
- component inventory
- navigation behavior
- toolbar/header behavior
- sidebars/panels/cards/forms/tables/modals if present
- spacing and density guidance
- hierarchy and visual rhythm
- empty/loading/error/success states
- responsive layout behavior
- interaction notes
- what must be preserved from the mockup or HTML
- what the implementation agent must not change

This file should explain how the interface should be assembled visually and structurally.

## File 3: project-design-system.md

Create the inferred design system.

Extract and document:

- design principles
- color tokens
- typography tokens
- spacing tokens
- radius tokens
- border tokens
- shadow/elevation rules
- surface/background rules
- button styles
- input/form styles
- card/panel styles
- table/list styles
- badge/tag/status styles
- modal/sheet/popover styles
- icon rules
- motion/transition rules
- responsive rules
- accessibility rules
- design QA checklist

If exact values are available from the HTML or design-system file, use them.
If exact values are not available, estimate values from the mockup, mark them as inferred, and record confidence. Use unknown when the source does not support an estimate; do not present proposed behavior or tokens as observed facts.

## Documentation rules

Be rigorous and practical.

Before writing the files, inspect all provided sources and identify:

- what is visually shown
- what behavior is implied
- what features are required by the brief
- what components are reusable
- what design tokens are visible or inferable
- what states are missing but necessary
- what implementation constraints must be preserved

Use clear headings, concise explanations, and implementation-ready detail.

Do not over-document obvious things.
Do not under-document important behavior.
Do not include vague design theory.
Do not include marketing fluff.
Do not add features that were not shown or requested.
Do not contradict the supplied mockup, HTML, brief, or design-system reference.

## Output format

Return the three files separately in this order:

1. project-spec.md
2. project-design.md
3. project-design-system.md

Each file must be complete, clean, and ready to save as Markdown.

### Evidence boundaries

Distinguish observed interface details, explicit brief requirements, inferred behavior, and unresolved decisions in all three files. A static mockup cannot confirm hidden menus, validation rules, backend behavior, hover states, or precise font metrics. Document necessary but unspecified states as proposals requiring approval, not added product requirements. Keep component names and token names consistent across the three documents. Do not implement the application in this documentation task.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `vision-when-needed`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Extract Images Into a Reusable Design Contract](../extraction/image-to-design-system-extraction-extended.md) — Produce a detailed visual extraction plus a reusable token-and-component implementation contract.
- [Implement a Spec Into Existing HTML](../page-builds/implement-spec-into-existing-html-with-design-system.md) — Add a specified feature to an existing interface while preserving its architecture and design system.
- [Audit and Implement Design-System Compliance](../quality/design-system-compliance-audit-and-fix.md) — Extract atomic design requirements, implement them in controlled passes, and score only verified compliance.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
