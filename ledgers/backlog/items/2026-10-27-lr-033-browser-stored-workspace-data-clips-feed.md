---
id: 2026-10-27-lr-033-browser-stored-workspace-data-clips-feed
title: Browser-stored workspace data (clips, feed cache, draft autosave) is not scoped to the user or cleared on sign-out, leaking across accounts.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j026-sign-out
- 2026-10-27-j041-open-the-feed-cache-first-auto
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
- 2026-10-27-j142-per-user-lists-are-scoped-clips
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: frontend/shell
raw_id: LR-033
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Browser-stored workspace data (clips, feed cache, draft autosave) is not scoped to the user or cleared on sign-out, leaking across accounts.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-026, J-041, J-044, J-140, J-142
- **Aliases:** FEA-009, FEB-018
- **Evidence:** frontend/src/features/feed/FeedPage.tsx:168-173,308-312; frontend/src/App.tsx:359,375
- **Repro:** Sign in as user A, clip two articles and start a topic, sign out, sign in as user B (no clips): B sees A's clips in the dock and A's topic text in Add Topic.
- **Fix hint:** Clear these keys and the feed store on sign-out and email change, prefix keys with a user hash, always replace local clips with the server response.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Clear these keys and the feed store on sign-out and email change, prefix keys with a user hash, always replace local clips with the server response.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-033). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/FeedPage.tsx:168-173,308-312.
