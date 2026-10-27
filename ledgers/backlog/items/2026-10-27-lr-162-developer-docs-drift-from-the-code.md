---
id: 2026-10-27-lr-162-developer-docs-drift-from-the-code
title: Developer docs drift from the code (React version, ports, Anthropic and Firebase claims, researcher providers, migration counts, wizard ports).
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j011-local-development-loop
- 2026-10-27-j013-documented-developer-test-commands-exist
related: []
docs:
- AGENTS.md
- worker/AGENTS.md
- packages/AGENTS.md
- packages/llm-core/src/static-models.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: docs
raw_id: LR-162
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Developer docs drift from the code (React version, ports, Anthropic and Firebase claims, researcher providers, migration counts, wizard ports).

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-011, J-013
- **Aliases:** ARCH-017, SET-033, GWP-025
- **Evidence:** AGENTS.md; worker/AGENTS.md; packages/AGENTS.md; packages/llm-core/src/static-models.ts:3-27
- **Repro:** static.
- **Fix hint:** One docs pass after the P0/P1 fixes; update ARCHITECTURE.md as the spec and add openrouter: [] to the static catalog.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

One docs pass after the P0/P1 fixes; update ARCHITECTURE.md as the spec and add openrouter: [] to the static catalog.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-162). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of AGENTS.md.
