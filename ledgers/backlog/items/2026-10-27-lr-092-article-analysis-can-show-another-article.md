---
id: 2026-10-27-lr-092-article-analysis-can-show-another-article
title: Article analysis can show another article summary because late responses overwrite state
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j046-article-analysis-and-insight-extraction
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/feed
raw_id: LR-092
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Article analysis can show another article summary because late responses overwrite state.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-046
- **Aliases:** FEA-020
- **Evidence:** frontend/src/features/feed/components/ArticleDetailView.tsx:150-176
- **Repro:** Open article A, immediately open article B with the keyboard shortcut; A's summary can replace B's.
- **Fix hint:** Use a cancelled flag keyed to article.url in both effects.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use a cancelled flag keyed to article.url in both effects.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-092). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/ArticleDetailView.tsx:150-176.
