---
id: 2026-10-27-lr-117-rss-parsing-does-not-decode-entities
title: RSS parsing does not decode entities, Atom detection is brittle, and parse failures return zero items silently
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- worker/src/researcher/providers/rss.ts
- packages/researcher/src/providers/rss.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: packages/researcher
raw_id: LR-117
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

RSS parsing does not decode entities, Atom detection is brittle, and parse failures return zero items silently.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-041, J-044, J-053
- **Aliases:** WKB-037, GWP-014
- **Evidence:** worker/src/researcher/providers/rss.ts:3-12,81-94; packages/researcher/src/providers/rss.ts:3-12
- **Repro:** static.
- **Fix hint:** Decode entities then strip tags, detect Atom by root element, prefer rel=alternate, warn when 0 items.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Decode entities then strip tags, detect Atom by root element, prefer rel=alternate, warn when 0 items.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-117). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/researcher/providers/rss.ts:3-12,81-94.
