---
id: 2026-10-27-lr-072-tenants-without-a-sheet-work-in
title: Tenants without a sheet work in D1, but the frontend shows a pending wall to non-admins and the worker throws on actions that only need D1.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j029-first-sign-in-shows-onboarding-skipping
- 2026-10-27-j031-non-admin-without-a-connected-sheet
- 2026-10-27-j039-delete-a-topic-and-its-generated
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j082-schedule-a-future-post-queued-via
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/tenancy
raw_id: LR-072
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Tenants without a sheet work in D1, but the frontend shows a pending wall to non-admins and the worker throws on actions that only need D1.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-029, J-031, J-039, J-065, J-076, J-082
- **Aliases:** FEB-003, WKA-009
- **Evidence:** frontend/src/components/dashboard/index.tsx:581-595; worker/src/index.ts:3111-3114,1573,2404
- **Repro:** sign in as an approved non-admin tenant, skip the sheet in onboarding, observe /connections shows the pending card.
- **Fix hint:** Drop ensureSpreadsheetConfigured in actions that only need D1 and always allow /connections, /usage, /rules; or require a sheet in onboarding and document it.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Drop ensureSpreadsheetConfigured in actions that only need D1 and always allow /connections, /usage, /rules; or require a sheet in onboarding and document it.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-072). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/index.tsx:581-595.
