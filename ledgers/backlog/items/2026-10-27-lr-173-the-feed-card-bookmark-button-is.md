---
id: 2026-10-27-lr-173-the-feed-card-bookmark-button-is
title: The feed card Bookmark button is a dead control (onClick only stops propagation)
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/feed
raw_id: LR-173
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The feed card Bookmark button is a dead control (onClick only stops propagation).

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041
- **Aliases:** NEW-1, C02-16
- **Evidence:** frontend/src/features/feed/components/FeedArticleCard.tsx:131
- **Repro:** (static check) Open frontend/src/features/feed/components/FeedArticleCard.tsx:131 and confirm the behaviour described in the summary; then exercise the matching journey (J-041) to observe it.
- **Fix hint:** Remove the button or wire it.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Remove the button or wire it.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-173). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/FeedArticleCard.tsx:131.
