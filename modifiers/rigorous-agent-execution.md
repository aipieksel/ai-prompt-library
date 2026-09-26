---
id: "rigorous-agent-execution"
title: "Rigorous Agent Execution"
type: "modifier"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when you want the agent to slow down, inspect carefully, avoid assumptions, and return accurate implementation-ready work"
search_terms: ["rigorous-agent-execution", "coding", "agent-quality", "accuracy", "agent", "execution", "implementation-ready", "rigorous", "verification"]
inputs: []
output: "The main task deliverable, with accurate verification status when the output format allows it."
mode: "modify"
capabilities: []
related: ["codebase-first-implementation", "verify-before-returning"]
aliases: ["coding/agent-quality/rigorous-agent-execution.md", "rigorous-agent-execution.md"]
---

# Rigorous Agent Execution

Use when you want the agent to slow down, inspect carefully, avoid assumptions, and return accurate implementation-ready work.

**Type:** modifier · **Mode:** modify · **ID:** `rigorous-agent-execution`

**Expected output:** The main task deliverable, with accurate verification status when the output format allows it.

**Not for:** A substitute for a task brief or a guarantee that generated work is correct.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Apply these execution requirements to the main task.

1. Inspect the actual source files and relevant project context before deciding or changing anything. Distinguish observations from assumptions.
2. Trace dependencies, likely edge cases, and the affected user flow. Resolve material uncertainty with available evidence rather than guessing.
3. Preserve the required content, functionality, conventions, and authorized scope. Produce the complete requested deliverable, not a shallow outline or speculative alternative.
4. Review the result for correctness, consistency, and implementation readiness. Run the relevant checks that the environment actually supports and fix failures caused by the change.
5. Report what was changed, what was verified, and what remains unverified. Do not claim a tool run, file edit, visual inspection, or successful test that did not happen.

When a missing input blocks a correct result, identify the specific blocker. Do not pretend the task is complete or loop indefinitely in pursuit of certainty.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Codebase-First Implementation](../prompts/coding/codebase-alignment/codebase-first-implementation.md) — Use as a single strong prompt before coding tasks.
- [Verify Before Returning](verify-before-returning.md) — Use when the agent should check its own work before returning it.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
