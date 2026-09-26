---
id: "implement-spec-into-existing-html-with-design-system"
title: "Implement a Spec Into Existing HTML"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "page-builds"
when_to_use: "Add a specified feature to an existing interface while preserving its architecture and design system"
search_terms: ["implement-spec-into-existing-html-with-design-system", "design", "page-builds"]
inputs: ["TARGET_HTML", "DESIGN_SYSTEM", "IMPLEMENTATION_SPEC"]
output: "The full updated target HTML, with only required placement or blocking notes as permitted by the contract."
mode: "edit"
capabilities: ["file-access", "browser-when-available"]
related: ["build-html-page-from-scope-and-design-system", "preserve-existing-system", "design-system-compliance-audit-and-fix"]
aliases: ["design/implement-spec-into-existing-html-with-design-system.md", "implement-spec-into-existing-html-with-design-system.md"]
---

# Implement a Spec Into Existing HTML

Add a specified feature to an existing interface while preserving its architecture and design system.

**Type:** prompt · **Mode:** edit · **ID:** `implement-spec-into-existing-html-with-design-system`

**Expected output:** The full updated target HTML, with only required placement or blocking notes as permitted by the contract.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TARGET_HTML}}` | The complete existing page/interface. | dashboard.html |
| `{{DESIGN_SYSTEM}}` | The authoritative design rules and component reference. | design.md and existing component styles. |
| `{{IMPLEMENTATION_SPEC}}` | The approved feature requirements and acceptance criteria. | billing-tab-spec.md |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Target HTML:
{{TARGET_HTML}}

Design rules:
{{DESIGN_SYSTEM}}

Implementation requirements:
{{IMPLEMENTATION_SPEC}}

You will receive three files:

1. Target HTML file  
   The existing interface or dashboard that must be updated.

2. Design system file  
   The visual rules, tokens, layout patterns, spacing, typography, components, and interaction style that must be preserved.

3. Implementation spec file  
   The feature, page, tab, section, workflow, or content specification that must be implemented into the target HTML.

Task:
Update the target HTML file by implementing the requirements from the implementation spec while preserving the design system and existing interface architecture.

Use the target HTML file as the source of truth for:
- existing structure
- existing layout patterns
- existing components
- existing classes
- existing IDs
- existing data attributes
- existing JavaScript behavior
- existing responsive behavior
- existing content that is not part of the requested change

Use the design system file as the source of truth for:
- colors
- typography
- spacing
- card styles
- table styles
- button styles
- form styles
- navigation patterns
- layout density
- border/radius rules
- status badges
- empty states
- responsive rules
- interaction style
- visual constraints

Use the implementation spec file as the source of truth for:
- what must be added
- what must be updated
- what each page, tab, section, or component should contain
- required data fields
- required actions
- required states
- information hierarchy
- display logic
- disabled/unavailable states
- acceptance criteria

Before editing, inspect all three files carefully.

First determine:
- which parts of the HTML already exist and should be reused
- which sections need to be replaced, expanded, or corrected
- which requirements from the spec map to existing components
- which new components are required
- which existing styles/classes should be reused
- which JavaScript state, routing, tabs, actions, or data structures must be updated
- which IDs, hooks, and data attributes must be preserved
- which functionality is already implemented and must not be broken

Implementation rules:
- Do not redesign the whole interface.
- Do not introduce a new design system.
- Do not add unrelated features.
- Do not invent data, claims, metrics, actions, or statuses that are not provided by the spec or required solely to demonstrate an explicitly requested UI state; label all demonstration data.
- Do not remove existing working functionality unless the spec explicitly requires it.
- Do not rename existing IDs, classes, data attributes, or JavaScript hooks unless a required spec change makes that unavoidable; identify and update affected references without unrelated renaming.
- If you must rename or restructure something, update every related reference.
- Reuse existing components before creating new ones.
- New UI must look native to the existing HTML and design system.
- New sections must follow the existing spacing, density, typography, card, table, badge, button, and responsive patterns.
- Preserve the current app/page architecture.
- Keep global navigation, local navigation, page state, modals, filters, tables, forms, and actions consistent with the existing system.

When implementing the spec:
- Map each requirement into the correct page, tab, section, table, card, modal, drawer, or action.
- Use clear headings and labels.
- Add empty states where records are missing.
- Show unavailable or unsupported data honestly instead of fabricating values.
- Distinguish live/runtime data, cached/module data, billing/account data, and unavailable data where the spec requires that distinction.
- Add confirmation flows for destructive or service-impacting actions where required.
- Keep account-level views separate from selected-item or service-specific views.
- Avoid duplicated information unless the spec clearly requires summary plus detail views.
- Ensure every visible action either works in the current mockup context, opens the correct workflow, shows a disabled/unavailable state, or routes to the correct existing section.

CSS rules:
- Reuse existing CSS variables and component classes first.
- Add new CSS only when the existing system does not already cover the required component.
- Keep new CSS scoped and consistent with the existing naming conventions.
- Do not add broad global resets.
- Do not add decorative styles that conflict with the design system.
- Do not use heavy shadows, gradients, glass effects, oversized decorative UI, or unrelated accent colors unless the design system already uses them.

JavaScript rules:
- Preserve existing state management and event handling patterns.
- Add only the JavaScript required for the new or updated functionality.
- Keep actions, tab changes, filters, modals, dropdowns, confirmations, and toasts consistent with the existing implementation style.
- Do not break existing search, navigation, theme, modal, table, filter, or service-selection behavior.
- Keep placeholder/demo actions honest and clearly scoped when real backend integration is not present.

Responsive rules:
- Preserve the existing desktop, tablet, and mobile behavior.
- Ensure new sections stack correctly on smaller screens.
- Keep tables horizontally scrollable where needed.
- Keep controls usable on mobile.
- Do not introduce layouts that only work at desktop width.

Output requirements:
Return the full updated HTML file only.

Do not return fragments.
Do not return a diff.
Do not return a summary instead of the file.
Do not explain the design theory.
Do not include unrelated commentary.

Before returning the final HTML, perform a strict self-review:

1. Every requirement from the implementation spec has been mapped or intentionally marked unavailable.
2. The target HTML structure and existing behavior are preserved.
3. The design system is followed accurately.
4. New UI feels native to the existing interface.
5. No unrelated features were added.
6. No existing working behavior was broken.
7. IDs, classes, data attributes, and JavaScript hooks remain stable.
8. Empty, unavailable, loading, disabled, and destructive states are handled properly.
9. Desktop, tablet, and mobile layouts still work.
10. The final output is a complete paste-ready HTML file.

### Source conflicts and completion

The spec authorizes the functional change, the design system controls its presentation, and the target protects unrelated structure and behavior. Do not silently resolve a material contradiction by discarding one source. Missing data should use the specified disabled, empty, or unavailable state, not a fabricated working backend. If the files or an essential decision are missing, identify the blocker rather than returning a falsely complete interface. Report only verification that was performed; preserve the successful output contract above.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `browser-when-available`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Build an HTML Page From Scope and Design Rules](build-html-page-from-scope-and-design-system.md) — Build one standalone HTML page using separate content requirements and visual design rules.
- [Preserve Existing System](../../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Audit and Implement Design-System Compliance](../quality/design-system-compliance-audit-and-fix.md) — Extract atomic design requirements, implement them in controlled passes, and score only verified compliance.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
