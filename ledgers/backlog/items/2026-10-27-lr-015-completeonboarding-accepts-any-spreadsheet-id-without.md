---
id: 2026-10-27-lr-015-completeonboarding-accepts-any-spreadsheet-id-without
title: completeOnboarding accepts any spreadsheet id without ownership proof, which scopes another tenant's data and gives access to their sheet.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j029-first-sign-in-shows-onboarding-skipping
- 2026-10-27-j030-onboarding-with-a-sheet-url-drive
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
- 2026-10-27-j141-two-tenants-connect-the-same-google
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
severity: P0
area: worker/tenancy
raw_id: LR-015
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

completeOnboarding accepts any spreadsheet id without ownership proof, which scopes another tenant's data and gives access to their sheet.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-029, J-030, J-140, J-141
- **Aliases:** WKA-005, WKB-003
- **Evidence:** worker/src/index.ts:2819-2826
- **Repro:** static. Executor: tenant B calls `completeOnboarding` with tenant A's sheet id, then `getRows`.
- **Fix hint:** Remove spreadsheetId from completeOnboarding (use connectSpreadsheet only) or run the same share-and-verify step; reject ids with the feed: prefix and ids bound to another user.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remove spreadsheetId from completeOnboarding (use connectSpreadsheet only) or run the same share-and-verify step; reject ids with the feed: prefix and ids bound to another user.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-015). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:2819-2826.
