---
id: 2026-10-27-tst-017-no-automated-test-asserts-alarm-fires
title: 'No automated test asserts: Alarm fires: what the scheduled run actually executes'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j083-alarm-fires-what-the-scheduled-run
related: []
docs:
- tests-e2e/e2e/journeys/40-wiring-loop26.spec.ts
- tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Scheduling and publishing
raw_id: TST-017
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Alarm fires: what the scheduled run actually executes.

## Evidence and reproduction

- **Journeys:** J-083
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'executeScheduledPublish|armScheduledPublish|alarm'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): tests-e2e/e2e/journeys/40-wiring-loop26.spec.ts, tests-e2e/e2e/journeys/69-wiring-loop50.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** At the scheduled time the post appears on the right account, D1 row `status='Published'`. Currently expected to FAIL for multi-tenant (non-admin or non-KV-sheet) users; for the single-owner self-hosted deployment (admin sheet == KV sheet, global LinkedIn token) it likely works. A row that stays `Approved` after the time with no log line is the symptom.
- **Fix hint:** add a test that asserts: when the Durable Object alarm fires, executeScheduledPublish posts to the right account and sets status Published. Test file suggestion: worker/src/scheduling.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: when the Durable Object alarm fires, executeScheduledPublish posts to the right account and sets status Published. Test file suggestion: worker/src/scheduling.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-017). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
