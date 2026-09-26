---
id: "design-system-compliance-audit-and-fix"
title: "Audit and Implement Design-System Compliance"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "quality"
when_to_use: "Extract atomic design requirements, implement them in controlled passes, and score only verified compliance"
search_terms: ["design-system-compliance-audit-and-fix", "design", "quality", "scoring", "compliance matrix", "atomic checklist", "mac voice"]
inputs: ["DESIGN_SYSTEM", "IMPLEMENTATION_FILES"]
output: "Updated implementation, atomic compliance matrix, and an evidence-backed eleven-part report."
mode: "audit-and-edit"
capabilities: ["file-access", "code-execution", "browser"]
related: ["strict-design-system-compliance", "visual-verification", "implementation-handoff-docs-from-mockup-or-html"]
aliases: ["design/design-system-scoring-implementation.prompt.md", "design-system-scoring-implementation.prompt.md", "design-system-scoring-implementation", "design/design-system-scoring-implementation-mac-voice.prompt.md", "design-system-scoring-implementation-mac-voice.prompt.md", "design-system-scoring-implementation-mac-voice"]
---

# Audit and Implement Design-System Compliance

Extract atomic design requirements, implement them in controlled passes, and score only verified compliance.

**Type:** prompt · **Mode:** audit-and-edit · **ID:** `design-system-compliance-audit-and-fix`

