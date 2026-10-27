---
id: 2026-10-27-cons-023-evergreen-sort-uses-real-signal
title: Evergreen sort uses real signal
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-174-evergreen-and-top-10-are-ranked
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/feed
raw_id: CONS-023
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Evergreen sort uses real signal.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C02-13
- **Alias:** C02-13
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** FeedCuratedPanel.tsx:89-92,152-154 (description length) (Top10 also uses desc length + recency)
- **Covered by:** LR-174

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-023). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (Top10 also uses desc length + recency); covered by LR-174.
