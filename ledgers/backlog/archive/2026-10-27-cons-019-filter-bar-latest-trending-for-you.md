---
id: 2026-10-27-cons-019-filter-bar-latest-trending-for-you
title: Filter bar Latest/Trending/For You
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-frz-002-feed-redesign-thumbnails-masonry-source-dedupe
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/feed
raw_id: CONS-019
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Filter bar Latest/Trending/For You.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C02-9
- **Alias:** C02-9
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** FeedPage.tsx:56,522-534,1063 ("For You" = hide downvoted only (:530); no per-topic pill beyond interest groups)
- **Covered by:** FZ-002

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-019). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-002 (see findings/FROZEN.md); "For You" = hide downvoted only (:530); no per-topic pill beyond interest groups
