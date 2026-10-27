---
id: 2026-10-27-inv-020-can-a-rethrown-alarm-error-replay
title: Can a rethrown alarm error replay a publish and double-post? (ARCH-010)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-070-publish-has-no-server-side-idempotency
docs:
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: worker/schedule
raw_id: INV-020
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Can a rethrown alarm error replay a publish and double-post? (ARCH-010). Duplicate LinkedIn posts, which cannot be undone.

## Evidence and reproduction

- **Question:** ScheduledPublishAlarm rethrows on error so the runtime retries; executeScheduledPublish has no already-published guard. Does a retry after a successful send post twice?
- **Why it matters:** Duplicate LinkedIn posts, which cannot be undone.
- **How to settle it:** Read worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100 and executeScheduledPublish in worker/src/index.ts:4756-4783 for a status or published-flag check. To settle: on a test Worker, force the post-send mark step to fail and let the alarm retry.
- **Related items:** LR-070
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-020). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: ARCH-AUDIT marks it hypothesis, not confirmed; not run. Covered by LR-070..
