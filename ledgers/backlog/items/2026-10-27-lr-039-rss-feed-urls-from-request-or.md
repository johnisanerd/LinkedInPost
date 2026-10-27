---
id: 2026-10-27-lr-039-rss-feed-urls-from-request-or
title: RSS feed URLs from request or config are fetched server-side with no scheme, host or size limits, allowing SSRF and memory exhaustion.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- packages/researcher/src/providers/rss.ts
- packages/researcher/src/config.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: packages/researcher
raw_id: LR-039
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

RSS feed URLs from request or config are fetched server-side with no scheme, host or size limits, allowing SSRF and memory exhaustion.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041, J-052, J-053
- **Aliases:** GWP-011, WKB-026 (RSS part)
- **Evidence:** packages/researcher/src/providers/rss.ts:81-94; packages/researcher/src/config.ts:5-38
- **Repro:** static; send newsResearchConfig with a 500 MB file URL or a localhost/internal URL.
- **Fix hint:** Require https, block private and loopback names, cap Content-Length and read at most about 1 MB.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Require https, block private and loopback names, cap Content-Length and read at most about 1 MB.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-039). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of packages/researcher/src/providers/rss.ts:81-94.
