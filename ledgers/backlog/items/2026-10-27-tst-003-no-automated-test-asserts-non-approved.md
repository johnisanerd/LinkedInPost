---
id: 2026-10-27-tst-003-no-automated-test-asserts-non-approved
title: 'No automated test asserts: Non-approved Google account signs in'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j017-non-approved-google-account-signs-in
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Sign-in and session
raw_id: TST-003
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Non-approved Google account signs in.

## Evidence and reproduction

- **Journeys:** J-017
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Access not granted|Request access at the homepage'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: Step 3 returns `{"ok":false,"error":"Access not granted. Request access at the homepage."}` and no `users` row with `status='active'` is created. (Currently expected to FAIL: bootstrap returns a session.)
- **Fix hint:** add a test that asserts: bootstrap with a Google email that is not approved returns 'Access not granted' and writes no active users row. Test file suggestion: worker/src/index.bootstrap.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: bootstrap with a Google email that is not approved returns 'Access not granted' and writes no active users row. Test file suggestion: worker/src/index.bootstrap.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
