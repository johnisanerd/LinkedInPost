---
id: 2026-10-27-cons-015-search-input-in-feed-desc-toggle
title: Search input in feed (+desc toggle)
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
raw_id: CONS-015
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Search input in feed (+desc toggle).

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C02-5
- **Alias:** C02-5
- **Original tag:** MED/HIGH (mixed tag, higher taken: P1)
- **Current status:** partial
- **Evidence:** FeedPage.tsx:109-111, 536-575 (debounced client filter on loaded items) (no "search description" toggle)
- **Covered by:** FZ-002

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-015). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-002 (see findings/FROZEN.md); no "search description" toggle
