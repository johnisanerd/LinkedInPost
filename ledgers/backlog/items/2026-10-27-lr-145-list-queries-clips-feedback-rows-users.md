---
id: 2026-10-27-lr-145-list-queries-clips-feedback-rows-users
title: List queries (clips, feedback, rows, users, tenant settings) have no LIMIT, the admin users list is N+1, and the nightly prune does not scale.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j049-thumbs-up-down-on-an-article
- 2026-10-27-j119-daily-cron-housekeeping
- 2026-10-27-j123-admin-panel-users-approve-suspend-budget
related: []
docs:
- worker/src/db/clips.ts
- worker/src/modes/saas/admin.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/db
raw_id: LR-145
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

List queries (clips, feedback, rows, users, tenant settings) have no LIMIT, the admin users list is N+1, and the nightly prune does not scale.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-040, J-044, J-049, J-119, J-123
- **Aliases:** WKA-023
- **Evidence:** worker/src/db/clips.ts:55-62; worker/src/modes/saas/admin.ts:9-18
- **Repro:** static.
- **Fix hint:** Add LIMIT and cursor, aggregate usage in one GROUP BY query, prune per tenant incrementally.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add LIMIT and cursor, aggregate usage in one GROUP BY query, prune per tenant incrementally.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-145). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/db/clips.ts:55-62.
