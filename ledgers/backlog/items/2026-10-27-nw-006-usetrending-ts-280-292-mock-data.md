---
id: 2026-10-27-nw-006-usetrending-ts-280-292-mock-data
title: useTrending.ts:280-292 mock-data path still present for !useRealApis; confirm production always has real APIs or users could see mock trending.
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-094-trending-falls-back-to-hard-coded
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: new-finding
severity: P2
area: frontend/trending
raw_id: NW-006
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

useTrending.ts:280-292 mock-data path still present for !useRealApis; confirm production always has real APIs or users could see mock trending.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md, row NEW-6
- **Alias:** NEW-6
- **Original tag:** new (not in a source; no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** none given
- **Covered by:** LR-094

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (NW-006). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (no code evidence given by reconciler); covered by LR-094.
