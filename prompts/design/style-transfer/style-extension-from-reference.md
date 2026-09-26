---
id: "style-extension-from-reference"
title: "Style Extension From Reference"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when one approved HTML section should become the visual source of truth for building more sections"
search_terms: ["style-extension-from-reference", "design", "style-transfer", "cohesive-sections", "design-system", "extend-page", "extension", "reference", "reference-style", "style"]
inputs: ["STYLE_REFERENCE", "TASK"]
output: "The requested new sections or interface implemented in the approved visual language."
mode: "build"
capabilities: ["file-access", "visual-inspection"]
related: ["style-transfer-extension", "design-system-page-build-from-request"]
aliases: ["design/design-system-style-transfer/style-extension-from-reference.md", "style-extension-from-reference.md"]
---

# Style Extension From Reference

Use when one approved HTML section should become the visual source of truth for building more sections.

**Type:** prompt · **Mode:** build · **ID:** `style-extension-from-reference`

**Expected output:** The requested new sections or interface implemented in the approved visual language.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{STYLE_REFERENCE}}` | Approved HTML/CSS section or page. | approved-hero.html |
| `{{TASK}}` | Sections or UI to extend from the approved style. | Add the required pricing comparison and FAQ sections. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Approved reference:
{{STYLE_REFERENCE}}

New sections or interface to build:
{{TASK}}

Extend the page or interface from the approved reference. Treat it as an implicit design system even when no separate token file or component library exists.

Inspect and reuse its palette, typography, spacing rhythm, radius, surfaces, shadows, buttons, cards, backgrounds, density, interaction style, hierarchy, and overall visual treatment. Preserve already-approved content and behavior.

Build the requested additions as part of the same design language, but vary composition according to each section's purpose. Extend the style, not the exact section: do not repeat the hero layout or component arrangement throughout the page.

Create only the requested additions. Identify any new derived pattern and keep it consistent with the reference. Return complete implementation files with the additions placed in context and verify visual consistency and responsive behavior where tools allow.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Style Transfer Extension](style-transfer-extension.md) — Use when you have a reference design file and a target page that needs to match that design language.
- [Design-System Page Build From Request](../page-builds/design-system-page-build-from-request.md) — Use when you want a new page/feature built from a request while using existing project variables and styles.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
