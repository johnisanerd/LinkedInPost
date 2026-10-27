---
id: 2026-10-27-cons-029-clipsdock-visible-trash-not-right-click
title: ClipsDock visible trash (not right-click)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-175-clip-delete-is-only-via-right
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/clips
raw_id: CONS-029
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

ClipsDock visible trash (not right-click).

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C03-1
- **Alias:** C03-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** features/feed/components/ClipsDock.tsx:206 onContextMenu confirm; hover-only Edit/Delete :~236 (delete still via right-click or hover buttons)
- **Covered by:** LR-175

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-029). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (delete still via right-click or hover buttons); covered by LR-175.
