---
id: 2026-10-27-cons-030-drop-zone-affordance-toast
title: Drop-zone affordance + toast
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
raw_id: CONS-030
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Drop-zone affordance + toast.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-2
- **Alias:** C03-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** ClipsDock.tsx:332-367 (dragOver highlight "Drop to assign") (no success toast on drop)
- **Covered by:** LR-175

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-030). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (no success toast on drop); covered by LR-175.
