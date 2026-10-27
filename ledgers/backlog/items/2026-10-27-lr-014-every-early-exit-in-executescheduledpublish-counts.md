---
id: 2026-10-27-lr-014-every-early-exit-in-executescheduledpublish-counts
title: Every early exit in executeScheduledPublish counts as success and deletes the schedule with no record, so skipped posts vanish silently.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j083-alarm-fires-what-the-scheduled-run
- 2026-10-27-j085-schedule-in-the-past
- 2026-10-27-j086-timezone-semantics-of-a-scheduled-time
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
- 2026-10-27-j092-durable-object-alarm-throws-and-is
related: []
docs:
- worker/src/index.ts
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/schedule
raw_id: LR-014
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Every early exit in executeScheduledPublish counts as success and deletes the schedule with no record, so skipped posts vanish silently.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-083, J-085..J-087, J-092
- **Aliases:** WKA-003, WKB-011
- **Evidence:** worker/src/index.ts:4756-4783; worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100
- **Repro:** static. Executor: schedule a post, then edit its `postTime` with `updatePostSchedule` and wait for the original time.
- **Fix hint:** Log and persist a reason (status Failed plus note) on each skip, cap alarm retries with a terminal failed state, and re-arm in updatePostSchedule.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Log and persist a reason (status Failed plus note) on each skip, cap alarm retries with a terminal failed state, and re-arm in updatePostSchedule.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-014). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:4756-4783.
