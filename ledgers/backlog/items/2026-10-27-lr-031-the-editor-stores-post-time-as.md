---
id: 2026-10-27-lr-031-the-editor-stores-post-time-as
title: The editor stores post time as UTC while the calendar and drag-reschedule treat the same string as local time, and no timezone is shown.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j085-schedule-in-the-past
- 2026-10-27-j086-timezone-semantics-of-a-scheduled-time
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
related: []
docs:
- frontend/src/features/review/context/useReviewFlowActions.ts
- frontend/src/features/content-schedule-calendar/adapters/sheetRowAdapter.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/schedule
raw_id: LR-031
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The editor stores post time as UTC while the calendar and drag-reschedule treat the same string as local time, and no timezone is shown.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082, J-085..J-087
- **Aliases:** FEA-002, C05-4
- **Evidence:** frontend/src/features/review/context/useReviewFlowActions.ts:632-641; frontend/src/features/content-schedule-calendar/adapters/sheetRowAdapter.ts:9-23
- **Repro:** (static reasoning) Set browser TZ to Asia/Kolkata, schedule 09:00 in the editor; observe the sheet value `03:30`; open calendar: event at 03:30. Drag to 10:00: sheet value `10:00`, editor then shows 15:30.
- **Fix hint:** Use one shared UTC/local conversion helper in the calendar adapter, reschedule commit and past-time check; add a timezone caption to ScheduleEditor.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use one shared UTC/local conversion helper in the calendar adapter, reschedule commit and past-time check; add a timezone caption to ScheduleEditor.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-031). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowActions.ts:632-641.
