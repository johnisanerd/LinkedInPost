---
id: 2026-10-27-cons-073-three-discard-dialogs-differentiated
title: Three discard dialogs differentiated
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-089-the-editor-has-no-beforeunload-guard
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/editor
raw_id: CONS-073
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Three discard dialogs differentiated.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-3
- **Alias:** C06-3
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/review/components/ReviewDialogs.tsx:60,95,110 all "Discard current editor changes?"
- **Covered by:** LR-089

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-073). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (features/review/components/ReviewDialogs.tsx:60,95,110 all "Discard current editor changes?"); covered by LR-089.
