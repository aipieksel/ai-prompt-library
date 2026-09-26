---
id: "fix-html-from-assessment"
title: "Fix HTML From an Approved Assessment"
type: "prompt"
primary_category: "design"
categories: ["design"]
subcategory: "quality"
when_to_use: "Apply only the approved issues from an HTML assessment; preserve all unrelated content, design, and behavior"
search_terms: ["fix-html-from-assessment", "design", "quality"]
inputs: ["HTML_FILE", "APPROVED_ASSESSMENT"]
output: "Only the complete updated HTML on success; a precise blocker report when required evidence is missing."
mode: "edit"
capabilities: ["file-access", "browser-when-available"]
related: ["assess-html-publish-readiness", "minimal-scope-change", "safe-file-editing"]
aliases: ["fix-this-page.md", "fix-this-page"]
---

# Fix HTML From an Approved Assessment

Apply only the approved issues from an HTML assessment; preserve all unrelated content, design, and behavior.

**Type:** prompt · **Mode:** edit · **ID:** `fix-html-from-assessment`

**Expected output:** Only the complete updated HTML on success; a precise blocker report when required evidence is missing.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{HTML_FILE}}` | The full original HTML to update. | linux-vps.html |
| `{{APPROVED_ASSESSMENT}}` | The assessment file and approved issue IDs, including any excluded findings. | assessed-linux-vps.md; apply HTML-001 through HTML-004 only. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Target HTML:
{{HTML_FILE}}

Approved assessment and authorized issue IDs:
{{APPROVED_ASSESSMENT}}

Apply the approved assessment to the target HTML. Read both sources completely before changing anything. The assessment controls which issues to fix; the original HTML controls everything outside those changes.

### Scope

Fix every approved, actionable issue, using the smallest complete change. Do not perform a new redesign, broad rewrite, unrelated cleanup, or speculative enhancement. Do not treat pre-launch URL checks as HTML defects. Do not apply unresolved research-dependent changes as verified facts.

Preserve all unrelated copy, sections, ordering, headings, metadata, structured data, links, navigation, footer, classes, IDs, data attributes, tracking hooks, forms, scripts, functionality, responsive behavior, and existing design-system rules. Preserve all content unless an approved issue explicitly calls for changing or removing it.

Reuse existing tokens and components. Do not introduce new frameworks, libraries, dependencies, products, features, prices, locations, claims, reviews, statistics, guarantees, or proof. Keep any authorized copy changes specific, accurate, concise, and consistent with the existing voice. Keep structured data and visible content aligned when either is changed.

### Implement and check

1. Map every authorized issue ID to the exact affected HTML and the assessment's acceptance condition.
2. Apply the fixes without overwriting unrelated user changes.
3. Verify each authorized issue against the updated source and check that unrelated content and hooks remain intact.
4. Check HTML completeness, corrected links and attributes, heading structure, metadata/schema consistency, and relevant interactions. Inspect desktop, tablet, and mobile behavior with browser tools when available.
5. Resolve defects introduced by the changes. Do not claim runtime or visual verification from source inspection alone.

### Output contract

On success, return only the complete updated HTML file, from <!doctype html> through </html>. Do not return fragments, a diff, “rest unchanged,” an assessment, a summary, or notes after the HTML. Do not insert public-facing placeholder notes to conceal an unresolved issue.

If missing files, contradictory approved instructions, or unavailable factual evidence prevent a required fix, return a concise blocker report identifying the affected issue IDs instead of claiming a completed file. Ask only for the information needed to resolve that blocker. Non-blocking tool limitations do not authorize fake verification claims.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `browser-when-available`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Assess HTML Publish Readiness](assess-html-publish-readiness.md) — Assess an HTML page for SEO, conversion, credibility, factual safety, and publish readiness without editing it.
- [Minimal Scope Change](../../../modifiers/minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.
- [Safe File Editing](../../../modifiers/safe-file-editing.md) — Use when the agent edits project files and must not break or overwrite unrelated content.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
