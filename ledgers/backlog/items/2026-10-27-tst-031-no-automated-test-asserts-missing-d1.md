---
id: 2026-10-27-tst-031-no-automated-test-asserts-missing-d1
title: 'No automated test asserts: Missing D1 binding or unapplied migrations'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j133-missing-d1-binding-or-unapplied-migrations
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Failure and recovery
raw_id: TST-031
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Missing D1 binding or unapplied migrations.

## Evidence and reproduction

- **Journeys:** J-133
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Unable to start|no such table|D1_ERROR'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Step 2 returns OK (health check does not touch D1, so setup "verify" can pass while the app is broken). Step 1 returns HTTP 400 with the raw runtime message (e.g. `Cannot read properties of undefined (reading 'prepare')` or `D1_ERROR: no such table: users`) and the frontend shows it as "Unable to start the session"/access error. Desired: a clear "database not initialised: run migrations" message and a health endpo...
- **Fix hint:** add a test that asserts: bootstrap with a missing D1 binding or unmigrated table returns a clear setup message. Test file suggestion: worker/src/bootstrap.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: bootstrap with a missing D1 binding or unmigrated table returns a clear setup message. Test file suggestion: worker/src/bootstrap.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-031). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
