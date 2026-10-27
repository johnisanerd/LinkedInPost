---
id: 2026-10-27-tst-034-no-automated-test-asserts-dev-auth
title: 'No automated test asserts: Dev auth bypass secret present in production'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j136-dev-auth-bypass-secret-present-in
related: []
docs:
- frontend/tests/e2e/cloud.spec.ts
- setup/tests/test_github_bugfix.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Failure and recovery
raw_id: TST-034
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Dev auth bypass secret present in production.

## Evidence and reproduction

- **Journeys:** J-136
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'tryResolveDevGoogleAuthBypassSession|DEV_GOOGLE_AUTH_BYPASS_SECRET'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): frontend/tests/e2e/cloud.spec.ts, setup/tests/test_github_bugfix.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: never accepted outside local dev. CODE-READING FINDING: `verifySession` calls `tryResolveDevGoogleAuthBypassSession` before any Google call and returns `{isAdmin:true}` if the secret matches; there is no environment guard (`wrangler dev` vs deployed). The only protection is the comment "Do not set these variables in production Worker secrets". Also if `VITE_DEV_GOOGLE_AUTH_BYPASS_SECRET` is baked into a p...
- **Fix hint:** add a test that asserts: the bypass secret is rejected when not running under wrangler dev. Test file suggestion: worker/src/plugins/dev-google-auth-bypass/resolve-session.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: the bypass secret is rejected when not running under wrangler dev. Test file suggestion: worker/src/plugins/dev-google-auth-bypass/resolve-session.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-034). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
