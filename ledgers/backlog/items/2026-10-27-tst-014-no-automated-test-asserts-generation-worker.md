---
id: 2026-10-27-tst-014-no-automated-test-asserts-generation-worker
title: 'No automated test asserts: Generation worker is open when `WORKER_SHARED_SECRET` is empty'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j060-generation-worker-is-open-when-worker
related: []
docs:
- setup/wizard/tests/test_apikeys.py
- tests/setup/test_setup_wiring.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Draft generation (SSE)
raw_id: TST-014
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Generation worker is open when `WORKER_SHARED_SECRET` is empty.

## Evidence and reproduction

- **Journeys:** J-060
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'WORKER_SHARED_SECRET|checkAuth'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): setup/wizard/tests/test_apikeys.py, tests/setup/test_setup_wiring.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: 401 `{"error":"Unauthorized"}`. CODE-READING FINDING: `checkAuth` returns `true` when the secret is empty, and CORS is `Access-Control-Allow-Origin: *`; anyone can run the LLM pipeline on the operator's keys. The setup path generates the secret, but a manual deploy or a skipped secret leaves it open with no warning. Also, `Authorization` is compared as `Bearer <secret>` or the bare secret (string `===`, n...
- **Fix hint:** add a test that asserts: checkAuth rejects requests when WORKER_SHARED_SECRET is empty. Test file suggestion: generation-worker/src/auth.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: checkAuth rejects requests when WORKER_SHARED_SECRET is empty. Test file suggestion: generation-worker/src/auth.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-014). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
