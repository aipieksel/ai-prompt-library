---
id: "css-architecture-redesign-without-markup-change"
title: "CSS Architecture Redesign Without Markup Change"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when the HTML must stay locked but the visual presentation needs a real CSS redesign"
search_terms: ["css-architecture-redesign-without-markup-change", "design", "style-transfer", "architecture", "change", "css", "css-redesign", "locked-html", "markup", "not-variable-only"]
inputs: ["TARGET_HTML", "DIRECTION"]
output: "Complete HTML with CSS-only changes, or a stylesheet when explicitly requested."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["full-presentation-redesign-for-locked-html", "visual-verification"]
aliases: ["design/design-system-style-transfer/css-architecture-redesign-without-markup-change.md", "css-architecture-redesign-without-markup-change.md"]
---

# CSS Architecture Redesign Without Markup Change

Use when the HTML must stay locked but the visual presentation needs a real CSS redesign.

**Type:** prompt · **Mode:** edit · **ID:** `css-architecture-redesign-without-markup-change`

**Expected output:** Complete HTML with CSS-only changes, or a stylesheet when explicitly requested.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_HTML}}` | Complete target HTML with markup that must remain unchanged. | locked-interface.html |
| `{{DIRECTION}}` | Visual goal or approved reference. | A denser border-led interface with clearer hierarchy and less empty space. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
HTML with locked markup:
{{TARGET_HTML}}

Desired visual result:
{{DIRECTION}}

Redesign the full presentation layer through CSS only. Keep the DOM tree, element order, text, labels, fields, buttons, IDs, classes, data attributes, links, scripts, accessibility attributes, and functional behavior unchanged. Stylesheet content may change; markup hooks may not.

Inspect the actual selectors controlling the UI. This must be more than a root-variable swap: improve how tokens and selector-level rules create layout rhythm, spacing, typography hierarchy, surfaces, borders, shadows, backgrounds, panels, cards, buttons, inputs, navigation, overlays, accordions, sidebars, selected/hover/focus states, responsiveness, and motion.

Do not use CSS to hide required content, alter the logical reading order, or make controls unusable. If a requirement cannot be achieved without changing markup, identify the blocker rather than violating the lock.

Compare the before/after DOM excluding permitted stylesheet text. Review responsive and keyboard behavior and inspect rendered components when tools allow.

Return the complete HTML with updated embedded CSS. Return a separate stylesheet instead only when the task explicitly requests one.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Full Presentation Redesign for Locked HTML](full-presentation-redesign-for-locked-html.md) — Use when prior CSS redesign only changed variables and did not materially improve the interface.
- [Visual Verification](../redesign/visual-verification.md) — Use after UI changes when the agent should compare the result visually and fix issues.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
