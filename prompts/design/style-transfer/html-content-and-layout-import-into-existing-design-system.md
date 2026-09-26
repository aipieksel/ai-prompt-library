---
id: "html-content-and-layout-import-into-existing-design-system"
title: "HTML Content and Layout Import Into Existing Design System"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when you want to import another HTML file’s layout/content into your current HTML but keep your current design system"
search_terms: ["html-content-and-layout-import-into-existing-design-system", "design", "style-transfer", "content", "current-design-system", "html", "import", "import-layout", "layout", "merge-content"]
inputs: ["TARGET_HTML", "SOURCE_HTML"]
output: "Complete target HTML with the imported experience expressed in the target design system."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["wordpress-admin-dashboard-migration-into-existing-plugin-design-system", "style-guided-redesign"]
aliases: ["design/design-system-style-transfer/html-content-and-layout-import-into-existing-design-system.md", "html-content-and-layout-import-into-existing-design-system.md"]
---

# HTML Content and Layout Import Into Existing Design System

Use when you want to import another HTML file’s layout/content into your current HTML but keep your current design system.

**Type:** prompt · **Mode:** edit · **ID:** `html-content-and-layout-import-into-existing-design-system`

**Expected output:** Complete target HTML with the imported experience expressed in the target design system.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_HTML}}` | Current HTML with the correct design system. | target-dashboard.html |
| `{{SOURCE_HTML}}` | HTML containing the required layout, content, and controls. | source-dashboard.html |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Current target implementation:
{{TARGET_HTML}}

Source layout and content:
{{SOURCE_HTML}}

Import the relevant source structure, content, controls, fields, labels, options, sections, flows, and functional intent into the target while retaining the target's design system and implementation architecture.

Authority:
- Target: CSS, tokens, components, naming conventions, JavaScript patterns, and responsive behavior.
- Source: required content, layout intent, fields, controls, and user flow.

Inspect both files and map source requirements onto existing target components. Do not blindly copy source CSS, colors, variables, fonts, shadows, spacing, button styles, resets, scripts, or visual identity. Reimplement required interactions using target patterns; do not drop behavior merely because source scripts are excluded.

Preserve unrelated target content and working functionality. Reuse components before deriving a new compatible pattern. Verify imported content, interaction coverage, hook integrity, and responsive layout.

Return the full updated target HTML. Include separate CSS or JavaScript only when unavoidable, with correct references from the HTML.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [WordPress Admin Dashboard Migration Into Existing Plugin Design System](../dashboard-migration/wordpress-admin-dashboard-migration-into-existing-plugin-design-system.md) — Use when migrating one plugin/admin dashboard into another while keeping the target plugin design system.
- [Style-Guided Redesign](style-guided-redesign.md) — Use when the target page should be structurally redesigned, but inside the reference style system.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
