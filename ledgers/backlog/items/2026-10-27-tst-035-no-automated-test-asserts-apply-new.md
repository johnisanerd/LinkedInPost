---
id: 2026-10-27-tst-035-no-automated-test-asserts-apply-new
title: 'No automated test asserts: Apply new D1 migrations on upgrade'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j137-apply-new-d1-migrations-on-upgrade
related: []
docs:
- frontend/tests/e2e/journeys/16-admin-panel.spec.ts
- worker/src/auth.test.ts
- setup/tests/test_cloudflare_bugfix_bug2.py
- setup/tests/test_cloudflare_bugfix.py
- tests-e2e/e2e/journeys/16-admin-panel.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Upgrade and migration
raw_id: TST-035
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Apply new D1 migrations on upgrade.

## Evidence and reproduction

- **Journeys:** J-137
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE '0019|monthly_token_budget|migrations'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 5 file(s): frontend/tests/e2e/journeys/16-admin-panel.spec.ts, worker/src/auth.test.ts, setup/tests/test_cloudflare_bugfix_bug2.py, setup/tests/test_cloudflare_bugfix.py, tests-e2e/e2e/journeys/16-admin-panel.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Lists 0001..0021 as applied; existing users keep working and become `status='active'` with `monthly_token_budget=500000` (defaults from 0019); `pipeline_state` rows preserved by the rebuild in 0010 (verify row counts before/after on a copy). Deploying code BEFORE migrating gives runtime `no such column/table` errors (J-133): the deploy workflow/docs must order migrate-then-deploy. The 0019 file header comment says...
- **Fix hint:** add a test that asserts: migrations 0001..0021 apply in order to a populated copy and keep users and pipeline_state rows. Test file suggestion: tests/setup/test_migrations.py

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: migrations 0001..0021 apply in order to a populated copy and keep users and pipeline_state rows. Test file suggestion: tests/setup/test_migrations.py

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-035). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
