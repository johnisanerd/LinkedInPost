---
id: 2026-10-27-cons-020-two-panel-layout-trending-rail-top
title: Two-panel layout, trending rail top carousel <lg
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
raw_id: CONS-020
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Two-panel layout, trending rail top carousel <lg.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-10
- **Alias:** C02-10
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** FeedPage.tsx:1340 hidden lg:flex, no carousel (rail simply disappears on tablet/phone)
- **Covered by:** LR-095

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-020). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (rail simply disappears on tablet/phone); covered by LR-095.
