---
id: 2026-10-27-tst-025-no-automated-test-asserts-newsletter-actions
title: 'No automated test asserts: Newsletter actions are not tenant-scoped'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j112-newsletter-actions-are-not-tenant-scoped
related: []
docs:
- tests-e2e/e2e/journeys/65-wiring-loop40.spec.ts
- tests-e2e/e2e/journeys/57-wiring-loop33.spec.ts
- tests-e2e/e2e/journeys/63-wiring-loop37.spec.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: test-gap
severity: P0
area: Newsletter
raw_id: TST-025
source_file: docs/launch-readiness/findings/TEST-COVERAGE.md
---

## Problem

No automated test asserts: Newsletter actions are not tenant-scoped.

## Evidence and reproduction

- **Journeys:** J-112
- **Status:** open
- **Confidence:** confirmed-by-reading
- **Evidence:** `grep -rIlE 'approveNewsletterIssue|newsletter\.approveIssue|handleDeleteNewsletter'` over worker/src, frontend/src, frontend/tests/e2e, tests-e2e, tests, setup and generation-worker test files returned 3 file(s): tests-e2e/e2e/journeys/65-wiring-loop40.spec.ts, tests-e2e/e2e/journeys/57-wiring-loop33.spec.ts, tests-e2e/e2e/journeys/63-wiring-loop37.spec.ts. None of these asserts the pass check (they match the term in an unrelated assertion or a mock).
- **Repro:** Desired: all refused (not found / forbidden). CODE-READING FINDING: these handlers take only `issueId`/`newsletterId` and run `WHERE id = ?` with no `spreadsheet_id` or user check (`handleApproveNewsletterIssue(db, issueId)`, `handleSendApprovedNewsletterIssue`, `handleDeleteNewsletter(db, newsletterId)`). Ids are UUID-like so exploitation needs the id, but ids appear in URLs/UI/exports. Cross-tenant read/modify/s...
- **Fix hint:** add a test that asserts: approve, send and delete newsletter actions on another tenant's id are refused. Test file suggestion: worker/src/newsletter/__tests__/tenancy.test.ts

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

add a test that asserts: approve, send and delete newsletter actions on another tenant's id are refused. Test file suggestion: worker/src/newsletter/__tests__/tenancy.test.ts

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/TEST-COVERAGE.md (TST-025). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: grepped test globs and read test titles for the journey's route/action/message text; no test run.
