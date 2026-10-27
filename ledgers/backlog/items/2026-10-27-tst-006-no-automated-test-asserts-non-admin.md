---
id: 2026-10-27-tst-006-no-automated-test-asserts-non-admin
title: 'No automated test asserts: Non-admin without a connected sheet is locked out of the whole workspace'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j031-non-admin-without-a-connected-sheet
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
severity: P0
area: Onboarding and workspace connection
raw_id: TST-006
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Non-admin without a connected sheet is locked out of the whole workspace.

## Evidence and reproduction

- **Journeys:** J-031
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Workspace setup pending'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: A sheetless user can reach `/connections`, connect a sheet, and use the app (or the app works D1-only). Currently expected to FAIL: the user sees only "Workspace setup pending".
- **Fix hint:** add a test that asserts: a non-admin with no sheet can reach /connections and use the app. Test file suggestion: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a non-admin with no sheet can reach /connections and use the app. Test file suggestion: frontend/tests/e2e/journeys/01-auth-onboarding.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-006). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
