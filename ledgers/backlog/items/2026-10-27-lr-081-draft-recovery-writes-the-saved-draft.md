---
id: 2026-10-27-lr-081-draft-recovery-writes-the-saved-draft
title: Draft recovery writes the saved draft into the editor before the user answers, and Start fresh does not revert
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j064-manual-edit-with-undo-redo-draft
related: []
docs:
- frontend/src/features/review/context/useReviewFlowState.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/editor
raw_id: LR-081
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Draft recovery writes the saved draft into the editor before the user answers, and Start fresh does not revert.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-064
- **Aliases:** FEA-007
- **Evidence:** frontend/src/features/review/context/useReviewFlowState.ts:682-690; frontend/src/features/review/components/ReviewDialogs.tsx:36-52
- **Repro:** (static reasoning) Reach variants screen with a differing autosave, click "Start fresh": editor text is still the stale draft.
- **Fix hint:** Move the restore into the dialog confirm handler and leave state untouched on cancel.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Move the restore into the dialog confirm handler and leave state untouched on cancel.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-081). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowState.ts:682-690.
