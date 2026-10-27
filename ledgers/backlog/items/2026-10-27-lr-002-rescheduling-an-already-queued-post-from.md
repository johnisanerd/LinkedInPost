---
id: 2026-10-27-lr-002-rescheduling-an-already-queued-post-from
title: Rescheduling an already queued post from the calendar or in bulk changes postTime without re-queuing, so the post never goes out.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j083-alarm-fires-what-the-scheduled-run
- 2026-10-27-j084-cancel-a-scheduled-post
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: frontend/schedule
raw_id: LR-002
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Rescheduling an already queued post from the calendar or in bulk changes postTime without re-queuing, so the post never goes out.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082..J-084, J-087
- **Aliases:** FEA-001, WKA-003 (reschedule path)
- **Evidence:** frontend/src/components/dashboard/index.tsx:521-580; worker/src/index.ts:4777
- **Repro:** (static reasoning) Schedule a LinkedIn post for T+10 min from the editor (deliveryMode `queued`). Open the calendar, drag the same post to T+20 min and confirm. Wait past both times: nothing publishes, row stays Approved.
- **Fix hint:** On any schedule change for an Approved row cancel the old queued task and call publishContent again (or re-arm in the worker updatePostSchedule); at minimum block drag-reschedule for queued rows.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

On any schedule change for an Approved row cancel the old queued task and call publishContent again (or re-arm in the worker updatePostSchedule); at minimum block drag-reschedule for queued rows.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/index.tsx:521-580.
