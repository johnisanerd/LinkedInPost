---
id: 2026-10-27-tst-037-no-automated-test-asserts-per-user
title: 'No automated test asserts: Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows)'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j142-per-user-lists-are-scoped-clips
related: []
docs:
- frontend/tests/e2e/feed-page.spec.ts
- frontend/tests/e2e/journeys/21-wiring-issues.spec.ts
- frontend/tests/e2e/journeys/10-trending-research.spec.ts
- frontend/tests/e2e/journeys/12-feed-feature.spec.ts
- tests-e2e/e2e/journeys/51-wiring-loop30.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P1
area: Data isolation between tenants
raw_id: TST-037
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Per-user lists are scoped (clips, groups, feedback, integrations, personas, workflows).

## Evidence and reproduction

- **Journeys:** J-142
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'listCustomPersonas|listInterestGroups|user_id'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 15 file(s): frontend/tests/e2e/feed-page.spec.ts, frontend/tests/e2e/journeys/21-wiring-issues.spec.ts, frontend/tests/e2e/journeys/10-trending-research.spec.ts, frontend/tests/e2e/journeys/12-feed-feature.spec.ts, tests-e2e/e2e/journeys/51-wiring-loop30.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Lists contain only A's rows; mutations on B's ids change nothing / error (statements are `WHERE user_id = ?`).
- **Fix hint:** add a test that asserts: clips, groups, feedback, integrations, personas and workflows are scoped to user_id. Test file suggestion: worker/src/tenancy.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: clips, groups, feedback, integrations, personas and workflows are scoped to user_id. Test file suggestion: worker/src/tenancy.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-037). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
