---
id: 2026-10-27-lr-032-the-pending-scheduled-publish-state-lives
title: The pending scheduled-publish state lives only in React memory, so after reload the banner and Cancel vanish and a post can queue twice.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j084-cancel-a-scheduled-post
- 2026-10-27-j088-double-click-on-publish
related: []
docs:
- frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts
- frontend/src/features/scheduled-publish/matchPending.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/schedule
raw_id: LR-032
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The pending scheduled-publish state lives only in React memory, so after reload the banner and Cancel vanish and a post can queue twice.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082, J-084, J-088
- **Aliases:** FEA-003
- **Evidence:** frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts:15,17-28; frontend/src/features/scheduled-publish/matchPending.ts
- **Repro:** (static reasoning) Schedule post A, schedule post B (A's banner is gone), or schedule A then reload: no banner, "Publish" is enabled again and re-queues A.
- **Fix hint:** Return queued tasks from bootstrap or getRows (keyed by topicId+channel) and derive the banner from server state.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return queued tasks from bootstrap or getRows (keyed by topicId+channel) and derive the banner from server state.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-032). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/scheduled-publish/usePendingScheduledPublish.ts:15,17-28.
