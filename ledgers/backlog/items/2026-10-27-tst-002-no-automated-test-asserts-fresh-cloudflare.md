---
id: 2026-10-27-tst-002-no-automated-test-asserts-fresh-cloudflare
title: 'No automated test asserts: Fresh Cloudflare account against the committed wrangler ids'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j003-fresh-cloudflare-account-against-the-committed
related: []
docs:
- setup/wizard/tests/test_verify.py
- setup/wizard/steps/test_verify.py
- tests/setup/test_setup_wiring.py
- tests/wizard/test_verify.py
- tests/test_wrangler_reload_fix.py
- tests/setup/test_worker_config.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: First-run, setup and install
raw_id: TST-002
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Fresh Cloudflare account against the committed wrangler ids.

## Evidence and reproduction

- **Journeys:** J-003
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'wrangler.jsonc|ALLOWED_EMAILS|ADMIN_EMAILS'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 6 file(s): setup/wizard/tests/test_verify.py, setup/wizard/steps/test_verify.py, tests/setup/test_setup_wiring.py, tests/wizard/test_verify.py, tests/test_wrangler_reload_fix.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** After setup, `worker/wrangler.jsonc` `d1_databases[0].database_id` equals an id returned by `npx wrangler d1 list` for the operator's account, and `ADMIN_EMAILS` / `ALLOWED_EMAILS` contain the operator's email, not the owner's.
- **Fix hint:** add a test that asserts: assert wrangler.jsonc d1 database_id and ADMIN_EMAILS/ALLOWED_EMAILS are rewritten to the operator's values. Test file suggestion: tests/setup/test_worker_config.py

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: assert wrangler.jsonc d1 database_id and ADMIN_EMAILS/ALLOWED_EMAILS are rewritten to the operator's values. Test file suggestion: tests/setup/test_worker_config.py

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-002). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
