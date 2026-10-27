---
id: 2026-10-27-tst-036-no-automated-test-asserts-tenant-a
title: 'No automated test asserts: Tenant A cannot read or modify tenant B''s topics'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
related: []
docs:
- frontend/tests/e2e/journeys/13-enrichment-pipeline.spec.ts
- tests-e2e/e2e/journeys/13-enrichment-pipeline.spec.ts
- tests-e2e/e2e/journeys/60-wiring-loop34.spec.ts
- tests-e2e/e2e/journeys/28-wiring-loop20.spec.ts
- tests-e2e/e2e/journeys/44-wiring-loop28.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Data isolation between tenants
raw_id: TST-036
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Tenant A cannot read or modify tenant B's topics.

## Evidence and reproduction

- **Journeys:** J-140
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'user_id|getNodeRuns|Topic not found'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 5 file(s): frontend/tests/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/13-enrichment-pipeline.spec.ts, tests-e2e/e2e/journeys/60-wiring-loop34.spec.ts, tests-e2e/e2e/journeys/28-wiring-loop20.spec.ts, tests-e2e/e2e/journeys/44-wiring-loop28.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Step 2 empty of B's rows. Step 3: every write is scoped by `user_id = A` in `pipeline_state` (PK `(user_id, topic_id)` per migration 0010), so none change B's data (A's call creates/updates only A's own row or fails with `Topic not found.`); `getNodeRuns` returns only rows with `user_id = A`. Verify by reading B's row afterwards. Note that `updateRowStatus` / `upsertFull` accept a client-supplied full row (includi...
- **Fix hint:** add a test that asserts: tenant A cannot read or write tenant B's topics, and getNodeRuns returns only A's rows. Test file suggestion: worker/src/tenancy.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: tenant A cannot read or write tenant B's topics, and getNodeRuns returns only A's rows. Test file suggestion: worker/src/tenancy.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-036). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
