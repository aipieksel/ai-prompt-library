---
id: "implement-page-from-markdown-wireframe-and-reference-html"
title: "Implement Page from Markdown, Wireframe, and Reference HTML"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "page-builds"
when_to_use: "You have a content Markdown file, an approved Balsamiq wireframe, and a reference HTML page, and you want the agent to implement the final page in the same website style"
search_terms: ["implement-page-from-markdown-wireframe-and-reference-html", "design", "page-builds", "page build", "html implementation", "seo markdown", "balsamiq wireframe", "reference html", "design system", "website style"]
inputs: ["CONTENT_MARKDOWN", "APPROVED_WIREFRAME", "REFERENCE_HTML", "PAGE_NAME"]
output: "Full HTML and any required separate page-scoped CSS and JavaScript files."
mode: "build"
capabilities: ["file-access", "browser-when-available"]
related: ["seo-markdown-to-balsamiq-wireframe", "build-html-page-from-scope-and-design-system", "visual-verification"]
aliases: ["design/page-feature-builds/implement-page-from-markdown-wireframe-and-reference-html.md", "implement-page-from-markdown-wireframe-and-reference-html.md"]
---

# Implement Page from Markdown, Wireframe, and Reference HTML

You have a content Markdown file, an approved Balsamiq wireframe, and a reference HTML page, and you want the agent to implement the final page in the same website style.

**Type:** prompt · **Mode:** build · **ID:** `implement-page-from-markdown-wireframe-and-reference-html`

