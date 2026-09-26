---
id: "codebase-first-implementation"
title: "Codebase-First Implementation"
type: "prompt"
primary_category: "coding"
categories: ["coding"]
subcategory: "codebase-alignment"
when_to_use: "Use as a single strong prompt before coding tasks"
search_terms: ["codebase-first-implementation", "coding", "codebase-alignment", "architecture", "codebase", "codebase-first", "existing-patterns", "first", "implementation"]
inputs: ["TASK", "PROJECT_CONTEXT"]
output: "The implementation, changed file paths, and verification results."
mode: "edit"
capabilities: ["file-access", "code-execution"]
related: ["smart-agent-logic", "safe-file-editing", "verify-before-returning"]
aliases: ["coding/codebase-alignment/codebase-first-implementation.md", "codebase-first-implementation.md"]
---

# Codebase-First Implementation

Use as a single strong prompt before coding tasks.

**Type:** prompt · **Mode:** edit · **ID:** `codebase-first-implementation`

**Expected output:** The implementation, changed file paths, and verification results.

## Inputs

Replace every listed placeholder. For an optional source, enter `None` when it is unavailable.

| Placeholder | What to provide | Example |
| --- | --- | --- |
| `{{TASK}}` | The concrete feature, fix, or implementation request. | Fix duplicate submissions without changing the form layout. |
| `{{PROJECT_CONTEXT}}` | Repository files, entry points, stack, and constraints available to the agent. | src/forms/submit.ts, the form component, and relevant tests. |

## Prompt

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Task:
{{TASK}}

Project files and constraints:
{{PROJECT_CONTEXT}}

Implement the task in the existing codebase.

1. Inspect the relevant files before coding. Trace the current architecture, data flow, dependencies, interfaces, error handling, and affected user journey.
2. Identify reusable helpers, utilities, components, services, hooks, APIs, state patterns, naming conventions, and tests. Prefer these over introducing a new pattern.
3. Implement the smallest robust solution that fully satisfies the request. Handle relevant invalid inputs, missing data, failure paths, and edge cases without broad refactoring.
4. Review the diff for correctness, regressions, duplication, security issues, accessibility where relevant, unnecessary complexity, and consistency with the existing architecture.
5. Run the relevant available tests or checks and fix failures introduced by the change. State any checks that could not run.

Return the final implementation with exact changed or created paths and concise verification evidence. Do not substitute generic advice for available implementation work.
````
<!-- prompt:end -->

## Usage notes

Supply the actual referenced material. A filename or URL does not grant the assistant file, browser, account, or edit access.

**Relevant capabilities:** `file-access`, `code-execution`. These are requirements or conditional needs, not tools installed by this file.

## Related entries

- [Smart Agent Logic](../code-quality/smart-agent-logic.md) — Use when the agent must build rules, scoring, matching, defaults, or automated behavior.
- [Safe File Editing](../../../modifiers/safe-file-editing.md) — Use when the agent edits project files and must not break or overwrite unrelated content.
- [Verify Before Returning](../../../modifiers/verify-before-returning.md) — Use when the agent should check its own work before returning it.

[Browse the catalog](../../../CATALOG.md) · [Usage guide](../../../docs/usage.md)
