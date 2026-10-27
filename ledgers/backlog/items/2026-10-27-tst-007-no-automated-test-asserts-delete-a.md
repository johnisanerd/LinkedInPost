---
id: 2026-10-27-tst-007-no-automated-test-asserts-delete-a
title: 'No automated test asserts: Delete a topic (and its generated images)'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j039-delete-a-topic-and-its-generated
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
area: Topic capture and scratchpad
raw_id: TST-007
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Delete a topic (and its generated images).

## Evidence and reproduction

- **Journeys:** J-039
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'deleteRow|deleteTopic'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** D1 `pipeline_state` row and news snapshots removed, GCS objects for the topic prefix removed, sheet row removed. Order in code is: GCS delete, then D1 delete in parallel with snapshot delete, then `sheets.deleteRow` last; a Sheets failure leaves the D1 row gone but the sheet row present, and the next merge may resurrect it (CODE-READING FINDING). No soft-delete / undo.
- **Fix hint:** add a test that asserts: deleteRow removes the D1 row, snapshots, GCS objects and the sheet row, and reports a Sheets failure. Test file suggestion: worker/src/topics.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: deleteRow removes the D1 row, snapshots, GCS objects and the sheet row, and reports a Sheets failure. Test file suggestion: worker/src/topics.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-007). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
