---
id: "preserve-existing-system"
title: "Preserve Existing System"
type: "modifier"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when the agent must fix or improve something without changing the surrounding system"
search_terms: ["preserve-existing-system", "coding", "agent-quality", "minimal-change", "no-refactor", "preserve", "preserve-system", "safe-edits", "system"]
inputs: []
output: "A scoped change that preserves unrelated structure, behavior, and visual identity."
mode: "modify"
capabilities: []
related: ["minimal-scope-change", "safe-file-editing"]
aliases: ["coding/agent-quality/preserve-existing-system.md", "preserve-existing-system.md"]
---

# Preserve Existing System

Use when the agent must fix or improve something without changing the surrounding system.

**Type:** modifier · **Mode:** modify · **ID:** `preserve-existing-system`

**Expected output:** A scoped change that preserves unrelated structure, behavior, and visual identity.

**Not for:** Fundamental redesign or migration tasks that explicitly authorize replacing the existing structure.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Preserve the existing system while carrying out the requested change.

Do not redesign, restructure, rename, replace, simplify, or refactor anything unless the requested change directly requires it. Keep existing logic, styling, naming conventions, file structure, component behavior, links, hooks, IDs, data attributes, and surrounding functionality intact.

Reuse established patterns. Introduce a new pattern only when no suitable existing one can satisfy the requirement. Before changing a shared contract, inspect and update every affected reference within the authorized scope.

Make the smallest complete change, then compare the diff and exercise the affected flow. Leave unrelated content and user changes untouched. Flag any necessary broader change before treating it as authorized.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Minimal Scope Change](minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.
- [Safe File Editing](safe-file-editing.md) — Use when the agent edits project files and must not break or overwrite unrelated content.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
