---
id: 2026-10-27-jrn-002-the-scheduled-publish-alarm-never-checks
title: The scheduled-publish alarm never checks the user's status, so a suspended user's already-queued posts still publish
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j128-admin-suspends-a-user-while-they
related:
- 2026-10-27-lr-013-the-scheduled-publish-durable-object-drops
- 2026-10-27-lr-014-every-early-exit-in-executescheduledpublish-counts
- 2026-10-27-lr-188-small-access-admin-defects-sql-text
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
raw_id: JRN-002
source_file: docs/launch-readiness/findings/JOURNEY-DELTA.md
---

## Problem

The scheduled-publish alarm never checks the user's status, so a suspended user's already-queued posts still publish.

## Evidence and reproduction

- **Journeys:** J-128
- **Covers:** none (LR-013 and LR-014 are about the dropped userId and silent skips; LR-188 is about admin suspend edge cases)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:4750-4800 (executeScheduledPublish has no checkUserAccess / status read); worker/src/scheduled-publish/ScheduledPublishAlarm.ts:85-100; status is only checked in worker/src/index.ts:3071 on the request path
- **Repro:** User U arms a post for 2 minutes ahead; admin clicks Suspend on U; wait for the alarm. Pass: no post goes out and the row records why. Today the alarm calls publishContent without any access check.
- **Fix hint:** Persist userId in the DO task (LR-013), then in executeScheduledPublish call checkUserAccess for that user and skip with a logged reason when suspended or removed; cancel the user's alarms when an admin suspends.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist userId in the DO task (LR-013), then in executeScheduledPublish call checkUserAccess for that user and skip with a logged reason when suspended or removed; cancel the user's alarms when an admin suspends.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/JOURNEY-DELTA.md (JRN-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: worker/src/index.ts:4750-4800.
