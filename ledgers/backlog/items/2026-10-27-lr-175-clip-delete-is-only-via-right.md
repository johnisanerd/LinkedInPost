---
id: 2026-10-27-lr-175-clip-delete-is-only-via-right
title: Clip delete is only via right-click or hover buttons and a drop gives no success toast
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j044-clip-an-article-or-a-passage
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/feed
raw_id: LR-175
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Clip delete is only via right-click or hover buttons and a drop gives no success toast.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-044
- **Aliases:** C03-1, C03-2
- **Evidence:** frontend/src/features/feed/components/ClipsDock.tsx:206,332-367
- **Repro:** (static check) Open frontend/src/features/feed/components/ClipsDock.tsx:206,332-367 and confirm the behaviour described in the summary; then exercise the matching journey (J-044) to observe it.
- **Fix hint:** Add a visible delete control and a drop confirmation.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a visible delete control and a drop confirmation.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-175). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/ClipsDock.tsx:206,332-367.
