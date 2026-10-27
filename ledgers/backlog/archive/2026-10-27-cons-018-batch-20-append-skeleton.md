---
id: 2026-10-27-cons-018-batch-20-append-skeleton
title: Batch 20 + append skeleton
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
severity: P2
area: frontend/feed
raw_id: CONS-018
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Batch 20 + append skeleton.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C02-8
- **Alias:** C02-8
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** FeedLeftPanel.tsx:39 BATCH_SIZE=20; :28,:116 skeletons (skeleton only on initial load; "Load more" fallback exists :206)
- **Covered by:** FZ-002

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-018). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-002 (see findings/FROZEN.md); skeleton only on initial load; "Load more" fallback exists :206
