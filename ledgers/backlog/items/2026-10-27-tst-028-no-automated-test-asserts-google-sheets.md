---
id: 2026-10-27-tst-028-no-automated-test-asserts-google-sheets
title: 'No automated test asserts: Google Sheets unavailable or unshared during topic list'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j129-google-sheets-unavailable-or-unshared-during
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Failure and recovery
raw_id: TST-028
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Google Sheets unavailable or unshared during topic list.

## Evidence and reproduction

- **Journeys:** J-129
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'falling back to D1|out of sync'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** `getRows` falls back to D1 rows (`console.error('[getRows] Sheets merge failed, falling back to D1')`) and the UI loads; no banner tells the user the sheet is out of sync (CODE-READING FINDING). Writes: D1 updates succeed; sheet mirroring errors in `updateRowStatus`/`publishContent` must not block publishing or must be reported. After restore, rows reconcile without duplicates or lost edits.
- **Fix hint:** add a test that asserts: getRows falls back to D1 when Sheets merge fails and the UI shows an out-of-sync notice. Test file suggestion: worker/src/topics.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: getRows falls back to D1 when Sheets merge fails and the UI shows an out-of-sync notice. Test file suggestion: worker/src/topics.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-028). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
