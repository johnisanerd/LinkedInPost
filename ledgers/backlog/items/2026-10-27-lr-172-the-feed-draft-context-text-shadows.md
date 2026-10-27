---
id: 2026-10-27-lr-172-the-feed-draft-context-text-shadows
title: The feed draft-context text shadows the real draft via a localStorage copy
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j045-attach-clips-to-a-draft-and
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
raw_id: LR-172
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The feed draft-context text shadows the real draft via a localStorage copy.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-045
- **Aliases:** FEA-031
- **Evidence:** frontend/src/features/feed/components/DraftContextView.tsx:66-85
- **Repro:** Open a draft in feed, change text, edit the post in the editor, reopen in feed: old text.
- **Fix hint:** Prefer the row text unless the local copy is newer, or drop the shadow copy.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Prefer the row text unless the local copy is newer, or drop the shadow copy.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-172). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/components/DraftContextView.tsx:66-85.
