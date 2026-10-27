---
id: 2026-10-27-tst-004-no-automated-test-asserts-worker-without
title: 'No automated test asserts: Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j028-worker-without-google-client-id-accepts
related: []
docs:
- setup/tests/test_github_bugfix.py
- setup/wizard/tests/test_google.py
- tests/setup/test_github.py
- tests-e2e/e2e/journeys/22-wiring-issues-round1.spec.ts
- tests-e2e/e2e/setup-flow.spec.ts
- worker/src/auth.test.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Sign-in and session
raw_id: TST-004
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Worker without `GOOGLE_CLIENT_ID` accepts tokens minted for other apps.

## Evidence and reproduction

- **Journeys:** J-028
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'audience does not match|GOOGLE_CLIENT_ID'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 5 file(s): setup/tests/test_github_bugfix.py, setup/wizard/tests/test_google.py, tests/setup/test_github.py, tests-e2e/e2e/journeys/22-wiring-issues-round1.spec.ts, tests-e2e/e2e/setup-flow.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: `Unauthorized: Google token audience does not match this app.` or a startup refusal. CODE-READING FINDING: the audience check is `if (env.GOOGLE_CLIENT_ID && tokenInfo.aud !== env.GOOGLE_CLIENT_ID)`, so with the variable unset the check is skipped and token verification relies on Google tokeninfo only. Combined with J-017 any Google user gets in.
- **Fix hint:** add a test that asserts: verifySession with GOOGLE_CLIENT_ID unset rejects a token whose aud is another app. Test file suggestion: worker/src/auth.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: verifySession with GOOGLE_CLIENT_ID unset rejects a token whose aud is another app. Test file suggestion: worker/src/auth.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
