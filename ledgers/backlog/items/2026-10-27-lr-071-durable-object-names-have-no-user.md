---
id: 2026-10-27-lr-071-durable-object-names-have-no-user
title: Durable Object names have no user component, and cancel or arm accepts any topicId and ignores the arm response, so tenants can collide.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j084-cancel-a-scheduled-post
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
- 2026-10-27-j144-scheduler-secret-internal-routes
related: []
docs:
- worker/src/scheduled-publish/durablePublishScheduler.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/schedule
raw_id: LR-071
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Durable Object names have no user component, and cancel or arm accepts any topicId and ignores the arm response, so tenants can collide.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082, J-084, J-087, J-140, J-144
- **Aliases:** WKA-006, WKB-036
- **Evidence:** worker/src/scheduled-publish/durablePublishScheduler.ts:11-13; worker/src/index.ts:2406-2408,4878-4890
- **Repro:** static.
- **Fix hint:** Prefix the DO name with userId, verify row ownership before arm and cancel, and check response.ok on arm.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Prefix the DO name with userId, verify row ownership before arm and cancel, and check response.ok on arm.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-071). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/scheduled-publish/durablePublishScheduler.ts:11-13.
