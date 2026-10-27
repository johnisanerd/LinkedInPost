---
id: 2026-10-27-tst-012-no-automated-test-asserts-client-supplied
title: 'No automated test asserts: Client-supplied `spreadsheetId` overrides the server''s in generation'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j057-client-supplied-spreadsheetid-overrides-the-server
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
area: Draft generation (SSE)
raw_id: TST-012
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Client-supplied `spreadsheetId` overrides the server's in generation.

## Evidence and reproduction

- **Journeys:** J-057
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'storedConfig|spreadsheetId override'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: server ignores client `spreadsheetId` and uses `storedConfig.spreadsheetId`. CODE-READING FINDING: both handlers build `{ spreadsheetId: storedConfig.spreadsheetId, ...payload }`, so the client value wins (spread order). Check which downstream reads/writes in generation-worker use `spreadsheetId` (feedback, variants/clips by session, LLM settings keyed by spreadsheet) and whether B's data can be read or p...
- **Fix hint:** add a test that asserts: a client-supplied spreadsheetId is ignored in favour of the stored one. Test file suggestion: worker/src/generation-routes.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: a client-supplied spreadsheetId is ignored in favour of the stored one. Test file suggestion: worker/src/generation-routes.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-012). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
