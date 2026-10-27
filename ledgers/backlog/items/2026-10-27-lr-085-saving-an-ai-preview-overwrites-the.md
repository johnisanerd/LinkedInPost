---
id: 2026-10-27-lr-085-saving-an-ai-preview-overwrites-the
title: Saving an AI preview overwrites the matching sheet slot without confirmation and rapid saves clobber each other
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j063-open-generated-variants-and-pick-one
- 2026-10-27-j066-variants-preview-for-a-selection
related: []
docs:
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
raw_id: LR-085
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Saving an AI preview overwrites the matching sheet slot without confirmation and rapid saves clobber each other.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-063, J-066
- **Aliases:** FEA-016
- **Evidence:** frontend/src/features/review/context/useReviewFlowActions.ts:416-460
- **Repro:** Generate 4 variants, click Save on preview 1 and, before "Saved" appears, on preview 2; reload: only one slot holds the preview.
- **Fix hint:** Serialize saves, merge from the latest sheetRow and confirm before overwriting a non-empty slot.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Serialize saves, merge from the latest sheetRow and confirm before overwriting a non-empty slot.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-085). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowActions.ts:416-460.
