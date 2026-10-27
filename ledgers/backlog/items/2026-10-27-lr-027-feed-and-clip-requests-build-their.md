---
id: 2026-10-27-lr-027-feed-and-clip-requests-build-their
title: Feed and clip requests build their URL from a never-set global, so they hit the Pages host and return 404 while the UI hides the error.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j045-attach-clips-to-a-draft-and
- 2026-10-27-j050-rest-feed-and-clip-endpoints-require
related: []
docs:
- frontend/src/services/backendApi.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/feed
raw_id: LR-027
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Feed and clip requests build their URL from a never-set global, so they hit the Pages host and return 404 while the UI hides the error.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-044, J-045, J-050
- **Aliases:** FEB-002, FEA-027, FEB-025
- **Evidence:** frontend/src/services/backendApi.ts:827,844,867,884; frontend/src/features/feed/FeedPage.tsx:283,308
- **Repro:** deploy to GitHub Pages, open /feed, click Clip on an article, watch network: request goes to `https://<user>.github.io/api/clips` (404). Static reasoning.
- **Fix hint:** Use this.endpointUrl in all call sites, delete the dead variants/save KV code and the window.__idToken read, and surface errors in FeedPage.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use this.endpointUrl in all call sites, delete the dead variants/save KV code and the window.__idToken read, and surface errors in FeedPage.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-027). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/services/backendApi.ts:827,844,867,884.
