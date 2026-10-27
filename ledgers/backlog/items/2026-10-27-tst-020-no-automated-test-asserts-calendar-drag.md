---
id: 2026-10-27-tst-020-no-automated-test-asserts-calendar-drag
title: 'No automated test asserts: Calendar drag-reschedule of an already queued post'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
related: []
docs:
- frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts
- frontend/tests/e2e/journeys/13-enrichment-pipeline.spec.ts
- tests-e2e/e2e/journeys/11-scheduled-publish.spec.ts
- tests-e2e/e2e/journeys/13-enrichment-pipeline.spec.ts
- tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Scheduling and publishing
raw_id: TST-020
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Calendar drag-reschedule of an already queued post.

## Evidence and reproduction

- **Journeys:** J-087
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'updatePostSchedule|reschedul|drag'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 7 file(s): frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts, frontend/tests/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/11-scheduled-publish.spec.ts, tests-e2e/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: post fires at the new time only. CODE-READING FINDING: `updatePostSchedule` only updates the row's `postTime`; nothing re-arms a Durable Object (`armScheduledPublish` is called only from `publishContent`). At the old time the DO runs `executeScheduledPublish`, sees `row.postTime != task.scheduledTime` and silently returns; no DO exists for the new time, so the post never fires. Errors in the drag handler...
- **Fix hint:** add a test that asserts: updatePostSchedule re-arms the Durable Object so the post fires only at the new time. Test file suggestion: worker/src/scheduling.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: updatePostSchedule re-arms the Durable Object so the post fires only at the new time. Test file suggestion: worker/src/scheduling.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-020). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
