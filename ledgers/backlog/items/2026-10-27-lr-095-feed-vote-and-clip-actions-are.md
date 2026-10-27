---
id: 2026-10-27-lr-095-feed-vote-and-clip-actions-are
title: Feed vote and clip actions are hover-only, the trending rail vanishes on small screens, and clips need drag-drop, so touch users are stuck.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j044-clip-an-article-or-a-passage
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
raw_id: LR-095
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Feed vote and clip actions are hover-only, the trending rail vanishes on small screens, and clips need drag-drop, so touch users are stuck.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041, J-044
- **Aliases:** C02-1, C02-10, C03-6, C13-7
- **Evidence:** frontend/src/features/feed/components/FeedArticleCard.tsx:97; frontend/src/features/feed/FeedPage.tsx:1340
- **Repro:** (static check) Open frontend/src/features/feed/components/FeedArticleCard.tsx:97 and confirm the behaviour described in the summary; then exercise the matching journey (J-041, J-044) to observe it.
- **Fix hint:** Make the action buttons visible on touch (CSS) and add an Add-to-topic menu per clip; defer the carousel.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Make the action buttons visible on touch (CSS) and add an Add-to-topic menu per clip; defer the carousel.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-095). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/FeedArticleCard.tsx:97.
