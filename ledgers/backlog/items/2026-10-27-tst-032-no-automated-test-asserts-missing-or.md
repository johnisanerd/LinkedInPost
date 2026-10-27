---
id: 2026-10-27-tst-032-no-automated-test-asserts-missing-or
title: 'No automated test asserts: Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON`'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j134-missing-or-invalid-google-service-account
related: []
docs:
- setup/wizard/tests/test_google.py
- tests/wizard/test_verify.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Failure and recovery
raw_id: TST-032
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Missing or invalid `GOOGLE_SERVICE_ACCOUNT_JSON`.

## Evidence and reproduction

- **Journeys:** J-134
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'GOOGLE_SERVICE_ACCOUNT_JSON|getServiceAccountEmail'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/wizard/tests/test_google.py, tests/wizard/test_verify.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Step 1 returns `{email:""}`; step 2 `Service account email not configured on this Worker.` or `GOOGLE_SERVICE_ACCOUNT_JSON is not valid JSON.`; step 3 `{accessible:false,title:""}` (errors swallowed). The SheetConnectionCard then shows no service-account email to share with: confirm the card tells the user it is a server misconfiguration, not their sheet.
- **Fix hint:** add a test that asserts: missing or invalid GOOGLE_SERVICE_ACCOUNT_JSON returns the documented errors and the card tells the user. Test file suggestion: worker/src/sheets.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: missing or invalid GOOGLE_SERVICE_ACCOUNT_JSON returns the documented errors and the card tells the user. Test file suggestion: worker/src/sheets.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-032). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
