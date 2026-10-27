---
id: 2026-10-27-cons-055-bulk-select-bulk-delete-reschedule-channel
title: Bulk select + bulk delete/reschedule/channel
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/queue
raw_id: CONS-055
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Bulk select + bulk delete/reschedule/channel.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-16
- **Alias:** C04-16
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:146-149,755-760 (checkbox, bulk channel/schedule dialogs)
- **Covered by:** none

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-055). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (DashboardQueue.tsx:146-149,755-760 (checkbox, bulk channel/schedule dialogs)); no LR item covers it.
