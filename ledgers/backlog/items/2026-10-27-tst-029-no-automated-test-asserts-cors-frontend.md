---
id: 2026-10-27-tst-029-no-automated-test-asserts-cors-frontend
title: 'No automated test asserts: CORS: frontend origin not allowed, or allowlist empty'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j131-cors-frontend-origin-not-allowed-or
related: []
docs:
- tests/setup/test_verification.py
- tests-e2e/e2e/setup-flow.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Failure and recovery
raw_id: TST-029
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: CORS: frontend origin not allowed, or allowlist empty.

## Evidence and reproduction

- **Journeys:** J-131
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'buildCorsHeaders|Access-Control-Allow-Origin|CORS'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): tests/setup/test_verification.py, tests-e2e/e2e/setup-flow.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Case 1: browser blocks the call; UI message built by `formatFetchNetworkFailure` explains the CORS variable and mixed content (if `http://` worker on an https page). Case 2: `buildCorsHeaders` returns `Access-Control-Allow-Origin: *` when the list is empty (fail-open) — acceptable only with token auth, but note `/api/waitlist` and webhooks are then callable from any site. Origins with a trailing slash or `127.0.0....
- **Fix hint:** add a test that asserts: a disallowed origin gets no ACAO header and an empty allowlist does not return *. Test file suggestion: worker/src/cors.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a disallowed origin gets no ACAO header and an empty allowlist does not return *. Test file suggestion: worker/src/cors.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-029). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
