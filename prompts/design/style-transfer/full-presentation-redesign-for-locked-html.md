---
id: "full-presentation-redesign-for-locked-html"
title: "Full Presentation Redesign for Locked HTML"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when prior CSS redesign only changed variables and did not materially improve the interface"
search_terms: ["full-presentation-redesign-for-locked-html", "design", "style-transfer", "css-delta", "css-redesign", "full-presentation", "html", "locked", "locked-html", "presentation"]
inputs: ["TARGET_HTML", "DIRECTION"]
output: "Complete updated HTML, or a minimal selector-level CSS delta for separate-file delivery."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["css-architecture-redesign-without-markup-change", "visual-verification"]
aliases: ["design/design-system-style-transfer/full-presentation-redesign-for-locked-html.md", "full-presentation-redesign-for-locked-html.md"]
---

# Full Presentation Redesign for Locked HTML

Use when prior CSS redesign only changed variables and did not materially improve the interface.

**Type:** prompt · **Mode:** edit · **ID:** `full-presentation-redesign-for-locked-html`

**Expected output:** Complete updated HTML, or a minimal selector-level CSS delta for separate-file delivery.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_HTML}}` | Target HTML whose markup is locked. | locked-dashboard.html |
| `{{DIRECTION}}` | Desired design system or correction. | Apply the reference density, component proportions, states, and surface hierarchy. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Locked HTML:
{{TARGET_HTML}}

Visual direction or reference:
{{DIRECTION}}

Perform a full selector-level CSS redesign without changing the HTML markup, content, hooks, scripts, or behavior. Use this as a corrective pass when earlier work merely changed colors or appended superficial theme overrides.

Inspect the existing cascade and identify the selectors controlling the shell, sidebar, navigation, content, cards, forms, buttons, tables, lists, panels, modals, toasts, selected/hover/focus states, and responsive behavior. Update the actual component presentation so the result is visibly more than the old page with another palette.

Use tokens where useful, but do not rely on tokens alone. Preserve all visible content and interaction affordances. Do not hide or visually reorder content to work around the markup lock. Report any requirement that truly needs a markup change.

For an embedded-CSS target, return the complete updated HTML. When separate-file output is requested, return only a token file if needed and a CSS delta containing changed or new selector-level declarations; do not duplicate the entire original stylesheet. Explain load order only where needed to apply the delta.

Verify that unchanged markup plus the new cascade produces the intended components at the relevant responsive sizes. Distinguish visual checks from static inspection.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [CSS Architecture Redesign Without Markup Change](css-architecture-redesign-without-markup-change.md) — Use when the HTML must stay locked but the visual presentation needs a real CSS redesign.
- [Visual Verification](../redesign/visual-verification.md) — Use after UI changes when the agent should compare the result visually and fix issues.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
