---
id: 2026-10-27-tst-019-no-automated-test-asserts-timezone-semantics
title: 'No automated test asserts: Timezone semantics of a scheduled time'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j086-timezone-semantics-of-a-scheduled-time
related: []
docs:
- frontend/tests/e2e/scheduling.spec.ts
- tests-e2e/e2e/scheduling.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Scheduling and publishing
raw_id: TST-019
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Timezone semantics of a scheduled time.

## Evidence and reproduction

- **Journeys:** J-086
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'timezone|UTC'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): frontend/tests/e2e/scheduling.spec.ts, tests-e2e/e2e/scheduling.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: fires at 09:30 local. CODE-READING FINDING: the string is interpreted as UTC, so a UTC+5:30 user's 09:30 post fires at 15:00 local; a UTC-8 user's fires 8 h early (and a "future" local time may be already "in the past" in UTC, see J-085). The same applies to the DO check `row.postTime === task.scheduledTime`. No timezone is stored with the row.
- **Fix hint:** add a test that asserts: a local 09:30 schedule fires at 09:30 local, not UTC. Test file suggestion: worker/src/scheduling.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a local 09:30 schedule fires at 09:30 local, not UTC. Test file suggestion: worker/src/scheduling.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-019). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
