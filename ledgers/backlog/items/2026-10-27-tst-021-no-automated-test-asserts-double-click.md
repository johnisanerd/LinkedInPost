---
id: 2026-10-27-tst-021-no-automated-test-asserts-double-click
title: 'No automated test asserts: Double-click on Publish'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j088-double-click-on-publish
related: []
docs:
- setup/wizard/test_state.py
- frontend/tests/e2e/journeys/05-publish-linkedin.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Scheduling and publishing
raw_id: TST-021
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Double-click on Publish.

## Evidence and reproduction

- **Journeys:** J-088
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'double-click|actionLoading|idempotency'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 1 file(s): setup/wizard/test_state.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Exactly one post on LinkedIn. UI guard: `if (actionLoading !== null) return;` is React state, so two clicks in one tick may both pass; server guard: `publishContent` has no idempotency key and no "already Published" check for the immediate path (only `executeScheduledPublish` checks status). Expect two posts for the parallel curl (CODE-READING FINDING). A second click after completion goes through the "Republish"...
- **Fix hint:** add a test that asserts: two rapid clicks on Publish send exactly one publishContent call and one LinkedIn post. Test file suggestion: frontend/tests/e2e/journeys/05-publish-linkedin.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: two rapid clicks on Publish send exactly one publishContent call and one LinkedIn post. Test file suggestion: frontend/tests/e2e/journeys/05-publish-linkedin.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-021). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
