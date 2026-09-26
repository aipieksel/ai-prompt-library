---
id: "design-system-page-build-from-request"
title: "Design-System Page Build From Request"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "page-builds"
when_to_use: "Use when you want a new page/feature built from a request while using existing project variables and styles"
search_terms: ["design-system-page-build-from-request", "design", "page-builds", "build", "css-variables", "existing-design-system", "new-page", "page", "request", "request-driven"]
inputs: ["TASK", "REFERENCE_FILES"]
output: "Complete HTML, a separate scoped CSS file when needed, and separate JavaScript only when required."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["implement-spec-into-existing-html-with-design-system", "style-extension-from-reference"]
aliases: ["design/page-feature-builds/design-system-page-build-from-request.md", "design-system-page-build-from-request.md"]
---

# Design-System Page Build From Request

Use when you want a new page/feature built from a request while using existing project variables and styles.

**Type:** prompt · **Mode:** build · **ID:** `design-system-page-build-from-request`

**Expected output:** Complete HTML, a separate scoped CSS file when needed, and separate JavaScript only when required.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TASK}}` | The precise page, feature, section, or UI request. | Build a filtering and detail view for import jobs. |
| `{{REFERENCE_FILES}}` | HTML/CSS and relevant project files containing the design system. | Existing page, shared tokens, components, and routing. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Request:
{{TASK}}

Reference files:
{{REFERENCE_FILES}}

Build the requested page, feature, section, or UI using the existing project design system as the source of truth.

Before building, inspect the attached files and search the project for all existing design variables, tokens, theme definitions, root styles, CSS custom properties, utility classes, shared component styles, and layout patterns. Do not assume the variables are only in the attached HTML file.

Use existing variables and component patterns wherever possible. Do not hard-code colors, spacing, font sizes, radius values, shadows, borders, or motion values if an existing variable or pattern already exists.

If the requested UI needs new CSS, create it in a separate scoped CSS file. Do not place new component CSS inside the HTML file except for the link tag. If new variables are required, define them inside the feature wrapper, not globally, unless they clearly need to be reused.

Return the full updated or new HTML file, the separate scoped CSS file, and any separate JS file only if required.

### Verification and missing dependencies

Preserve unrelated existing content, behavior, and hooks. Exercise every new visible action and relevant empty/loading/error state. If a backend capability or real data source is absent, expose an honest disabled or unavailable state rather than fabricating a working integration. Review the full result on desktop, tablet, and mobile where tools allow and report checks that could not run.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Implement a Spec Into Existing HTML](implement-spec-into-existing-html-with-design-system.md) — Add a specified feature to an existing interface while preserving its architecture and design system.
- [Style Extension From Reference](../style-transfer/style-extension-from-reference.md) — Use when one approved HTML section should become the visual source of truth for building more sections.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
