---
id: 2026-10-27-lr-169-the-footer-button-says-publish-even
title: The footer button says Publish even when it schedules a future time, and the editor uses a bare datetime-local with no past-time warning.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j085-schedule-in-the-past
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
area: frontend/editor
raw_id: LR-169
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The footer button says Publish even when it schedules a future time, and the editor uses a bare datetime-local with no past-time warning.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076, J-082, J-085
- **Aliases:** FEA-030, C05-1, C05-7, C07-3, C07-5
- **Evidence:** frontend/src/features/review-editor/screens/EditorScreen.tsx:310,370-460
- **Repro:** Approve with a future time, reopen the editor, click Publish.
- **Fix hint:** Relabel to Schedule for <time> when in the future, warn when in the past, and use ScheduleEditor in the editor.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Relabel to Schedule for <time> when in the future, warn when in the past, and use ScheduleEditor in the editor.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-169). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review-editor/screens/EditorScreen.tsx:310,370-460.
