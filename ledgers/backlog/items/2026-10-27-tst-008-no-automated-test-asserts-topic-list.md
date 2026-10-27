---
id: 2026-10-27-tst-008-no-automated-test-asserts-topic-list
title: 'No automated test asserts: Topic list merges Sheets and D1'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
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
raw_id: TST-008
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Topic list merges Sheets and D1.

## Evidence and reproduction

- **Journeys:** J-040
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'Sheets merge failed|mergeRows|merged-rows'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** New sheet row appears after reload with `topicId` assigned; counts per status match; no duplicate rows for topics that exist in both stores.
- **Fix hint:** add a test that asserts: getRows merges Sheets and D1 with no duplicates and correct status counts. Test file suggestion: worker/src/topics.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: getRows merges Sheets and D1 with no duplicates and correct status counts. Test file suggestion: worker/src/topics.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-008). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
