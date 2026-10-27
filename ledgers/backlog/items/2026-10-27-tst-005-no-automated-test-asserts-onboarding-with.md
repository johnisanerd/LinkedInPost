---
id: 2026-10-27-tst-005-no-automated-test-asserts-onboarding-with
title: 'No automated test asserts: Onboarding with a sheet URL (Drive consent and share)'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j030-onboarding-with-a-sheet-url-drive
related: []
docs:
- frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Onboarding and workspace connection
raw_id: TST-005
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Onboarding with a sheet URL (Drive consent and share).

## Evidence and reproduction

- **Journeys:** J-030
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'connectSpreadsheet|spreadsheet_id|completeOnboarding'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Step 3 returns `{"ok":true,"title":"<sheet title>"}` and D1 `users.spreadsheet_id=<ID>`. Failure cases: CODE-READING FINDING: `handleCompleteOnboarding` catches any error, logs to console only, still calls `completeOnboarding`, and redirects to `/connections`; the user never sees why the sheet was not connected.
- **Fix hint:** add a test that asserts: connect a sheet during onboarding, assert users.spreadsheet_id is set and a failure is shown to the user. Test file suggestion: tests-e2e style: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts plus worker/src/onboarding.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: connect a sheet during onboarding, assert users.spreadsheet_id is set and a failure is shown to the user. Test file suggestion: tests-e2e style: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts plus worker/src/onboarding.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-005). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
