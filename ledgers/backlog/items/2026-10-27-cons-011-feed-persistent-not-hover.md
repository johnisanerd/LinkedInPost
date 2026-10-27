---
id: 2026-10-27-cons-011-feed-persistent-not-hover
title: 'Feed: persistent 👍👎✂ (not hover)'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-095-feed-vote-and-clip-actions-are
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/feed
raw_id: CONS-011
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Feed: persistent 👍👎✂ (not hover).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-1
- **Alias:** C02-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/feed/components/FeedArticleCard.tsx:~97 (opacity-0 group-hover:opacity-100 pointer-events-none) (touch users cannot vote/clip from stream; 26px targets (<40px AC))
- **Covered by:** LR-095

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-011). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (touch users cannot vote/clip from stream; 26px targets (<40px AC)); covered by LR-095.
