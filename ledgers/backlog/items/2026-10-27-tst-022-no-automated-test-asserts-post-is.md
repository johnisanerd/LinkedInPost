---
id: 2026-10-27-tst-022-no-automated-test-asserts-post-is
title: 'No automated test asserts: Post is live but marking it Published fails'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j089-post-is-live-but-marking-it
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
area: Scheduling and publishing
raw_id: TST-022
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Post is live but marking it Published fails.

## Evidence and reproduction

- **Journeys:** J-089
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'markRowPublished|Failed to send the approved message'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Order in code: send to channel first, then `markRowPublished` and `appendToPostedDoc`. A failure after a successful send surfaces "Failed to send the approved message..." to the user, the row stays `Approved`, and a retry posts a duplicate (CODE-READING FINDING). Pass requires the success to be reported or the retry to detect the existing post.
- **Fix hint:** add a test that asserts: when markRowPublished fails after a successful send, the user is told it posted and a retry does not duplicate. Test file suggestion: worker/src/publish.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: when markRowPublished fails after a successful send, the user is told it posted and a retry does not duplicate. Test file suggestion: worker/src/publish.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-022). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
