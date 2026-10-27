---
id: 2026-10-27-lr-090-feed-refresh-replaces-a-multi-topic
title: Feed refresh replaces a multi-topic group with only the first topic's results, and the cache is not invalidated when a group is edited.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j042-refresh-the-feed-on-demand
- 2026-10-27-j043-interest-groups-create-edit-delete
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
area: frontend/feed
raw_id: LR-090
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Feed refresh replaces a multi-topic group with only the first topic's results, and the cache is not invalidated when a group is edited.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041..J-043
- **Aliases:** FEA-018, WKA-034
- **Evidence:** frontend/src/features/feed/FeedPage.tsx:235-250,330-375; worker/src/index.ts:1746-1811
- **Repro:** Group with topics A,B: feed shows both; click refresh: only A's articles.
- **Fix hint:** Refresh per topic in parallel with a timeout, merge and dedupe, clear the feed store when a group is saved, return the refresh error.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Refresh per topic in parallel with a timeout, merge and dedupe, clear the feed store when a group is saved, return the refresh error.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-090). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/FeedPage.tsx:235-250,330-375.
