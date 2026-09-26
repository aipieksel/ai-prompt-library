---
id: "research-vps-palette-comparison"
title: "Compare Six VPS Brand Palettes"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "showcases"
when_to_use: "Compare six palettes in a neutral editorial HTML document while preserving a fixed dark-indigo brand anchor"
search_terms: ["research-vps-palette-comparison", "design", "showcases", "palette", "pallete", "six palettes", "indigo", "neutral", "comparison"]
inputs: ["PALETTE_BRIEF", "PREVIOUS_ATTEMPTS"]
output: "A brief list of avoided patterns followed by one complete neutral HTML document comparing exactly six palettes."
mode: "research-and-build"
capabilities: ["research", "file-access", "browser", "code-execution"]
related: ["research-palette-showcase", "research-campaign-design-system", "extend-vps-design-system-showcase"]
aliases: ["design-system-showcase/research-vps-company-pallete.md", "research-vps-company-pallete.md", "research-vps-company-pallete"]
---

# Compare Six VPS Brand Palettes

Compare six palettes in a neutral editorial HTML document while preserving a fixed dark-indigo brand anchor.

**Type:** prompt · **Mode:** research-and-build · **ID:** `research-vps-palette-comparison`

**Expected output:** A brief list of avoided patterns followed by one complete neutral HTML document comparing exactly six palettes.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{PALETTE_BRIEF}}` | VPS audience, brand constraints, fixed indigo value, and any six-palette research. | Example Hosting palette comparison; fixed brand anchor #020281; developer audience. |
| `{{PREVIOUS_ATTEMPTS}}` | Earlier comparison HTML files and observed issues, or None. | None |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
VPS brand brief and existing palette research (None for missing optional research):
{{PALETTE_BRIEF}}

Previous comparison HTML files, if any:
{{PREVIOUS_ATTEMPTS}}

Keep the existing dark-indigo brand anchor fixed. Use the approved value in the brief; for the original Example Hosting example that value is #020281. Research or complete exactly six palettes around the authorized anchor and clearly distinguish supplied palette data from new recommendations. Do not silently replace existing six-palette research when it has been provided.

Use a neutral, responsive comparison document with internal CSS and no required external assets or libraries. System fonts are the default; use a named font such as Inter only when already available or explicitly approved. Place dated research links and contrast-check evidence inside the document. When research or browser tools are unavailable, label the relevant conclusions or checks provisional/not run.

Create a completely new design-system showcase for the colour palette research.

Important: do not reuse the style, structure, visual language, spacing, effects, components, or layout patterns from the supplied previous HTML files, if any.

This is not a landing page.
This is not a dashboard.
This is not a command deck.
This is not a futuristic cloud UI.
This is not a SaaS hero page.
This is not a decorative portfolio piece.

It must be a clean, neutral, professional palette evaluation document in HTML.

Design direction:
Use a calm editorial / Swiss-style / design-document layout.
Think: Figma design system documentation, Stripe-quality internal design notes, high-end brand guideline PDF, clean product design audit.
The page should feel precise, quiet, spacious, and easy to scan.

Hard visual restrictions:
- No giant hero section.
- No fake terminal blocks.
- No server cards.
- No dashboard shell.
- No dark app frame.
- No glassmorphism.
- No glowing blobs.
- No radial-gradient backgrounds.
- No decorative grid overlays.
- No fake metrics.
- No exaggerated shadows.
- No huge gradient headlines.
- No “AI SaaS” visual clichés.
- No random pills everywhere.
- No over-designed cards.
- No cluttered bento layout.
- No theatrical copy like “command deck”, “deploy”, “audit”, “cockpit”, or “system online”.
- No page design that visually competes with the colour palettes.

Required layout:
- Use a simple fixed-width content container.
- Use a plain light background, preferably #f7f8fb or #ffffff.
- Use a clean header with title, short description, and metadata.
- Use a sticky or simple table of contents only if it stays visually quiet.
- Use clear sections with generous whitespace.
- Use thin borders instead of heavy shadows.
- Use one typeface system, preferably Inter or system-ui.
- Use restrained heading sizes.
- Use tables where comparison is needed.
- Use swatch strips, token tables, and compact preview blocks.
- Keep the showcase neutral so the palettes themselves are the focus.

Required content structure:
1. Executive summary
   - What was researched
   - The fixed dark indigo requirement
   - The best overall recommendation
   - The best secondary / technical recommendation

2. Palette comparison overview
   - Show all six palettes in a clean grid
   - Each palette card should include:
     - Palette name
     - Strategic purpose
     - 5–8 colour swatches
     - Best use cases
     - Risk / caution
   - Cards must be neutral and consistent. Do not style each card like a mini landing page.

3. Top two recommendation section
   - Compare the top two palettes side by side
   - Explain why one is the primary recommendation
   - Explain where the second one should be used
   - Use a clean comparison table

4. Token tables
   - For each recommended palette, show:
     - primary
     - primary-hover
     - primary-soft
     - secondary
     - accent
     - background
     - surface
     - border
     - text-primary
     - text-muted
     - link
     - cta
     - success
     - warning
     - error
     - focus
     - code/background if relevant
   - Include colour swatch, hex value, usage, and do-not-use guidance.

5. Component colour usage
   - Show compact neutral examples of:
     - button states
     - badge
     - pricing card
     - form field
     - alert
     - table
     - code block
   - These must be examples only, not a fake landing page.

6. Marketing application preview
   - Show small wireframe-style blocks for:
     - hero
     - pricing
     - feature grid
     - comparison table
     - CTA strip
   - Keep these previews minimal and neutral.
   - Do not turn them into full page designs.

7. Usage rules and QA checklist
   - What to do
   - What not to do
   - Implementation checks
   - Accessibility checks
   - Contrast checks
   - Mobile checks

Visual quality bar:
The page should feel like a serious internal brand decision document, not AI-generated eye candy.

Use this visual style:
- Background: light neutral
- Section background: white
- Borders: #e5e7eb or similar
- Text: dark neutral
- Muted text: grey-blue
- Spacing: generous but not dramatic
- Cards: simple, flat, consistent
- Swatches: clear labels, hex values, consistent sizing
- Tables: clean, readable, minimal
- Typography: restrained, precise, professional

Acceptance criteria:
- I can compare all six palettes quickly without being distracted by the showcase design.
- The showcase does not look like a SaaS landing page.
- The showcase does not contain fake dashboard/terminal/server visuals.
- The HTML is clean and implementation-friendly.
- The design is neutral enough that the palettes are the hero.
- The page feels like a useful design-system document, not an AI-generated website mockup.
- If any decorative element does not improve comparison or understanding, remove it.

Final instruction:
Review any supplied previous files and list the patterns you are avoiding in a short note before the HTML. When none were provided, state that fact and use the anti-pattern rules above. Then return the full standalone HTML from <!doctype html> through </html>. Do not imply that unavailable previous files were reviewed.
````
<!-- prompt:end -->

## Usage notes

The document shell is intentionally neutral; only the palette and compact component examples express the alternatives.

**Relevant capabilities:** `research`, `file-access`, `browser`, `code-execution`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Research a Palette and Build Its Showcase](research-palette-showcase.md) — Research a product or brand direction and demonstrate the full proposed design system in HTML.
- [Research a Campaign Design System](research-campaign-design-system.md) — Define a campaign-specific visual and conversion system before building the campaign landing page.
- [Extend a Showcase With VPS Website Components](extend-vps-design-system-showcase.md) — Extend an existing dashboard showcase with a complete VPS website component layer and updated documentation.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
