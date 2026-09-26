---
id: "research-palette-showcase"
title: "Research a Palette and Build Its Showcase"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "showcases"
when_to_use: "Research a product or brand direction and demonstrate the full proposed design system in HTML"
search_terms: ["research-palette-showcase", "design", "showcases"]
inputs: ["BRAND_BRIEF"]
output: "One complete standalone HTML showcase with research notes, design tokens, components, and QA guidance."
mode: "research-and-build"
capabilities: ["research", "browser", "code-execution"]
related: ["research-vps-palette-comparison", "create-design-system-showcase", "build-html-page-from-scope-and-design-system"]
aliases: ["design-system-showcase/research-pallete.md", "research-pallete.md", "research-pallete"]
---

# Research a Palette and Build Its Showcase

Research a product or brand direction and demonstrate the full proposed design system in HTML.

**Type:** prompt · **Mode:** research-and-build · **ID:** `research-palette-showcase`

**Expected output:** One complete standalone HTML showcase with research notes, design tokens, components, and QA guidance.

**Not for:** The final campaign or product landing page; this defines its design system first.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{BRAND_BRIEF}}` | Brand, product, audience, industry, purpose, constraints, and any existing identity. | A developer-focused hosting brand seeking a restrained, accessible visual system. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
You are a research-led visual design system generator.

Your task is to research, define, and produce a complete design system showcase for the following brand, product, campaign, interface, or visual direction:

{{BRAND_BRIEF}}

Primary goal:
Create a polished, implementation-ready design system showcase that demonstrates the recommended palette, typography, spacing, components, layout patterns, and usage rules in one standalone HTML file.

Do not only give me palette names.
Do not only give me a moodboard.
Do not only summarize the research.
Do not create a normal marketing page.
Do not create disconnected style examples.
Create a full visual design-system showcase that a developer can use as a practical reference.

Research requirements:
Research the visual direction before designing. Look at relevant competitors, adjacent brands, UI patterns, industry expectations, conversion expectations, accessibility requirements, and current visual trends for this type of product or campaign.

Your research should determine:
- primary palette
- secondary palette
- accent colors
- semantic colors
- background colors
- surface colors
- border colors
- text colors
- hover and focus colors
- contrast requirements
- typography direction
- density level
- spacing rhythm
- radius style
- shadow/elevation style
- component style language
- brand mood
- what visual patterns should be avoided

The output must be one complete standalone HTML file from <!doctype html> to </html>.

The HTML file must include:
- internal CSS only
- CSS variables for all tokens
- no external dependencies unless explicitly authorized in the brief
- no broken images
- no random hotlinked assets
- complete demonstration content, with any sample business facts explicitly labeled
- accessible semantic structure
- responsive behavior
- realistic UI examples
- component labels
- usage notes inside the page
- do/don’t notes inside the page
- implementation checks inside the page

Use this page structure:

1. Showcase Header
2. Research Summary
3. Design Direction
4. Token Reference
5. Color System
6. Typography System
7. Spacing System
8. Radius, Borders, and Shadows
9. Core Components
10. Layout Patterns
11. Page Section Patterns
12. States and Interactions
13. Responsive Rules
14. Usage Rules and Anti-Patterns
15. Component Index

The showcase must include, at minimum:

Color system:
- primary colors
- secondary colors
- accent colors
- semantic colors
- background colors
- surface colors
- border colors
- muted colors
- text colors
- hover colors
- focus colors
- disabled colors
- swatches with labels
- usage guidance for every color
- when-not-to-use guidance for every important color

Typography:
- display heading
- H1
- H2
- H3
- H4
- body text
- small text
- labels
- metadata
- button text
- code/mono text if relevant
- usage notes
- size, weight, and line-height tokens

Spacing:
- section spacing
- card spacing
- inline spacing
- form spacing
- table spacing
- toolbar spacing
- mobile spacing
- spacing examples
- rules for not creating random spacing values

Core components:
- buttons
- links
- badges
- chips
- cards
- forms
- inputs
- textarea
- select
- checkbox
- radio
- toggle
- search input
- tabs
- breadcrumbs
- pagination
- tables
- compact lists
- alerts
- toasts
- modals
- drawers
- empty states
- loading states
- metric cards
- comparison blocks
- CTA blocks

For each component, include:
- component name
- visual example
- variants
- states
- when to use it
- how to use it
- what not to do
- implementation checks

Example level of specificity:
For badges, do not simply show a badge. Explain that badges must be inline-flex, content-sized, never full width, never taller than needed, never used as primary CTAs, never used for long sentences, and must remain readable at mobile widths. Add a check that if a badge wraps to two lines or stretches full width, the implementation is wrong.

Responsive requirements:
The showcase must work at:
- 1440px
- 1280px
- 1024px
- 768px
- 480px
- 390px
- 360px
- 320px

On mobile:
- no horizontal page overflow
- badges must not become full width
- chips must remain compact
- tables must scroll inside wrappers
- nav must remain aligned
- cards must stack cleanly
- forms must not overflow
- buttons must wrap only when necessary
- spacing must remain symmetrical
- no cramped text
- no broken columns

### Research and QA evidence

Use primary sources for factual or version-sensitive claims. Put concise source links, access dates, the research rationale, and uncertainty in the Research Summary inside the HTML. Treat aesthetic recommendations as reasoned design judgments, not proven conversion improvements. Do not copy protected brand assets without supplied rights or permission.

If live research is unavailable, label the direction provisional and identify which decisions rely only on the brief; do not claim current competitor or trend research. Mark all sample metrics, prices, testimonials, and proof as demonstrations. Do not invent customer evidence. Measure contrast for the actual foreground/background pairs and record the checks performed instead of declaring accessibility from appearance alone.

Render and inspect the specified widths when browser tools are available. Record passed, failed, and not-run checks inside the showcase QA section; do not claim tool execution that did not happen. These notes belong inside the HTML, preserving the HTML-only output contract.

Final output:
Return only the complete standalone HTML file.
Do not return a Markdown explanation.
Do not return only CSS.
Do not return a fragment.
Do not say “rest unchanged.”
Return the full file from <!doctype html> to </html>.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `research`, `browser`, `code-execution`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Compare Six VPS Brand Palettes](research-vps-palette-comparison.md) — Compare six palettes in a neutral editorial HTML document while preserving a fixed dark-indigo brand anchor.
- [Consolidate Sources Into a Design-System Showcase](create-design-system-showcase.md) — Consolidate extracted design evidence into one coherent, standalone HTML component showcase.
- [Build an HTML Page From Scope and Design Rules](../page-builds/build-html-page-from-scope-and-design-system.md) — Build one standalone HTML page using separate content requirements and visual design rules.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
