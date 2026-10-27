---
id: 2026-10-27-lr-118-the-news-window-excludes-its-end
title: The news window excludes its end day because a date-only windowEnd parses to midnight UTC, dropping today's articles.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- packages/researcher/src/search.ts
- generation-worker/src/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: packages/researcher
raw_id: LR-118
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The news window excludes its end day because a date-only windowEnd parses to midnight UTC, dropping today's articles.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-052, J-053
- **Aliases:** GWP-012
- **Evidence:** packages/researcher/src/search.ts:14-21; generation-worker/src/pipeline.ts:80-81
- **Repro:** static; with an RSS item published an hour ago and default window, it is dropped.
- **Fix hint:** Treat a date-only end as end-of-day or compare by slice(0,10).

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Treat a date-only end as end-of-day or compare by slice(0,10).

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-118). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of packages/researcher/src/search.ts:14-21.
