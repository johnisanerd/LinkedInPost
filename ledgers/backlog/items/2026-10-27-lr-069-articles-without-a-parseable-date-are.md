---
id: 2026-10-27-lr-069-articles-without-a-parseable-date-are
title: Articles without a parseable date are stamped now, so old news passes the window and reaches prompts as fresh
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- worker/src/researcher/providers/rss.ts
- worker/src/researcher/providers/newsApis.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/researcher
raw_id: LR-069
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Articles without a parseable date are stamped now, so old news passes the window and reaches prompts as fresh.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041, J-044, J-052, J-053
- **Aliases:** WKB-021, GWP-015
- **Evidence:** worker/src/researcher/providers/rss.ts:28-35,60-67; worker/src/researcher/providers/newsApis.ts:46,97,146,198-200
- **Repro:** static. Executor: feed an RSS item with no pubDate; run `searchNewsResearch`.
- **Fix hint:** Keep publishedAt empty when unknown, exclude undated items from windowed searches, parse SerpApi relative dates through one date function.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Keep publishedAt empty when unknown, exclude undated items from windowed searches, parse SerpApi relative dates through one date function.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-069). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/researcher/providers/rss.ts:28-35,60-67.
