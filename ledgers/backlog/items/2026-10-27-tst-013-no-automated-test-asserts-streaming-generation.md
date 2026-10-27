---
id: 2026-10-27-tst-013-no-automated-test-asserts-streaming-generation
title: 'No automated test asserts: Streaming generation bypasses the monthly token budget'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j058-streaming-generation-bypasses-the-monthly-token
related: []
docs:
- worker/src/auth.test.ts
- setup/wizard/tests/test_apikeys.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Draft generation (SSE)
raw_id: TST-013
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Streaming generation bypasses the monthly token budget.

## Evidence and reproduction

- **Journeys:** J-058
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'checkTokenBudget|Monthly token budget exceeded|429'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 2 file(s): worker/src/auth.test.ts, setup/wizard/tests/test_apikeys.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: 429-style refusal on both. CODE-READING FINDING: `/api/quickchange/stream`, `generateQuickChange`, `generateVariantsPreview` and `callGenerationWorker` call `checkTokenBudget`; `/api/generate/stream` does not. Also `analyzeTopicInsights`, `analyzeFeedArticle`, `extractArticleInsights`, `clusterDraftClips`, `findDraftConnections`, `findDebateArticle`, `crossDomainInsight`, `opinionLeaderInsights`, `generat...
- **Fix hint:** add a test that asserts: POST /api/generate/stream refuses with 429 when the monthly budget is exhausted. Test file suggestion: worker/src/generation-routes.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: POST /api/generate/stream refuses with 429 when the monthly budget is exhausted. Test file suggestion: worker/src/generation-routes.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-013). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
