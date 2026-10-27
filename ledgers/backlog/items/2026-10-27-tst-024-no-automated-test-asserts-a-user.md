---
id: 2026-10-27-tst-024-no-automated-test-asserts-a-user
title: 'No automated test asserts: A user with no LinkedIn connection publishes through someone else''s token'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j103-a-user-with-no-linkedin-connection
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Connections and OAuth
raw_id: TST-024
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: A user with no LinkedIn connection publishes through someone else's token.

## Evidence and reproduction

- **Journeys:** J-103
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'LinkedIn publishing is not configured|shared-config'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: B gets `LinkedIn publishing is not configured...`/"connect your account" and nothing is posted. Expected to FAIL today in multi-tenant deployments (single-owner self-hosted is fine and relies on this fallback).
- **Fix hint:** add a test that asserts: a user without a LinkedIn connection gets 'connect your account' and nothing is posted with the shared KV token. Test file suggestion: worker/src/publish.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a user without a LinkedIn connection gets 'connect your account' and nothing is posted with the shared KV token. Test file suggestion: worker/src/publish.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-024). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
