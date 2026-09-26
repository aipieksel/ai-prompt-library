---
id: "prompt-library-dashboard-balsamiq-wireframe"
title: "Prompt Library Dashboard Balsamiq Wireframe"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "wireframes"
when_to_use: "Use to wireframe a prompt library, wording library, knowledge base, or reusable instruction dashboard"
search_terms: ["prompt-library-dashboard-balsamiq-wireframe", "design", "wireframes", "balsamiq", "dashboard", "knowledge-dashboard", "library", "no-code", "planning", "prompt"]
inputs: ["DASHBOARD_REQUEST", "CONTENT_TYPES", "REQUIRED_ACTIONS", "REFERENCE_MATERIAL"]
output: "A low-fidelity library dashboard specification including data model and UI states."
mode: "plan"
capabilities: ["file-access"]
related: ["general-balsamiq-wireframe", "balsamiq-ui-state-map", "execution-plan-from-approved-wireframe", "build-from-approved-balsamiq-wireframe"]
aliases: ["design/wireframes/prompt-library-dashboard-balsamiq-wireframe.md", "prompt-library-dashboard-balsamiq-wireframe.md"]
---

# Prompt Library Dashboard Balsamiq Wireframe

Use to wireframe a prompt library, wording library, knowledge base, or reusable instruction dashboard.

**Type:** prompt · **Mode:** plan · **ID:** `prompt-library-dashboard-balsamiq-wireframe`

**Expected output:** A low-fidelity library dashboard specification including data model and UI states.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{DASHBOARD_REQUEST}}` | Purpose and scope of the library dashboard. | Browse, search, copy, add, and edit reusable prompts. |
| `{{CONTENT_TYPES}}` | Types of entries and their metadata. | Prompts, modifiers, references, categories, and tags. |
| `{{REQUIRED_ACTIONS}}` | Required user actions. | Search, filter, preview, copy, create, edit, and archive. |
| `{{REFERENCE_MATERIAL}}` | Existing library files, examples, and design rules, or None. | Prompt metadata and current app shell. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Library/dashboard description:
{{DASHBOARD_REQUEST}}

Content types:
{{CONTENT_TYPES}}

Required actions:
{{REQUIRED_ACTIONS}}

Reference material:
{{REFERENCE_MATERIAL}}

Create Balsamiq-style wireframes that map the dashboard structure, views, states, user flows, affordances, signifiers, and data model.

Include main library view, search/filter state, entry detail view, add new entry view, edit entry view, category/tag management if relevant, empty state, no search results state, delete/archive confirmation, and mobile/narrow layout if relevant.

Include navigation/sidebar, page header, search, filters, category/tag controls, sorting, list/table/grid, preview/details panel, markdown display area, copy action, metadata, create/edit form, labels, and annotations.

### Scope and evidence

Use supplied requirements, not invented features. Label missing data or behavior as an assumption or dependency. Include only states relevant to the feature, and explain any omitted state that the brief requires. “Balsamiq-style” describes low fidelity; do not claim to have created a native Balsamiq project unless that file was actually generated. Keep the output reviewable as annotated Markdown or clearly labeled wireframes; do not imply that a plan is an implemented interface.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [General Balsamiq Wireframe](general-balsamiq-wireframe.md) — Use for any project, feature, dashboard, page, workflow, or interface before implementation.
- [Balsamiq UI State Map](balsamiq-ui-state-map.md) — Use when you want every meaningful UI state mapped before building.
- [Execution Plan From Approved Wireframe](execution-plan-from-approved-wireframe.md) — Use after wireframes are approved to create an implementation plan before coding.
- [Build From Approved Balsamiq Wireframe](build-from-approved-balsamiq-wireframe.md) — Use when the wireframe is approved and the agent should implement from it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
