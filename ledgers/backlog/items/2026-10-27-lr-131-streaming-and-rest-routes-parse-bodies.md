---
id: 2026-10-27-lr-131-streaming-and-rest-routes-parse-bodies
title: Streaming and REST routes parse bodies and load config outside any try/catch, so failures return a 500 page without CORS headers that browsers hide.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j050-rest-feed-and-clip-endpoints-require
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j054-network-drop-in-the-middle-of
- 2026-10-27-j065-quick-change-via-sse
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/api
raw_id: LR-131
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Streaming and REST routes parse bodies and load config outside any try/catch, so failures return a 500 page without CORS headers that browsers hide.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-044, J-050, J-053, J-054, J-065
- **Aliases:** WKA-021
- **Evidence:** worker/src/index.ts:854,1009-1011,6500,6600
- **Repro:** static. Executor: POST `/api/quickchange/stream` as a no-sheet user.
- **Fix hint:** Wrap the whole fetch handler in one try/catch that always builds CORS headers.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wrap the whole fetch handler in one try/catch that always builds CORS headers.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-131). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:854,1009-1011,6500,6600.
