---
id: 2026-10-27-cons-035-passage-clipping-from-stream-selectionclipper-in
title: Passage clipping from stream (SelectionClipper in card)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-frz-003-passage-clipping-from-the-stream-card
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/clips
raw_id: CONS-035
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Passage clipping from stream (SelectionClipper in card).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C03-7
- **Alias:** C03-7
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** grep: SelectionClipper only used in ArticleDetailView.tsx:11,150 (cons doc says toast was added; toast exists (SelectionClipper.tsx:19-23) but card wiring absent)
- **Covered by:** FZ-003

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-035). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: real gap, frozen as FRZ-003 (see findings/FROZEN.md); cons doc says toast was added; toast exists (SelectionClipper.tsx:19-23) but card wiring absent
