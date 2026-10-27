---
id: 2026-10-27-lr-070-publish-has-no-server-side-idempotency
title: 'Publish has no server-side idempotency: the client row is trusted, status is not checked, and a failed mark step lets a retry post twice.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j088-double-click-on-publish
- 2026-10-27-j089-post-is-live-but-marking-it
- 2026-10-27-j091-republish-an-already-published-post
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
severity: P1
area: worker/schedule
raw_id: LR-070
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Publish has no server-side idempotency: the client row is trusted, status is not checked, and a failed mark step lets a retry post twice.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076, J-088, J-089, J-091, J-092
- **Aliases:** WKA-007, WKB-010, ARCH-010, WKB-011 (replay path)
- **Evidence:** worker/src/index.ts:4824-4869; worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100
- **Repro:** static. Executor: click Publish twice quickly, or make `GOOGLE_SERVICE_ACCOUNT_JSON` invalid after send to force a mark failure and retry.
- **Fix hint:** Load the row server-side, claim it atomically (UPDATE status=Publishing WHERE status=Approved), store the channel post id, make the mark step best-effort after a successful send, and bound alarm retries.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Load the row server-side, claim it atomically (UPDATE status=Publishing WHERE status=Approved), store the channel post id, make the mark step best-effort after a successful send, and bound alarm retries.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-070). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:4824-4869.
