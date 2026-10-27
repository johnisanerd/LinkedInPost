---
id: 2026-10-27-lr-024-auto-saved-editor-drafts-are-never
title: Auto-saved editor drafts are never offered for recovery on the editor route because draftRecoveryPending is hard-coded to false there.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j021-google-id-token-expires-mid-session
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
severity: P1
area: frontend/editor
raw_id: LR-024
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Auto-saved editor drafts are never offered for recovery on the editor route because draftRecoveryPending is hard-coded to false there.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-021, J-064
- **Aliases:** FEA-006
- **Evidence:** frontend/src/features/review/context/useReviewFlowState.ts:258,273-282,615-679
- **Repro:** Open `/topics/<id>/editor/0`, type 300 words, wait 3 s (autosave), close the tab, reopen the same URL: original sheet text, no restore prompt.
- **Fix hint:** Arm draftRecoveryPending for the editor screen too and show the prompt before applying.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Arm draftRecoveryPending for the editor screen too and show the prompt before applying.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-024). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowState.ts:258,273-282,615-679.
