---
id: 2026-10-27-lr-185-pattern-outcome-recording-is-awaited-without
title: Pattern outcome recording is awaited without catch and pattern stats are global across tenants
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j059-pick-a-writing-pattern-template-for
related: []
docs:
- generation-worker/src/players/patternFinder.ts
- generation-worker/src/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: generation-worker
raw_id: LR-185
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Pattern outcome recording is awaited without catch and pattern stats are global across tenants.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-059
- **Aliases:** GWP-021
- **Evidence:** generation-worker/src/players/patternFinder.ts:23-36,93; generation-worker/src/pipeline.ts:186
- **Repro:** static.
- **Fix hint:** Wrap in try/catch and scope stats by spreadsheet if desired.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wrap in try/catch and scope stats by spreadsheet if desired.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-185). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/players/patternFinder.ts:23-36,93.
