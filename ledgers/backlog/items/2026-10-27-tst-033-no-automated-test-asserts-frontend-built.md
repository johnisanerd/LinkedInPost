---
id: 2026-10-27-tst-033-no-automated-test-asserts-frontend-built
title: 'No automated test asserts: Frontend built with the wrong Google client id'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j135-frontend-built-with-the-wrong-google
related: []
docs:
- SETUP.md
- frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Failure and recovery
raw_id: TST-033
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Frontend built with the wrong Google client id.

## Evidence and reproduction

- **Journeys:** J-135
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'origin_mismatch|audience does not match'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Google popup shows `origin_mismatch`/`invalid_client` (origins) or bootstrap fails with `Unauthorized: Google token audience does not match this app.` shown in the red error box on the sign-in card; the operator doc (SETUP.md Step 2) lists the exact origins (`http://localhost:5173` only; `5174` used by `npm run dev` is not listed: CODE-READING FINDING).
- **Fix hint:** add a test that asserts: a wrong audience shows the red audience-mismatch error on the sign-in card. Test file suggestion: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a wrong audience shows the red audience-mismatch error on the sign-in card. Test file suggestion: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-033). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