**Expected output:** Full HTML and any required separate page-scoped CSS and JavaScript files.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{CONTENT_MARKDOWN}}` | The approved copy, SEO requirements, factual boundaries, links, and CTAs. | approved-content.md |
| `{{APPROVED_WIREFRAME}}` | The approved structural wireframe, export, or detailed spec. | approved-wireframe.md |
| `{{REFERENCE_HTML}}` | The existing website HTML and required companion styles/assets. | reference-page.html and shared CSS. |
| `{{PAGE_NAME}}` | A lowercase kebab-case output stem without an extension. | linux-vps-guide |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Output filename stem (lowercase kebab-case, without extension):
{{PAGE_NAME}}

Implement the page using the approved SEO/content Markdown file, the approved Balsamiq wireframe, and the reference HTML page.

## Content source

{{CONTENT_MARKDOWN}}

## Approved wireframe

{{APPROVED_WIREFRAME}}

## Reference HTML / design source

{{REFERENCE_HTML}}

## Task

Create the final HTML implementation of the page.

Use the Markdown file as the source of truth for:

- page content
- SEO text
- headings
- section copy
- factual claims
- keyword direction
- FAQs
- CTAs
- links
- product/service messaging

Use the approved Balsamiq wireframe as the source of truth for:

- section order
- page structure
- layout flow
- content grouping
- hierarchy
- component placement
- CTA placement
- wireframed sections
- affordances and signifiers
- notes about how each section should work

Use the reference HTML as the source of truth for:

- visual style
- brand look and feel
- colors
- typography
- spacing rhythm
- section treatment
- card style
- button style
- form/input style if relevant
- badges and labels
- borders
- radius
- shadows
- gradients
- responsive behavior
- CSS variables
- component patterns
- naming conventions

Do not redesign the page from scratch. Do not create a new visual identity. Do not introduce unrelated styling. Build the new page so it looks like it belongs to the same website as the reference HTML.

Preserve the SEO/content Markdown wording as much as possible. Do not rewrite, shorten, remove, or invent important SEO copy unless the Markdown explicitly requires adaptation for layout. If content must be shortened for a card, preserve the meaning and keyword intent.

Translate the Balsamiq wireframe into real HTML sections using the reference HTML’s existing design system. If the wireframe shows a card, use the reference HTML’s card pattern. If it shows a CTA, use the reference HTML’s CTA/button pattern. If it shows a comparison, use the reference HTML’s table or comparison pattern if one exists. If it shows FAQ content, use the reference HTML’s FAQ pattern if one exists.

If the reference HTML does not contain a suitable existing section or component for something required by the Markdown or wireframe, create a new section or new element, but it must be designed inside the same visual language as the reference HTML. Any new section must use the same colors, spacing, typography, radius, buttons, cards, borders, shadows, gradients, layout rhythm, and responsive behavior patterns. New sections are allowed when needed, but they must feel native to the existing website and not like an unrelated design system.

Before implementing, inspect all three inputs and identify:

- the final section order
- which Markdown content belongs in each wireframe section
- which reference HTML components should be reused
- which new sections or elements are required because no suitable reference section exists
- which styles/classes/variables should be reused
- whether any new CSS is required
- whether any JavaScript is required
- which links, CTAs, and factual claims must remain unchanged

Implementation rules:

- Use the reference HTML’s CSS variables and existing classes wherever possible.
- Reuse existing section/component patterns before creating new ones.
- Create new sections or elements only when the wireframe or Markdown requires them and the reference HTML has no suitable equivalent.
- Any new HTML must follow the reference HTML’s naming conventions, structure, and visual style.
- Do not copy unused sections from the reference HTML.
- Do not copy unrelated content from the reference HTML.
- Do not add new product claims, pricing, locations, guarantees, specs, or features.
- Do not invent new CTAs or links unless required by the Markdown.
- Do not introduce a new CSS system.
- Do not add broad global CSS unless the reference HTML already uses that pattern.
- If new CSS is required, return it in a separate CSS file.
- If new JavaScript is required, return it in a separate JavaScript file.
- New CSS must be scoped to this page or its new sections and must reuse reference variables first.
- New JavaScript must be minimal, scoped, and consistent with the reference HTML’s patterns.
- Do not inline new CSS or JavaScript unless the reference HTML’s established pattern clearly requires inline code.
- Keep the HTML readable, semantic, maintainable, and implementation-ready.
- Make the page responsive on desktop, tablet, and mobile.
- Preserve accessibility basics such as semantic headings, link text, button text, alt text where relevant, and logical reading order.

## New CSS / JavaScript rules

If new CSS is required, create and return a separate CSS file named:

{{PAGE_NAME}}.css

If new JavaScript is required, create and return a separate JavaScript file named:

{{PAGE_NAME}}.js

The final HTML must link to the new CSS file and JavaScript file if they are required.

The new CSS file must contain only the additional styles required for this page. Do not duplicate the full reference CSS. Do not copy unused CSS. Do not create broad resets. Do not redefine the entire design system.

The new JavaScript file must contain only the behavior required for this page. Do not duplicate existing scripts. Do not rewrite unrelated interactions. Do not add broad global listeners unless unavoidable.

The final result should follow this priority order:

1. Accuracy to the Markdown content and SEO intent.
2. Fidelity to the approved Balsamiq wireframe structure.
3. Visual consistency with the reference HTML design system.
4. Clean, maintainable implementation.
5. Scoped, minimal new CSS or JavaScript only where needed.

Deliverables:

1. Return the full final HTML file.
2. Return a separate CSS file if new CSS was added.
3. Return a separate JavaScript file if new JavaScript was added.
4. Make sure the HTML links to the CSS and JavaScript files correctly.
5. Do not return fragments unless explicitly requested.
6. Do not include unrelated explanation.
7. Include a short implementation note only if needed to explain file placement or verification.

Before returning, verify:

- the Markdown content has been represented accurately
- the wireframe structure has been followed
- the reference HTML style controls the final look and feel
- existing reference components were reused where suitable
- new sections were created only where needed
- any new sections feel native to the reference design system
- no unrelated design system was introduced
- no unsupported claims were added
- CTAs and links are correct
- section hierarchy is clear
- desktop, tablet, and mobile layouts are handled
- any new CSS is in a separate CSS file
- any new JavaScript is in a separate JavaScript file
- the final page looks native to the existing website

### Source conflicts and verification limits

Do not silently omit content because it does not fit the wireframe. Resolve the section mapping while preserving the approved content, structure, and visual responsibilities above. An unresolved conflict that changes scope is a blocker. A Balsamiq export or screenshot is usable evidence but is not proof that a native Balsamiq project was opened or edited. Distinguish browser checks actually run from source-only inspection. Do not claim existing backend integration where only demonstration interactions were built.
````
<!-- prompt:end -->

## Usage notes

The approved Markdown controls content; the wireframe controls structure; reference HTML controls visual style. The unavailable legacy related ID was removed.

**Relevant capabilities:** `file-access`, `browser-when-available`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [SEO Markdown to Balsamiq Wireframe](../wireframes/seo-markdown-to-balsamiq-wireframe.md) — You have SEO research or page content in Markdown and want a Balsamiq-style wireframe before design or implementation.
- [Build an HTML Page From Scope and Design Rules](build-html-page-from-scope-and-design-system.md) — Build one standalone HTML page using separate content requirements and visual design rules.
- [Visual Verification](../redesign/visual-verification.md) — Use after UI changes when the agent should compare the result visually and fix issues.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
