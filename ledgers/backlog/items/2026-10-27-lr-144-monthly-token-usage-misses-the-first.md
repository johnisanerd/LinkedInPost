---
id: 2026-10-27-lr-144-monthly-token-usage-misses-the-first
title: Monthly token usage misses the first day of each month because a space-separated timestamp is compared with an ISO T string
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j124-usage-meter-and-usage-page
- 2026-10-27-j125-monthly-token-budget-exhausted
related: []
docs:
- worker/src/db/users.ts
- worker/src/db/llm-usage.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/db
raw_id: LR-144
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Monthly token usage misses the first day of each month because a space-separated timestamp is compared with an ISO T string.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-124, J-125
- **Aliases:** WKA-014, WKB-041
- **Evidence:** worker/src/db/users.ts:123-140; worker/src/db/llm-usage.ts:31-45
- **Repro:** static. Executor: insert a log row dated the 1st via the app and read `/api/usage`.
- **Fix hint:** Compare with datetime(?) or format the bound as YYYY-MM-DD HH:MM:SS; keep usage rows at least 31 days.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Compare with datetime(?) or format the bound as YYYY-MM-DD HH:MM:SS; keep usage rows at least 31 days.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-144). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/db/users.ts:123-140.
