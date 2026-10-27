---
id: 2026-10-27-tst-010-no-automated-test-asserts-rest-feed
title: 'No automated test asserts: REST feed and clip endpoints require auth'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j050-rest-feed-and-clip-endpoints-require
related: []
docs:
- frontend/tests/e2e/integration/error-states.spec.ts
- frontend/tests/e2e/feed-page.spec.ts
- tests/setup/test_github.py
- tests/wizard/test_apikeys.py
- tests/automations/test_youtube_poller.py
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Feed and clipping
raw_id: TST-010
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: REST feed and clip endpoints require auth.

## Evidence and reproduction

- **Journeys:** J-050
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'api/feed/items|api/clips|Unauthorized'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 6 file(s): frontend/tests/e2e/integration/error-states.spec.ts, frontend/tests/e2e/feed-page.spec.ts, tests/setup/test_github.py, tests/wizard/test_apikeys.py, tests/automations/test_youtube_poller.py. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Step 1 HTTP 401 `Unauthorized`; step 2 200 with only the caller's data (`interest_group_id` filtered by `user_id`); bad bodies get 4xx. Note the feed SELECT filters `news_snapshots` by `spreadsheet_id` (shared sheet = shared snapshots, see J-141).
- **Fix hint:** add a test that asserts: /api/feed and /api/clips return 401 without a token and only the caller's rows with one. Test file suggestion: worker/src/feed-routes.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: /api/feed and /api/clips return 401 without a token and only the caller's rows with one. Test file suggestion: worker/src/feed-routes.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-010). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
