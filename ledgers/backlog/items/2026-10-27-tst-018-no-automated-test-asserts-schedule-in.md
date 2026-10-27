---
id: 2026-10-27-tst-018-no-automated-test-asserts-schedule-in
title: 'No automated test asserts: Schedule in the past'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j085-schedule-in-the-past
related: []
docs:
- frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts
- tests-e2e/e2e/journeys/11-scheduled-publish.spec.ts
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
raw_id: TST-018
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Schedule in the past.

## Evidence and reproduction

- **Journeys:** J-085
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'scheduledAt|past slot|Schedule in the past'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 3 file(s): frontend/tests/e2e/journeys/11-scheduled-publish.spec.ts, tests-e2e/e2e/journeys/11-scheduled-publish.spec.ts, tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** UI blocks or warns on a past slot. API: because the arm branch requires `scheduledAt > Date.now() + 60000`, a past or near-now `postTime` is NOT queued: the call publishes immediately and returns `deliveryMode:"sent"`. The user who typed a past time must be told this will publish now before they confirm.
- **Fix hint:** add a test that asserts: a postTime in the past (or within 60s) publishes now and the UI warns before confirming. Test file suggestion: worker/src/scheduling.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a postTime in the past (or within 60s) publishes now and the UI warns before confirming. Test file suggestion: worker/src/scheduling.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-018). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
