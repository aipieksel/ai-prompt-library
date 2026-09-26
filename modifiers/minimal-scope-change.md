---
id: "minimal-scope-change"
title: "Minimal Scope Change"
type: "modifier"
primary_category: "coding"
categories: ["coding"]
subcategory: "implementation-control"
when_to_use: "Use when the agent keeps changing unrelated code, styling, or behavior"
search_terms: ["minimal-scope-change", "coding", "implementation-control", "change", "focused-patch", "minimal", "minimal-change", "no-unrelated-cleanup", "scope", "scope-control"]
inputs: []
output: "The smallest complete fix within the authorized scope."
mode: "modify"
capabilities: []
related: ["preserve-existing-system", "safe-file-editing"]
aliases: ["coding/implementation-control/minimal-scope-change.md", "minimal-scope-change.md"]
---

# Minimal Scope Change

Use when the agent keeps changing unrelated code, styling, or behavior.

**Type:** modifier · **Mode:** modify · **ID:** `minimal-scope-change`

**Expected output:** The smallest complete fix within the authorized scope.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Solve only the requested issue. Avoid unrelated cleanup, refactors, renames, broad rewrites, new dependencies, new abstractions, or changes to surrounding styling and behavior.

A change is in scope only when it implements the request or is necessary to keep the affected path correct. Explain a necessary scope expansion before treating unrelated work as approved.

Review the final diff for accidental edits. Report unrelated issues separately when the output format allows, but do not fix them without authorization.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Preserve Existing System](preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Safe File Editing](safe-file-editing.md) — Use when the agent edits project files and must not break or overwrite unrelated content.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
