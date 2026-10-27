---
id: 2026-10-27-lr-132-the-api-feed-limit-is-unvalidated
title: The /api/feed limit is unvalidated (NaN or negative returns the whole table), pagination is miscounted, and requests with no group return nothing.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j050-rest-feed-and-clip-endpoints-require
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
severity: P2
area: worker/api
raw_id: LR-132
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The /api/feed limit is unvalidated (NaN or negative returns the whole table), pagination is miscounted, and requests with no group return nothing.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041, J-044, J-050
- **Aliases:** WKA-022
- **Evidence:** worker/src/index.ts:6432-6488,6546-6588
- **Repro:** static. Executor: `GET /api/feed?limit=-1`, `?interest_group_id=<id>&limit=2`.
- **Fix hint:** Clamp limit to 1..100 integers, page on flattened articles, return the all-groups feed when none is given.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Clamp limit to 1..100 integers, page on flattened articles, return the all-groups feed when none is given.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-132). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:6432-6488,6546-6588.
