---
id: 2026-10-27-lr-013-the-scheduled-publish-durable-object-drops
title: The scheduled-publish Durable Object drops userId, so the alarm reads the wrong tenant sheet and posts through the shared account.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j083-alarm-fires-what-the-scheduled-run
- 2026-10-27-j092-durable-object-alarm-throws-and-is
- 2026-10-27-j103-a-user-with-no-linkedin-connection
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
docs:
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/schedule
raw_id: LR-013
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The scheduled-publish Durable Object drops userId, so the alarm reads the wrong tenant sheet and posts through the shared account.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082, J-083, J-092, J-103, J-140
- **Aliases:** WKA-002, WKB-001
- **Evidence:** worker/src/scheduled-publish/ScheduledPublishAlarm.ts:36-44; worker/src/index.ts:4751,4754
- **Repro:** static. Executor: as a non-admin user with own sheet, approve a post, schedule 2 minutes ahead, wait; check LinkedIn, D1 `pipeline_state.status` and worker logs.
- **Fix hint:** Persist userId in the DO task and call loadStoredConfig(env, task.userId) and buildServices(env, task.userId) in executeScheduledPublish.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Persist userId in the DO task and call loadStoredConfig(env, task.userId) and buildServices(env, task.userId) in executeScheduledPublish.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-013). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/scheduled-publish/ScheduledPublishAlarm.ts:36-44.
