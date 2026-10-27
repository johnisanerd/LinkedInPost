---
id: 2026-10-27-tst-026-no-automated-test-asserts-llm-provider
title: 'No automated test asserts: LLM provider failure and fallback'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j122-llm-provider-failure-and-fallback
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
area: Settings, models and providers
raw_id: TST-026
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: LLM provider failure and fallback.

## Evidence and reproduction

- **Journeys:** J-122
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'resolveFallbackForGeneration|llmProvider'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned no files. No test touches this journey.
- **Repro:** Where a fallback is configured (`resolveFallbackForGeneration`) the call succeeds and `llmProvider` in the result names the fallback; otherwise a readable error reaches the user (not `[object Object]`, not a raw API key in the text); usage rows recorded in `llm_usage_log` only for successful calls (check token accounting on failures).
- **Fix hint:** add a test that asserts: on provider failure the fallback is used and llmProvider names it; otherwise a readable error is returned. Test file suggestion: worker/src/llm-fallback.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: on provider failure the fallback is used and llmProvider names it; otherwise a readable error is returned. Test file suggestion: worker/src/llm-fallback.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-026). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
