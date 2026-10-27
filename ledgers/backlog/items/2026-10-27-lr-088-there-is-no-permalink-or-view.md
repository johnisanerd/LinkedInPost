---
id: 2026-10-27-lr-088-there-is-no-permalink-or-view
title: There is no permalink or View-on-channel link after publish, only a generic Success modal, although USE-CASES.md claims a link.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
related: []
docs:
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
- USE-CASES.md
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/editor
raw_id: LR-088
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

There is no permalink or View-on-channel link after publish, only a generic Success modal, although USE-CASES.md claims a link.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076
- **Aliases:** C07-2, U-J1.10
- **Evidence:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts:587
- **Repro:** (static check) Open frontend/src/components/dashboard/hooks/useDashboardQueue.ts:587 and confirm the behaviour described in the summary; then exercise the matching journey (J-076) to observe it.
- **Fix hint:** Show channel and time (and post id if the API returns one) in the success message, or correct the USE-CASES.md claim.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Show channel and time (and post id if the API returns one) in the success message, or correct the USE-CASES.md claim.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-088). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/hooks/useDashboardQueue.ts:587.
