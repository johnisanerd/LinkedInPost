---
id: 2026-10-27-tst-027-no-automated-test-asserts-empty-admin
title: 'No automated test asserts: Empty `ADMIN_EMAILS` makes the repo owner an admin'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j127-empty-admin-emails-makes-the-repo
related: []
docs:
- worker/src/auth.test.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Admin, tenant and budget
raw_id: TST-027
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Empty `ADMIN_EMAILS` makes the repo owner an admin.

## Evidence and reproduction

- **Journeys:** J-127
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'DEFAULT_ADMIN_EMAIL|ADMIN_EMAILS|99pratyush'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: with no `ADMIN_EMAILS`, nobody is admin (or deploy refuses). CODE-READING FINDING: `resolveAdminEmailAllowlist` falls back to `DEFAULT_ADMIN_EMAIL = '99pratyush@gmail.com'`, so on any customer's deployment missing the variable, the project author gets admin (shared config, tokens, all users) and the real operator is not admin. The committed `worker/wrangler.jsonc` also lists the owner's and another person...
- **Fix hint:** add a test that asserts: with ADMIN_EMAILS unset nobody is admin. Test file suggestion: worker/src/auth.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: with ADMIN_EMAILS unset nobody is admin. Test file suggestion: worker/src/auth.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-027). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
