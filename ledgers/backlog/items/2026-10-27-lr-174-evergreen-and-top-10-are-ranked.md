---
id: 2026-10-27-lr-174-evergreen-and-top-10-are-ranked
title: Evergreen and Top 10 are ranked by description length and recency, not a real signal
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
raw_id: LR-174
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Evergreen and Top 10 are ranked by description length and recency, not a real signal.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041
- **Aliases:** C02-13
- **Evidence:** frontend/src/features/feed/components/FeedCuratedPanel.tsx:89-92,152-154
- **Repro:** (static check) Open frontend/src/features/feed/components/FeedCuratedPanel.tsx:89-92,152-154 and confirm the behaviour described in the summary; then exercise the matching journey (J-041) to observe it.
- **Fix hint:** Relabel the sections or use a real signal.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Relabel the sections or use a real signal.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-174). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/FeedCuratedPanel.tsx:89-92,152-154.
