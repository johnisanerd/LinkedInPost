---
id: 2026-10-27-tst-023-no-automated-test-asserts-oauth-misconfiguration
title: 'No automated test asserts: OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j101-oauth-misconfiguration-missing-or-wrong-client
related: []
docs:
- frontend/tests/e2e/journeys/07-connections-setup.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Connections and OAuth
raw_id: TST-023
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: OAuth misconfiguration: missing or wrong client id/secret, wrong redirect URI.

## Evidence and reproduction

- **Journeys:** J-101
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'LinkedIn OAuth is not configured|linkedinAuthAvailable'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** (a) HTTP 400 `LinkedIn OAuth is not configured in the Worker environment. Add LINKEDIN_CLIENT_ID and LINKEDIN_CLIENT_SECRET first.`; the UI card should hide Connect when `linkedinAuthAvailable` is false. CODE-READING FINDING: for every failure `handleConnect` only does `console.error('OAuth connect failed:', err)`, so the user sees nothing happen. (b)-(d) fail inside the provider popup page; the operator needs a d...
- **Fix hint:** add a test that asserts: a failed startLinkedInAuth shows the missing client id message and hides Connect. Test file suggestion: frontend/tests/e2e/journeys/07-connections-setup.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a failed startLinkedInAuth shows the missing client id message and hides Connect. Test file suggestion: frontend/tests/e2e/journeys/07-connections-setup.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-023). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
