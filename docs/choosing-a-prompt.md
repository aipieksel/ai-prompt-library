# Choosing the right prompt

[Home](../README.md) · [Catalog](../CATALOG.md)

Choose by **what may change** and **what you want returned**. Similar vocabulary does not make two prompts interchangeable.

## Style transfer is not structural redesign

| Intended operation | Prompt | Boundary |
| --- | --- | --- |
| Restyle a target without changing its layout | [Apply Reference Style](../prompts/design/style-transfer/apply-reference-style.md) | The reference controls appearance; the target keeps its structure, copy, and behavior. |
| Produce a new HTML file from a visual reference | [Reference Style Transfer to Target HTML](../prompts/design/style-transfer/reference-style-transfer-to-target-html.md) | HTML-specific transfer with a new output file rather than an implicit overwrite. |
| Apply a written design-system contract | [Reference Design System Style Transfer to Target HTML](../prompts/design/style-transfer/reference-design-system-style-transfer-to-target-html.md) | The approved Markdown rules outrank supporting visual examples. |
| Restyle and derive a missing compatible component | [Style Transfer Extension](../prompts/design/style-transfer/style-transfer-extension.md) | Keep target content and structure; label genuinely derived extensions. |
| Add sections after an approved hero or page | [Style Extension From Reference](../prompts/design/style-transfer/style-extension-from-reference.md) | Extend the visual language without repeating the hero composition everywhere. |
| Polish strictly inside existing design rules | [Strict Design System Compliance](../prompts/design/style-transfer/strict-design-system-compliance.md) | No new token values or patterns; use the full compliance audit for an exhaustive matrix. |
| Replace structure within a reference identity | [Style-Guided Redesign](../prompts/design/style-transfer/style-guided-redesign.md) | Layout changes are authorized; deletion or rewriting of required content is not. |
| Redesign presentation with a truly locked DOM | [CSS Architecture Redesign Without Markup Change](../prompts/design/style-transfer/css-architecture-redesign-without-markup-change.md) | CSS changes only. Report a structural blocker rather than silently editing markup. |
| Correct a superficial theme-only redesign | [Full Presentation Redesign for Locked HTML](../prompts/design/style-transfer/full-presentation-redesign-for-locked-html.md) | Selector-level corrective pass; supports a scoped CSS delta when requested. |
| Import another interface into the target system | [HTML Content and Layout Import Into Existing Design System](../prompts/design/style-transfer/html-content-and-layout-import-into-existing-design-system.md) | Source contributes the experience; target retains its style and implementation patterns. |
| Replace layout and visual composition | [Fundamental Visual Redesign](../prompts/design/redesign/fundamental-visual-redesign.md) | Use when a real redesign—not a restyle—is approved. |
| Change visual identity specifically | [Visual Identity Redesign](../prompts/design/redesign/visual-identity-redesign.md) | A new palette and visual direction, subject to the stated brand constraints. |

Keep content fidelity separate from visual similarity. A style transfer should carry spacing, density, typography, component treatment, and states—not only colors—but it must still obey its markup and layout boundaries.

## Choose the correct building stage

| Stage and available inputs | Prompt family | What comes next |
| --- | --- | --- |
| An idea or an unclear interface structure | [Wireframes](../prompts/design/wireframes/README.md) | Approve structure before implementation. |
| Content Markdown + approved wireframe + reference HTML | [Three-source page build](../prompts/design/page-builds/implement-page-from-markdown-wireframe-and-reference-html.md) | Review content coverage, layout fidelity, and visual consistency. |
| Page scope + design rules, with no separate approved wireframe | [Build from scope and design rules](../prompts/design/page-builds/build-html-page-from-scope-and-design-system.md) | Assess the completed page. |
| Existing HTML + design system + feature specification | [Implement a spec into existing HTML](../prompts/design/page-builds/implement-spec-into-existing-html-with-design-system.md) | Verify the changed flow and preserve unrelated behavior. |
| Approved mockup/HTML needing a documented handoff | [Implementation handoff](../prompts/design/handoff/implementation-handoff-docs-from-mockup-or-html.md) | Give all three output documents to the implementation agent. |

A wireframe prompt is not a request for production HTML. A planning prompt does not authorize writing code. A static wireframe or screenshot is not evidence that a native Balsamiq file was opened or created.

## Choose the right extraction or showcase

**Standard image extraction** produces a detailed inventory of visible copy, structure, components, and design rules. **Extended extraction** additionally requires a reusable implementation contract and token schema. Both must label inferred values and unreadable text rather than inventing precision.

**Consolidate sources into a showcase** reconstructs an existing system and should look like that system. **Research a palette/showcase** proposes a system from a brief. **Campaign research** defines the campaign system without producing the final landing page. **Six-palette VPS comparison** uses a deliberately neutral document shell so the palettes—not decorative UI—can be compared. **VPS showcase extension** preserves an existing console and adds the detailed website layer; it is the specialized 52-section package, not a general starting point.

Find these in [Extraction](../prompts/design/extraction/README.md) and [Showcases](../prompts/design/showcases/README.md).

## Choose audit, correction, or verification

[Content Audit](../prompts/content/editing/content-audit.md) examines copy and returns feedback, without rewriting the source. [Content Update](../prompts/content/editing/content-update.md) applies approved, correctly matched feedback and produces updated copy plus a summary.

[Assess HTML Publish Readiness](../prompts/design/quality/assess-html-publish-readiness.md) reviews actual HTML across seven categories. It separates malformed or incorrect URLs from correct future URLs that are not deployed yet. [Fix HTML From an Approved Assessment](../prompts/design/quality/fix-html-from-assessment.md) applies only authorized findings.

[Design-System Compliance](../prompts/design/quality/design-system-compliance-audit-and-fix.md) is an audit-and-edit workflow with atomic requirements and evidence-backed scores. [Visual Verification](../prompts/design/redesign/visual-verification.md) focuses on rendered defects and the actual UI result.

Do not run an edit prompt merely because you wanted a diagnosis. Do not turn unverified findings into mandatory edits without checking or approval.

## Component exploration versus implementation

The component recommendation prompts return **eight directions**. Select one before using a redesign/build prompt. The “without existing focal component” variant is for a page that does not already have the thing being replaced; it must not pretend a missing component exists. The “with direction” variant follows an already selected direction. The infrastructure-metaphor prompt changes how the same technical idea is communicated.

All are in [Components](../prompts/design/components/README.md). Preserve real HTML/CSS output where requested; a static mockup is not an equivalent implementation.

## Technical and business planning

Use [Codebase-First Implementation](../prompts/coding/codebase-alignment/codebase-first-implementation.md) for a concrete change, [Smart Agent Logic](../prompts/coding/code-quality/smart-agent-logic.md) for explicit rules and test cases, and [Research Before Deciding](../prompts/coding/agent-quality/research-before-deciding.md) when choosing among options.

[Plan a Business Integration](../prompts/business/integration-planning/integration-design-outline.md) produces a business-facing integration design and phased implementation outline. It is not a financial model, investor pitch, or comprehensive business plan, despite its older filename.
