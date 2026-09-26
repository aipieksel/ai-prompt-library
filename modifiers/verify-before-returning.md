---
id: "verify-before-returning"
title: "Verify Before Returning"
type: "modifier"
primary_category: "coding"
categories: ["coding", "design"]
subcategory: "agent-quality"
when_to_use: "Use when the agent should check its own work before returning it"
search_terms: ["verify-before-returning", "coding", "agent-quality", "evidence", "returning", "self-review", "testing", "validation", "verification", "verify"]
inputs: []
output: "The main deliverable and a truthful checked/unverified status in its permitted report format."
mode: "modify"
capabilities: []
related: ["visual-verification", "rigorous-agent-execution"]
aliases: ["coding/agent-quality/verify-before-returning.md", "verify-before-returning.md"]
---

# Verify Before Returning

Use when the agent should check its own work before returning it.

**Type:** modifier · **Mode:** modify · **ID:** `verify-before-returning`

**Expected output:** The main deliverable and a truthful checked/unverified status in its permitted report format.

## Inputs

No placeholders. Use this with a concrete main task.

## Modifier

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Before returning the main task's result:

1. Inspect the affected files and establish expected behavior from the brief, tests, or observed baseline.
2. Review the actual change, including dependencies and the paths most likely to regress.
3. Run available checks appropriate to the change: parsing, build, targeted tests, or the affected user flow. For visual changes, inspect rendered output when browser or screenshot tools are available.
4. Fix failures introduced by the change and rerun the relevant checks.
5. Distinguish checks that passed, checks that failed, and checks that could not run. Include the command or evidence when reporting verification.

Do not treat code inspection as proof of runtime or visual correctness. Do not report a test as passed merely because the implementation looks plausible.
````
<!-- prompt:end -->

## Usage notes

This is a modifier: append it to a concrete prompt only when their scopes and output contracts agree.

## Related entries

- [Visual Verification](../prompts/design/redesign/visual-verification.md) — Use after UI changes when the agent should compare the result visually and fix issues.
- [Rigorous Agent Execution](rigorous-agent-execution.md) — Use when you want the agent to slow down, inspect carefully, avoid assumptions, and return accurate implementation-ready work.

[Browse the catalog](../CATALOG.md) · [Usage guide](../docs/usage.md)
