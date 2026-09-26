---
id: "visual-verification"
title: "Visual Verification"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "redesign"
when_to_use: "Use after UI changes when the agent should compare the result visually and fix issues"
search_terms: ["visual-verification", "design", "redesign", "alignment", "before-after", "responsive", "ui-polish", "verification", "visual", "visual-check"]
inputs: ["CONTEXT", "REFERENCES"]
output: "Visual findings, scoped corrections, and evidence of inspected views and states."
mode: "verify"
capabilities: ["visual-inspection"]
related: ["verify-before-returning", "design-system-compliance-audit-and-fix"]
aliases: ["design/visual-redesign/visual-verification.md", "visual-verification.md"]
---

# Visual Verification

Use after UI changes when the agent should compare the result visually and fix issues.

**Type:** prompt · **Mode:** verify · **ID:** `visual-verification`

**Expected output:** Visual findings, scoped corrections, and evidence of inspected views and states.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CONTEXT}}` | Changed interface, expected behavior, and allowed correction scope. | The updated dashboard table and date-column alignment. |
| `{{REFERENCES}}` | Before/after screenshots, source files, preview URL, and design rules. | Approved desktop/mobile screenshots and local preview URL. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
UI and change context:
{{CONTEXT}}

Before/after references and expected design:
{{REFERENCES}}

Visually verify the changed interface rather than relying only on code correctness.

Inspect the before and after states at the relevant desktop, tablet, and mobile widths. Compare content coverage, layout, spacing, alignment, hierarchy, typography, visual balance, component states, and responsive behavior against the intended design. Exercise affected controls and inspect keyboard focus, overlays, and overflow where applicable.

Separate an intentional approved difference from a regression. Fix issues within the authorized scope, then recheck the affected views and states.

Return the issues found, fixes made, views and widths checked, and any remaining limitations. Reference actual screenshots or evidence where available. If browser or image access is missing, report a static review as static; do not label it visual verification.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `visual-inspection`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Verify Before Returning](../../../modifiers/verify-before-returning.md) — Use when the agent should check its own work before returning it.
- [Audit and Implement Design-System Compliance](../quality/design-system-compliance-audit-and-fix.md) — Extract atomic design requirements, implement them in controlled passes, and score only verified compliance.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
