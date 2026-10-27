---
id: 2026-10-27-tst-011-no-automated-test-asserts-send-to
title: 'No automated test asserts: "Send to Generation" button on a saved Draft topic'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j056-send-to-generation-button-on-a
related: []
docs:
- frontend/tests/e2e/journeys/03-generate-draft.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Draft generation (SSE)
raw_id: TST-011
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: "Send to Generation" button on a saved Draft topic.

## Evidence and reproduction

- **Journeys:** J-056
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'sendTopicToGeneration|Send to Generation'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Desired: Row moves Draft -> Pending -> has 4 variants and the UI shows them on `/topics/:topicId`. Currently expected to FAIL.
- **Fix hint:** add a test that asserts: Send to Generation moves a Draft topic to Pending and shows 4 variants. Test file suggestion: frontend/tests/e2e/journeys/03-generate-draft.spec.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: Send to Generation moves a Draft topic to Pending and shows 4 variants. Test file suggestion: frontend/tests/e2e/journeys/03-generate-draft.spec.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-011). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
