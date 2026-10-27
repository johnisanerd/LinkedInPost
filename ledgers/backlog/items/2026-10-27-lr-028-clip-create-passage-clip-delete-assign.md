---
id: 2026-10-27-lr-028-clip-create-passage-clip-delete-assign
title: Clip create, passage clip, delete, assign, group edits, refresh and votes fail silently and optimistic state is not rolled back.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j042-refresh-the-feed-on-demand
- 2026-10-27-j043-interest-groups-create-edit-delete
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j045-attach-clips-to-a-draft-and
- 2026-10-27-j049-thumbs-up-down-on-an-article
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
area: frontend/feed
raw_id: LR-028
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Clip create, passage clip, delete, assign, group edits, refresh and votes fail silently and optimistic state is not rolled back.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-042..J-045, J-049
- **Aliases:** FEA-010, FEB-019
- **Evidence:** frontend/src/features/feed/FeedPage.tsx:184-233,280-296; frontend/src/features/feed/components/ClipsDock.tsx:66-76
- **Repro:** Block the worker (or use an expired token) and clip an article: no message. Delete a clip while offline: gone until reload.
- **Fix hint:** Surface an error notice in each catch, roll back optimistic state, route auth expiry to onAuthExpired.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Surface an error notice in each catch, roll back optimistic state, route auth expiry to onAuthExpired.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-028). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/FeedPage.tsx:184-233,280-296.
