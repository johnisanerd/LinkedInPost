---
id: 2026-10-27-lr-087-news-research-selections-keep-feeding-every
title: News-research selections keep feeding every prompt after the panel is closed or the topic changes, with no indicator
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j066-variants-preview-for-a-selection
related: []
docs:
- frontend/src/features/review/context/useReviewFlowActions.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/editor
raw_id: LR-087
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

News-research selections keep feeding every prompt after the panel is closed or the topic changes, with no indicator.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-052, J-065, J-066
- **Aliases:** FEA-023
- **Evidence:** frontend/src/features/news-research/ResearcherPanel.tsx:87-120; frontend/src/features/review/context/useReviewFlowActions.ts:175
- **Repro:** Select 2 articles, switch to Styles tab, run Quick Change: request includes the articles; open another topic: still included.
- **Fix hint:** Reset researchContextArticles on topic change and show a sources-attached chip outside the News tab.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Reset researchContextArticles on topic change and show a sources-attached chip outside the News tab.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-087). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/news-research/ResearcherPanel.tsx:87-120.
