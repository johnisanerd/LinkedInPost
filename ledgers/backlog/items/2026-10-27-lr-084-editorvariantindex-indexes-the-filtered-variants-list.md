---
id: 2026-10-27-lr-084-editorvariantindex-indexes-the-filtered-variants-list
title: editorVariantIndex indexes the filtered variants list but is used as the sheet column slot, so Save draft writes into the wrong column.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j063-open-generated-variants-and-pick-one
- 2026-10-27-j064-manual-edit-with-undo-redo-draft
related: []
docs:
- frontend/src/features/review/context/useReviewFlowState.ts
- frontend/src/features/review/context/useReviewFlowActions.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/editor
raw_id: LR-084
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

editorVariantIndex indexes the filtered variants list but is used as the sheet column slot, so Save draft writes into the wrong column.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-063, J-064
- **Aliases:** FEA-015
- **Evidence:** frontend/src/features/review/context/useReviewFlowState.ts:241,264-268; frontend/src/features/review/context/useReviewFlowActions.ts:732-738
- **Repro:** Row with variant1, variant3 and variant4 filled; open `/editor/2`, edit, "Save draft": variant2 gets the text, variant3 unchanged.
- **Fix hint:** Store variant.originalIndex in state and refuse to save when it is unknown.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Store variant.originalIndex in state and refuse to save when it is unknown.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-084). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowState.ts:241,264-268.
