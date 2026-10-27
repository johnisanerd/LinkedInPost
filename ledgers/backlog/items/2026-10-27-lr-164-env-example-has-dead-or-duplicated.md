---
id: 2026-10-27-lr-164-env-example-has-dead-or-duplicated
title: .env.example has dead or duplicated keys, a stale line reference, and inconsistent separators
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j001-web-setup-wizard-end-to-end
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: docs/env
raw_id: LR-164
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

.env.example has dead or duplicated keys, a stale line reference, and inconsistent separators.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-001
- **Aliases:** ARCH-016
- **Evidence:** .env.example:40-50,117
- **Repro:** (static check) Open .env.example:40-50,117 and confirm the behaviour described in the summary; then exercise the matching journey (J-001) to observe it.
- **Fix hint:** Prune dead keys, dedupe and fix the stale reference.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Prune dead keys, dedupe and fix the stale reference.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-164). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of .env.example:40-50,117.
