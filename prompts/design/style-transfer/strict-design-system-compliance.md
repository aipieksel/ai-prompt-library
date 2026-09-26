---
id: "strict-design-system-compliance"
title: "Strict Design System Compliance"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "style-transfer"
when_to_use: "Use when the agent should polish within an existing design system, not invent a new style"
search_terms: ["strict-design-system-compliance", "design", "style-transfer", "compliance", "design-system", "no-new-style", "polish", "strict", "system", "tokens"]
inputs: ["DESIGN_SYSTEM", "TASK"]
output: "A scoped polish pass using only approved design rules."
mode: "edit"
capabilities: ["file-access", "visual-inspection"]
related: ["design-system-compliance-audit-and-fix", "preserve-existing-system"]
aliases: ["design/design-system-style-transfer/strict-design-system-compliance.md", "strict-design-system-compliance.md"]
---

# Strict Design System Compliance

Use when the agent should polish within an existing design system, not invent a new style.

**Type:** prompt · **Mode:** edit · **ID:** `strict-design-system-compliance`

**Expected output:** A scoped polish pass using only approved design rules.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{DESIGN_SYSTEM}}` | Approved design-system document or implementation. | DESIGN.md and shared.css |
| `{{TASK}}` | Specific polish or compliance request. | Fix inconsistent table density and button alignment. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Design-system reference:
{{DESIGN_SYSTEM}}

Improvement request:
{{TASK}}

Polish the requested interface strictly within the existing design system. Inspect the reference and the affected implementation before changing anything.

Reuse current tokens, spacing, radius, typography, components, states, interaction patterns, buttons, cards, forms, and visual language. Improve alignment, visual rhythm, hierarchy, responsive behavior, and balance only within those rules.

Do not introduce new colors, typography, gradients, shadows, radii, spacing values, or component patterns. Preserve required content, functionality, and layout architecture. If the request cannot be achieved within the system, identify the precise conflict rather than silently inventing an exception.

Return the scoped implementation and the design rules checked. Report visual or runtime checks that could not be performed.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Audit and Implement Design-System Compliance](../quality/design-system-compliance-audit-and-fix.md) — Extract atomic design requirements, implement them in controlled passes, and score only verified compliance.
- [Preserve Existing System](../../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
