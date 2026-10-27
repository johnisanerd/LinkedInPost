---
id: 2026-10-27-inv-001-do-feed-and-clip-rest-calls
title: Do feed and clip REST calls fail because VITE_WORKER_URL is unset? (FEB-002 vs FEA-027)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-027-feed-and-clip-requests-build-their
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P1
area: frontend/feed
raw_id: INV-001
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Do feed and clip REST calls fail because VITE_WORKER_URL is unset? (FEB-002 vs FEA-027). If FEB-002 holds, clipping an article does nothing visible on a deployed Pages site and clips never persist (FeedPage swallows the error). If FEA-027 were right the fix would be on the worker side instead.

## Evidence and reproduction

- **Question:** FEB-002 says getFeed, createFeedItem, getClipsPage and createClipPage read globalThis.VITE_WORKER_URL, which is never set, so they hit the frontend host. FEA-027 says /api/clips is not routed by the worker. Which is right?
- **Why it matters:** If FEB-002 holds, clipping an article does nothing visible on a deployed Pages site and clips never persist (FeedPage swallows the error). If FEA-027 were right the fix would be on the worker side instead.
- **How to settle it:** Run on a Pages build: open /feed, click Clip, check the network tab for the request host (expect the Pages host, 404). Also run `cd frontend && grep -rn "globalThis" src vite.config.ts` and confirm nothing assigns VITE_WORKER_URL. Fix test: use this.endpointUrl in backendApi.ts:827,844,867,884 then re-click Clip.
- **Related items:** LR-027, FEB-002, FEA-027
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code says FEB-002 is right and FEA-027 is half wrong. Worker routes /api/clips GET/POST and /api/feed/items POST exist (worker/src/index.ts:714-717 and 804-807). backendApi.ts:827,844,867,884 read globalThis.VITE_WORKER_URL; grep over frontend/src and frontend/vite.config.ts finds no assignment outside backendApi.ts, and vite.config.ts has no proxy block. FEA-027's other claim holds: /v1/variants/save and /v1/clips are not routed (worker/src/index.ts only routes /v1/image-gen-catalog under /v1/). Item kept: not run live. Covered by LR-027..
