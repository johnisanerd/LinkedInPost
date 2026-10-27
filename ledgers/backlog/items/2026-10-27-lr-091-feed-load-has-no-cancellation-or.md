---
id: 2026-10-27-lr-091-feed-load-has-no-cancellation-or
title: Feed load has no cancellation or error state, so switching groups can show the previous group's articles and failures look like an empty feed.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j042-refresh-the-feed-on-demand
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/feed
raw_id: LR-091
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Feed load has no cancellation or error state, so switching groups can show the previous group's articles and failures look like an empty feed.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041, J-042
- **Aliases:** FEA-019
- **Evidence:** frontend/src/features/feed/FeedPage.tsx:328-378
- **Repro:** Throttle network, click group A then B quickly; or disable provider keys and open the feed: empty list, no error.
- **Fix hint:** Add a cancelled/request-id guard and an error state in the list.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a cancelled/request-id guard and an error state in the list.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-091). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/FeedPage.tsx:328-378.
