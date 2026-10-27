---
id: 2026-10-27-lr-094-trending-falls-back-to-hard-coded
title: Trending falls back to hard-coded mock data when no API is enabled, with no clear sample label
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j051-trending-panels-youtube-linkedin-instagram-use
related: []
docs:
- frontend/src/features/trending/hooks/useTrending.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P2
area: frontend/feed
raw_id: LR-094
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Trending falls back to hard-coded mock data when no API is enabled, with no clear sample label. Suspected, not confirmed (see Confidence in the evidence).

## Evidence and reproduction

- **Confidence:** hypothesis
- **Journeys:** J-041, J-051
- **Aliases:** FEB-020, NEW-6, U-J11
- **Evidence:** frontend/src/features/trending/hooks/useTrending.ts:213-225,280-292
- **Repro:** open trending with no keys configured.
- **Fix hint:** Return an empty connect-a-source state or label the data as sample; confirm production always has real APIs.

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return an empty connect-a-source state or label the data as sample; confirm production always has real APIs.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-094). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: hypothesis from static reading of frontend/src/features/trending/hooks/useTrending.ts:213-225,280-292; confirm by running the Repro and observing the described behaviour.
