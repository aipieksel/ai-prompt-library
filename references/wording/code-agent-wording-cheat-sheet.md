---
id: "code-agent-wording-cheat-sheet"
title: "Code Agent Wording Cheat Sheet"
type: "reference"
primary_category: "coding"
categories: ["coding"]
subcategory: "code-quality"
when_to_use: "Use as a categorized reference for instructing agents to write better code"
search_terms: ["code-agent-wording-cheat-sheet", "coding", "code-quality", "agent", "code", "codebase-first", "implementation", "phrases", "quality", "wording"]
inputs: []
output: "Selected wording to add to a concrete task; no standalone deliverable."
mode: "reference"
capabilities: []
related: ["preserve-existing-system", "fundamental-visual-redesign", "minimal-scope-change"]
aliases: ["coding/code-quality/code-agent-wording-cheat-sheet.md", "code-agent-wording-cheat-sheet.md"]
---

# Code Agent Wording Cheat Sheet

Use as a categorized reference for instructing agents to write better code.

**Type:** reference · **Mode:** reference · **ID:** `code-agent-wording-cheat-sheet`

**Expected output:** Selected wording to add to a concrete task; no standalone deliverable.

**Not for:** Running the entire collection as a single prompt.

## Inputs

No placeholders. Select the wording relevant to the authorized task.

## Reference

Copy the block below, not the metadata or usage notes.

<!-- prompt:start -->
````text
Choose the line that describes the authorized change; do not paste this entire menu as one instruction.

## Optimal code
Write the most maintainable implementation for this codebase, not a generic solution. Prefer clear, simple, robust code that fits the existing architecture, avoids duplication, handles edge cases, and can be safely extended later.

## Match existing code
Follow the existing codebase conventions exactly. Reuse current helpers, utilities, components, services, hooks, APIs, naming patterns, file structure, error handling, and styling approach. Do not introduce a new pattern unless the current codebase has no suitable equivalent.

## Review own code
After implementing, review the changed code critically. Check for correctness, edge cases, regressions, duplicated logic, security issues, naming consistency, unnecessary complexity, and whether the solution matches the existing architecture. Fix issues before returning the final answer.

## Inspect before coding
Do not start coding immediately. First inspect the relevant files and trace how the current system works. Identify existing patterns, dependencies, data flow, and edge cases, then implement using that understanding.

## Current best practices
Check current primary documentation for version-sensitive decisions, and use practices appropriate to this codebase. Do not chase novelty. Prefer stable, well-supported, readable, maintainable patterns that match the project’s stack and existing architecture.

## No overengineering
Solve the actual problem with the simplest robust implementation. Avoid unnecessary abstractions, new dependencies, broad rewrites, cleverness, or architecture changes unless clearly required.

## Production-ready code
Include validation, error handling, safe defaults, clear state handling, accessibility where relevant, responsive behavior where relevant, and graceful failure paths. Avoid demo-only logic unless explicitly requested.

## Security-aware code
Validate inputs, sanitize and escape output where relevant, protect sensitive data, preserve nonce/capability checks, avoid unsafe assumptions, and do not expose internal state or credentials.

## Minimal patch
Make the smallest correct change. Do not refactor unrelated code, rename existing APIs, change surrounding behavior, or clean up unrelated files.

## Root-cause debugging
Trace the issue from source to effect. Identify the root cause, affected files, failing path, expected behavior, and safest fix. Do not patch symptoms without understanding why the bug happens.

## WordPress-safe code
For WordPress work, verify the applicable APIs against the project version and preserve: capability checks, nonces, sanitization, escaping, prepared queries, enqueueing, translation functions, and scoped admin hooks.

## Best reusable line
Be rigorous and codebase-first. Inspect the relevant files, understand the existing architecture and patterns, then implement the smallest robust solution that fits the current system. Reuse existing utilities and conventions, handle edge cases and errors, avoid unrelated refactors, and review your own code for regressions, duplication, security issues, and maintainability before returning the final implementation.
````
<!-- prompt:end -->

## Usage notes

Select compatible excerpts. Verification language requires actual evidence, not a guarantee of correctness.

## Related entries

- [Preserve Existing System](../../modifiers/preserve-existing-system.md) — Use when the agent must fix or improve something without changing the surrounding system.
- [Fundamental Visual Redesign](../../prompts/design/redesign/fundamental-visual-redesign.md) — Use when the agent keeps changing colors or spacing but the design still looks the same.
- [Minimal Scope Change](../../modifiers/minimal-scope-change.md) — Use when the agent keeps changing unrelated code, styling, or behavior.

[Browse the catalog](../../CATALOG.md) · [Usage guide](../../docs/usage.md)