**Expected output:** Updated implementation, atomic compliance matrix, and an evidence-backed eleven-part report.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{DESIGN_SYSTEM}}` | The complete authoritative visual and interaction requirements. | design.md |
| `{{IMPLEMENTATION_FILES}}` | The current source, affected pages/components, and edit boundary. | app/views/, shared styles, and the approved dashboard routes. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Authoritative design-system source:
{{DESIGN_SYSTEM}}

Implementation files and authorized scope:
{{IMPLEMENTATION_FILES}}

I have provided a design-system file for this project. Treat that file as the single source of truth for the visual design, layout rules, component behavior, responsive behavior, spacing, typography, colors, states, and interaction patterns.

Your task is to audit the current implementation and update it so the project follows the design-system file against explicit, testable requirements, preserving unrelated behavior.

Do not redesign the project.
Do not rebuild the project from scratch.
Do not invent new styles, colors, components, layouts, effects, or interactions.
Do not make creative improvements unless they are directly required by the design-system file.
Do not remove existing working functionality.
Do not change the information architecture unless the current structure directly conflicts with the design-system file.

Your job is to implement the design system exactly, systematically, and verifiably.

Before editing anything, do this:

1. Read the entire design-system file from top to bottom.

2. Extract every design requirement into an atomic checklist.

Do not create broad checklist items such as:

- Typography
- Colors
- Buttons
- Cards
- Tables
- Layout
- Responsive

Break every category into small, testable requirements.

For example, typography should become separate checklist items such as:

- Font family is implemented globally
- Font fallback stack matches the design file
- Body text size matches the design file
- Body line-height matches the design file
- Body letter-spacing matches the design file
- Page titles match the required size, weight, and line-height
- Section headings match the required size, weight, and line-height
- Card titles match the required size, weight, and line-height
- Table headers match the required typography
- Table cells match the required typography
- Buttons match the required typography
- Labels match the required typography
- Metadata text matches the required typography
- Monospace text is used only where the design system requires it

Do the same level of breakdown for every category in the design-system file, including but not limited to:

- Color tokens
- Theme modes
- Surface hierarchy
- Text hierarchy
- Border system
- Accent usage
- Status colors
- Typography
- Spacing scale
- Padding rules
- Gap rules
- Border radius
- Layout widths
- App shell
- Sidebar
- Topbar
- Page headers
- Section headers
- Cards
- Compact cards
- Metric cards
- Tables
- Data rows
- Filters
- Search fields
- Dropdowns/selectors
- Buttons
- Icon buttons
- Badges/status pills
- Progress bars
- Toolbars
- Popovers
- Modals
- Forms
- Inputs
- Textareas
- Empty states
- Alerts
- Panels
- Navigation states
- Hover states
- Active states
- Focus states
- Disabled states
- Loading states
- Error states
- Responsive behavior
- Mobile behavior
- Any project-specific component rules described in the file

3. Create a design-system compliance matrix before making changes.

Use this structure:

ID:
Category:
Exact requirement from design-system file:
Where this applies:
Current implementation:
Required change:
Files/components/selectors affected:
Verification method:
Status:
Score:

Scoring rules:

- Every checklist item starts at 0.
- Give 1 point only when the requirement is implemented and verified everywhere it applies.
- Do not give partial points.
- Do not mark an item complete if it is correct in one place but missing elsewhere.
- If a requirement does not apply to this project, mark it as Not Applicable and explain why.
- If a requirement cannot be verified, keep it at 0 and explain what is missing.
- Do not continue claiming completion unless the matrix supports it.

4. Implement the design system in controlled passes.

Use this order:

Pass 1: Global tokens and foundations
- Colors
- Theme variables
- Typography variables
- Font imports or font declarations
- Spacing scale
- Radius values
- Border values
- Motion values
- Global body styles
- Global focus styles
- Global text rendering rules

Pass 2: App structure and layout
- App shell
- Main content wrapper
- Sidebar structure
- Topbar structure
- Page width
- Page padding
- Responsive layout behavior
- Mobile sidebar behavior
- Any nested layout patterns required by the design system

Pass 3: Core components
- Buttons
- Inputs
- Selectors/dropdowns
- Search fields
- Cards
- Tables
- Badges
- Toolbars
- Tabs
- Navigation items
- Modals
- Popovers
- Alerts
- Empty states
- Progress bars
- Forms

Pass 4: Page-by-page implementation
- Review every page, tab, panel, section, and state.
- Apply the design-system requirements wherever relevant.
- Remove one-off styles that conflict with the system.
- Replace hardcoded values with design tokens where possible.
- Keep page purpose and existing functionality intact.

Pass 5: State and interaction audit
Verify all states required by the design system:

- Default
- Hover
- Active
- Selected
- Focus
- Disabled
- Loading
- Empty
- Error
- Warning
- Danger
- Success
- Info
- Mobile
- Tablet
- Desktop

Pass 6: Final visual consistency audit
Check for hidden mismatches, including:

- Wrong font family
- Browser default font still appearing
- Incorrect font weights
- Incorrect line heights
- Incorrect letter spacing
- Hardcoded colors outside the token system
- Incorrect surface hierarchy
- Overused accent color
- Missing borders
- Wrong border opacity
- Wrong border radius
- Incorrect padding
- Incorrect gaps
- Inconsistent card styling
- Inconsistent table row height
- Inconsistent button height
- Native controls where custom styled controls are required
- Missing focus states
- Weak or missing hover states
- Incorrect mobile stacking
- Broken responsive behavior
- Components that look close but do not actually follow the design tokens

Implementation rules:

- Use the design-system file as the authority.
- Preserve the existing project structure unless a structure directly violates the design system.
- Prefer central tokens, variables, utility classes, or shared component styles over repeating hardcoded values.
- Do not introduce new visual language.
- Do not add shadows, gradients, glass effects, oversized typography, decorative graphics, or new colors unless the design-system file explicitly allows them.
- Do not make the interface more decorative than the design system.
- Do not simplify dense operational layouts into oversized cards unless the design-system file says to do so.
- Do not fabricate missing data just to fill empty states.
- Do not remove useful labels, descriptions, metadata, table headers, or status indicators if the design system relies on them for clarity.
- Keep account-level/global views separate from item-level/detail/workspace views if the design system defines that distinction.
- Keep destructive, warning, and service-impacting actions visually distinct and properly confirmed.
- Maintain accessibility basics: visible focus states, readable contrast, labelled controls, keyboard-friendly interactions, and clear disabled states.

Important verification requirement:

After each checklist item is implemented, verify it in every relevant place before scoring it as complete.

For example:

If the design system says buttons are 36px high with 8px radius, verify every primary, secondary, ghost, danger, warning, modal, toolbar, table-action, and small button variant.

If the design system says cards use a specific surface, border, radius, and padding, verify every dashboard card, panel, table wrapper, modal body, sidebar card, metric card, and compact card.

If the design system says a specific font stack is required, verify the global body, headings, tables, buttons, labels, inputs, navigation, badges, and metadata.

Do not assume inheritance is working. Inspect the actual rendered result for visual/behavioral requirements; final CSS/class output alone can verify only source-level requirements. If a required browser check cannot run, keep the item unverified and scored 0.

Final response format:

When finished, provide a concise implementation report with:

1. Total checklist items extracted
2. Total items implemented and verified
3. Total items marked Not Applicable
4. Total applicable items not verified as compliant, split into known failures and unverified items
5. Overall compliance score
6. Compliance score by category
7. Files changed
8. Major fixes made
9. Remaining issues, if any
10. Anything that could not be verified
11. Any places where the current project structure prevented perfect compliance

Only say “fully implemented” if every applicable checklist item scores 1.

If anything remains incomplete, say exactly what remains incomplete and why.

### Score calculation and evidence

Assign 1 only after the entire atomic requirement passes in every applicable location. Assign 0 to both known failures and unverified applicable requirements; distinguish those statuses in the matrix. Exclude justified Not Applicable items from denominators.

Overall compliance = 100 × verified applicable items / all applicable items. Use the same formula per category. If there are no applicable items, report N/A rather than 100%. Round displayed percentages to one decimal, retain raw counts, and do not count a requirement twice. Attach the exact check or evidence to each verified row. The scores describe this checklist, not an external design-quality benchmark.

The 36px button height and 8px radius above are illustrative conditional examples, not new global values. Use actual values from the supplied design system. Do not invent requirements merely to fill the sample categories. If source files are missing or authority conflicts, report that blocker before making broad changes.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `code-execution`, `browser`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Strict Design System Compliance](../style-transfer/strict-design-system-compliance.md) — Use when the agent should polish within an existing design system, not invent a new style.
- [Visual Verification](../redesign/visual-verification.md) — Use after UI changes when the agent should compare the result visually and fix issues.
- [Create an Implementation Handoff](../handoff/implementation-handoff-docs-from-mockup-or-html.md) — Document an approved mockup or HTML interface as three build-ready Markdown specifications.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
