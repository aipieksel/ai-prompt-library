---
id: "safe-file-editing"
title: "Safe File Editing"
type: "modifier"
primary_category: "coding"
categories: ["coding"]
subcategory: "file-safety"
when_to_use: "Use when the agent edits project files and must not break or overwrite unrelated content"
search_terms: ["safe-file-editing", "coding", "file-safety", "editing", "file", "file-editing", "formatting", "no-overwrite", "patch", "safe"]
inputs: []
output: "Safely applied changes limited to the requested files and sections."
mode: "modify"
capabilities: []
related: ["minimal-scope-change", "preserve-existing-system"]
aliases: ["coding/file-safety/safe-file-editing.md", "safe-file-editing.md"]
---

# Safe File Editing

Use when the agent edits project files and must not break or overwrite unrelated content.

**Type:** modifier · **Mode:** modify · **ID:** `safe-file-editing`

**Expected output:** Safely applied changes limited to the requested files and sections.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Edit only the files and sections required for the main task.

Read each target before editing. Preserve encoding, line endings, formatting conventions, unrelated code, comments, and existing user changes. Prefer an anchored patch or a checked scripted write over fragile shell echo chains or unverified text replacement.

Confirm that the intended match is unique before replacing it. Do not silently overwrite an unrelated file, follow an unexpected symlink, or truncate content. Use a temporary file and replacement step when that is safer for a generated artifact.

After editing, reopen the affected content, inspect the diff, and run relevant validation. If a patch does not match the current source, re-inspect instead of forcing it. Do not perform unrelated cleanup.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Minimal Scope Change](minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.
- [Preserve Existing System](preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
