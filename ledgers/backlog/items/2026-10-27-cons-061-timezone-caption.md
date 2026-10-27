---
id: 2026-10-27-cons-061-timezone-caption
title: Timezone caption
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-031-the-editor-stores-post-time-as
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/schedule
raw_id: CONS-061
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Timezone caption.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-4
- **Alias:** C05-4
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** components/schedule/ScheduleEditor.tsx (no tz hit) (editor posts UTC string (useReviewFlowActions.ts:690-697))
- **Covered by:** LR-031

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-061). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (editor posts UTC string (useReviewFlowActions.ts:690-697)); covered by LR-031.
