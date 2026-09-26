# Workflow recipes

[Home](../README.md) · [Catalog](../CATALOG.md) · [Choosing guide](choosing-a-prompt.md)

Each recipe is a sequence of separate tasks. Carry the actual output files and approval decisions into the next stage. Do not paste the entire sequence into an agent and assume every step has been approved.

## 1. Audit and improve website copy

**Audit:** give complete source Markdown files to [Content Audit](../prompts/content/editing/content-audit.md). It creates one feedback file per source and leaves the originals unchanged.

**Approve:** review the issue IDs, factual corrections, and scope. Resolve research-dependent changes before authorizing them.

**Apply:** give [Content Update](../prompts/content/editing/content-update.md) isolated source/feedback pairs. It returns full updated copy and a separate summary for each matched pair.

```text
original-linux-vps.md
        ↓ content-audit
feedback-linux-vps.md
        ↓ human review and approval
original-linux-vps.md + approved feedback-linux-vps.md
        ↓ content-update
updated-linux-vps.md + summary-linux-vps.md
```

Do not pair files by topic similarity alone or let feedback for the Windows page change the Linux page. Rename a generic audited source to the expected `original-<base>.md` convention before the update stage, preserving its content and the matching feedback base.

## 2. Deliver an HTML page from approved content

Use [SEO Markdown to Balsamiq Wireframe](../prompts/design/wireframes/seo-markdown-to-balsamiq-wireframe.md) to organize approved content. Review and approve the wireframe before moving to [the three-source implementation prompt](../prompts/design/page-builds/implement-page-from-markdown-wireframe-and-reference-html.md).

Pass the exact content Markdown, approved wireframe, reference HTML, and required styles/assets. Content controls wording, the wireframe controls structure, and the reference controls visual style. The builder returns full HTML and only the necessary separate CSS/JavaScript.

Run [Assess HTML Publish Readiness](../prompts/design/quality/assess-html-publish-readiness.md) on the actual output and specify `live`, `unpublished`, or `unknown`. For `linux-vps.html`, the assessment is `assessed-linux-vps.md`. Approve findings, then use [Fix HTML From an Approved Assessment](../prompts/design/quality/fix-html-from-assessment.md). Perform a final rendered check; do not convert deployment-only 404 checks into copy or HTML defects.

## 3. Extract a design and make it reusable

Give accessible screenshots and supporting source to [Extended Image Extraction](../prompts/design/extraction/image-to-design-system-extraction-extended.md). Review inferred tokens and unknown behaviors before treating the output as a contract.

Pass the approved extraction, original screenshots, and available HTML/CSS into [Consolidate Sources Into a Showcase](../prompts/design/showcases/create-design-system-showcase.md). Preserve all meaningful components and variants; consolidate duplicates without deleting unique content.

Use the resulting contract to guide implementation. Check the actual implementation with [Design-System Compliance](../prompts/design/quality/design-system-compliance-audit-and-fix.md). A screenshot cannot prove hover behavior or hidden states; those checks need additional evidence.

## 4. Explore a component, then build one direction

Use [Component Direction Recommendations](../prompts/design/components/component-direction-recommendations.md) when a focal component exists, or [the no-existing-component variant](../prompts/design/components/component-direction-recommendations-without-existing-focal-component.md) when it does not. Both explore eight alternatives.

Choose one direction and pass it to [Component Concept Redesign With Direction](../prompts/design/components/component-concept-redesign-with-direction.md), together with the source and preservation requirements. Verify the requested HTML/CSS behavior rather than accepting a static image as a substitute.

## 5. Make a safe code change

Give the task, affected source, project conventions, and tests to [Codebase-First Implementation](../prompts/coding/codebase-alignment/codebase-first-implementation.md). Add [Safe File Editing](../modifiers/safe-file-editing.md) or [Minimal Scope Change](../modifiers/minimal-scope-change.md) only where the main prompt needs that emphasis.

For new scoring, matching, or automation, use [Smart Agent Logic](../prompts/coding/code-quality/smart-agent-logic.md) to make inputs, priority rules, edge cases, and expected outputs explicit. Review proposed thresholds rather than treating arbitrary numbers as approved requirements. Run actual tests and record which checks were not available.

## 6. Extend an existing VPS showcase package

Provide the current HTML and four canonical documents to [Extend a Showcase With VPS Website Components](../prompts/design/showcases/extend-vps-design-system-showcase.md). Include older attempts only when they are useful evidence.

The required result is an updated showcase plus seven Markdown documents in one ZIP. Keep the original dashboard system, add the defined VPS layer, preserve all 52 section requirements, and review the specified chart values and ten viewport widths. Sample regions, pricing, support features, and proof structures must remain clearly illustrative until supported by approved facts.

This is a specialized implementation workflow. Use [the neutral palette comparison](../prompts/design/showcases/research-vps-palette-comparison.md) for selecting colors; it has a different purpose and should not look like a marketing showcase.
