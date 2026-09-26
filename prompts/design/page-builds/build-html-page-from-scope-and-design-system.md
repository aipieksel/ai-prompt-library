---
id: "build-html-page-from-scope-and-design-system"
title: "Build an HTML Page From Scope and Design Rules"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "page-builds"
when_to_use: "Build one standalone HTML page using separate content requirements and visual design rules"
search_terms: ["build-html-page-from-scope-and-design-system", "design", "page-builds"]
inputs: ["SOURCE_FILES"]
output: "One complete standalone HTML file; no summary on success."
mode: "build"
capabilities: ["file-access", "browser-when-available", "research-when-needed"]
related: ["implement-page-from-markdown-wireframe-and-reference-html", "implement-spec-into-existing-html-with-design-system", "assess-html-publish-readiness"]
aliases: ["design/build-html-page-from-scope-and-design-system.md", "build-html-page-from-scope-and-design-system.md"]
---

# Build an HTML Page From Scope and Design Rules

Build one standalone HTML page using separate content requirements and visual design rules.

**Type:** prompt · **Mode:** build · **ID:** `build-html-page-from-scope-and-design-system`

**Expected output:** One complete standalone HTML file; no summary on success.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{SOURCE_FILES}}` | Both complete sources, with roles; identify by contents rather than filenames alone. | scope.md: page content and requirements; design.md: visual rules. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Source files and their intended roles:
{{SOURCE_FILES}}

You will receive two source files. The file names may vary, so do not rely on exact names like design.md or scope.md. Instead, identify the role of each file by its content.

Source file roles:

1. Design reference file
   This file defines the visual system, brand rules, component patterns, layout rhythm, typography, colors, spacing, buttons, cards, sections, responsive behavior, and implementation constraints.

2. Page scope file
   This file defines the page to build: purpose, target audience, required sections, content requirements, SEO requirements, CTA requirements, links, factual boundaries, product positioning, technical requirements, and acceptance criteria.

Task:
Build one complete HTML page from the page scope file using the design reference file as the visual and structural source of truth.

Before building, inspect both files and determine which one is the design reference and which one is the page scope. Do not assume this from the file name alone.

Use the page scope file as the source of truth for:
- page purpose
- target audience
- search intent
- required sections
- required headings
- required copy points
- required CTAs and links
- product positioning
- factual boundaries
- unsupported-claim restrictions
- disclaimers
- internal links
- FAQ content
- conversion goals
- technical/page-quality requirements

Use the design reference file as the source of truth for:
- colors
- typography
- spacing
- buttons
- cards
- section rhythm
- containers
- grids
- hero patterns
- pricing/product patterns
- feature sections
- setup/workflow sections
- comparison tables
- FAQ patterns
- CTA sections
- responsive behavior
- visual constraints

If the two files conflict:
- Content, claims, links, required sections, and factual boundaries come from the page scope file.
- Visual design, layout style, typography, components, and spacing come from the design reference file.
- Do not invent missing claims or features to resolve conflicts.

Implementation rules:
- Build a complete, standalone HTML file.
- Follow the design reference for visual rules while keeping all scope-required content and sections.
- Do not invent a new visual brand.
- Do not introduce unrelated CSS frameworks, external UI libraries, or unnecessary JavaScript.
- Do not add unsupported product claims, fake data, fake reviews, fake metrics, or unsupported integrations.
- Do not ignore required sections from the page scope.
- Do not turn the page into a generic template.
- Do not use generic filler copy.
- Do not overload the page with unnecessary cards or repeated sections.
- Keep the page commercially sharp, readable, responsive, and practical.
- Preserve the scope’s factual boundaries exactly.
- Use concise, high-signal copy.
- Use semantic HTML and proper heading hierarchy.
- Use accessible links, buttons, labels, and alt text where needed.
- Keep mobile readability strong.
- Keep the final page visually native to the design reference.

Component selection rules:
- Use the design reference’s hero pattern for the page opener.
- Use feature cards only for true benefits or capabilities.
- Use product/pricing components when the scope includes plan recommendations or pricing.
- Use setup-flow/workflow patterns when the scope includes steps or commands.
- Use comparison tables when the scope includes side-by-side decisions.
- Use FAQ patterns for FAQ content.
- Use CTA sections for final conversion blocks.
- Use internal-products or related-links patterns only where the scope requires related next steps.
- Do not force every section into the same card grid.
- Select the component pattern that best matches the content’s purpose, not merely the closest visual shape.

Content rules:
- Keep required H1s, CTAs, links, product names, pricing references, factual claims, and compliance boundaries from the page scope file.
- Improve flow and clarity where needed, but do not change the meaning.
- Do not remove required disclaimers.
- Do not let disclaimers dominate the page unless the scope requires it.
- Make every major section directly support the page goal.
- Keep page copy specific to the target topic in the page scope file.
- Remove repetition where possible without removing required meaning.
- Do not add unrelated sections just because the design reference contains them.

CSS rules:
- Use the tokens and component language from the design reference.
- Prefer existing design-system values over hardcoded arbitrary styles.
- Keep CSS organized and maintainable.
- Avoid heavy shadows, unrelated gradients, oversized decorative elements, or off-brand effects unless the design reference explicitly supports them.
- Keep section spacing, card radius, button styles, typography, and colors consistent with the design reference.
- Do not create new design tokens unless the required page cannot be built without them.
- If new CSS is required, keep it minimal and aligned with the design reference.

Responsive rules:
- Build desktop, tablet, and mobile behavior intentionally.
- Stack grids cleanly on smaller screens.
- Keep CTAs visible and usable.
- Keep tables scrollable or simplified on mobile.
- Avoid horizontal overflow.
- Keep hero and visual sections readable on mobile.
- Ensure the final page does not depend on desktop-only layout assumptions.

Accuracy rules:
- If the page scope requires current external documentation verification and source access is available, verify it before finalizing the page.
- If source access is unavailable, preserve supported facts and required official-documentation references. Do not claim verification; report a blocker before producing final HTML when a required factual decision cannot be made safely.
- Do not claim capabilities that the page scope explicitly excludes.
- Do not add integrations, partnerships, guarantees, or managed services unless the page scope explicitly says they exist.

Build workflow:
1. Identify which file is the design reference and which file is the page scope.
2. Extract the required page sections from the page scope.
3. Extract the relevant visual/component patterns from the design reference.
4. Map every page section to the most appropriate component pattern.
5. Build the complete HTML page.
6. Check the page against the scope requirements.
7. Check the page against the design reference.
8. Refine the layout, copy density, responsiveness, and CTA clarity.
9. Return the final completed HTML file only.

Self-review before returning:
Check the completed page against these criteria:

1. Every required page-scope section is included.
2. Every required CTA and link is correct.
3. The page follows the design reference visually.
4. The page does not invent unsupported claims.
5. The page does not feel generic.
6. The hero clearly communicates the page offer.
7. The recommended product or primary action is obvious.
8. The section order is logical.
9. The copy is concise and conversion-focused.
10. The page is responsive.
11. The HTML is complete and paste-ready.
12. No unrelated features were added.
13. The implementation does not depend on exact file names.
14. The design reference controls the look.
15. The page scope controls the content and requirements.

Final output:
Return only the completed HTML file.

Do not return a summary.
Do not return fragments.
Do not return a diff.
Do not explain the design theory.
For a blocking missing input or unresolved conflict, return a precise blocker report instead of incomplete HTML. Do not append unrelated notes to a successful HTML deliverable.
````
<!-- prompt:end -->

## Usage notes

Use this when scope and visual rules are supplied separately. Use the three-source builder when an approved wireframe also controls structure.

**Relevant capabilities:** `file-access`, `browser-when-available`, `research-when-needed`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Implement Page from Markdown, Wireframe, and Reference HTML](implement-page-from-markdown-wireframe-and-reference-html.md) — You have a content Markdown file, an approved Balsamiq wireframe, and a reference HTML page, and you want the agent to implement the final page in the same website style.
- [Implement a Spec Into Existing HTML](implement-spec-into-existing-html-with-design-system.md) — Add a specified feature to an existing interface while preserving its architecture and design system.
- [Assess HTML Publish Readiness](../quality/assess-html-publish-readiness.md) — Assess an HTML page for SEO, conversion, credibility, factual safety, and publish readiness without editing it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
