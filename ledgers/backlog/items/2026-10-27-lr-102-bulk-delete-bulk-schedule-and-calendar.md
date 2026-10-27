---
id: 2026-10-27-lr-102-bulk-delete-bulk-schedule-and-calendar
title: Bulk delete, bulk schedule and calendar reschedule swallow errors, and bulk delete never cancels queued publishes
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j039-delete-a-topic-and-its-generated
- 2026-10-27-j083-alarm-fires-what-the-scheduled-run
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/schedule
raw_id: LR-102
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Bulk delete, bulk schedule and calendar reschedule swallow errors, and bulk delete never cancels queued publishes.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-039, J-083, J-087
- **Aliases:** FEA-011
- **Evidence:** frontend/src/components/dashboard/index.tsx:496-580
- **Repro:** Select several rows, bulk delete with the worker returning errors: no message, rows reappear after reload.
- **Fix hint:** Collect failures into one summary notice and cancel queued tasks before deleting.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Collect failures into one summary notice and cancel queued tasks before deleting.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-102). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/index.tsx:496-580.
