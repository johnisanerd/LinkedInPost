---
id: 2026-10-27-lr-182-the-bootstrap-failure-screen-has-no
title: The bootstrap failure screen has no Retry and a timeout leaves a stale token
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j023-backend-unreachable-at-boot
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
area: frontend/shell
raw_id: LR-182
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The bootstrap failure screen has no Retry and a timeout leaves a stale token.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-023
- **Aliases:** FEB-024
- **Evidence:** frontend/src/App.tsx:301-367,683-689
- **Repro:** static reasoning.
- **Fix hint:** Retry button that re-runs the bootstrap effect; structured error codes.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Retry button that re-runs the bootstrap effect; structured error codes.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-182). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/App.tsx:301-367,683-689.
