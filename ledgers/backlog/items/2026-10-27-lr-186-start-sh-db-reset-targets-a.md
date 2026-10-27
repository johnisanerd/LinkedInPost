---
id: 2026-10-27-lr-186-start-sh-db-reset-targets-a
title: start.sh db reset targets a D1 and tables that do not exist, uses grep -oP (not on macOS) and hides errors
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j011-local-development-loop
- 2026-10-27-j014-start-sh-unified-launcher
related: []
docs:
- start.sh
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: setup/cli
raw_id: LR-186
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

start.sh db reset targets a D1 and tables that do not exist, uses grep -oP (not on macOS) and hides errors.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-011, J-014
- **Aliases:** ARCH-020
- **Evidence:** start.sh:90-118
- **Repro:** (static check) Open start.sh:90-118 and confirm the behaviour described in the summary; then exercise the matching journey (J-011, J-014) to observe it.
- **Fix hint:** Remove or retarget.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remove or retarget.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-186). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of start.sh:90-118.
