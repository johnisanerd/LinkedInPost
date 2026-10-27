---
id: 2026-10-27-inv-013-does-generate-and-save-return-null
title: Does Generate-and-save return null because the card is built inside a setState updater? (FEA-029)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-168-generate-and-save-workflow-may-never
docs:
- frontend/src/features/review/context/useReviewFlowActions.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: investigation
severity: P3
area: frontend/editor
raw_id: INV-013
source_file: docs/launch-readiness/findings/INVESTIGATE.md
---

## Problem

Does Generate-and-save return null because the card is built inside a setState updater? (FEA-029). If not, the workflow is never saved and the user sees no error.

## Evidence and reproduction

- **Question:** newCard is assigned inside the setGeneratedCards updater and returned immediately. Is the updater run before the return?
- **Why it matters:** If not, the workflow is never saved and the user sees no error.
- **How to settle it:** Read frontend/src/features/review/context/useReviewFlowActions.ts:344-357. To settle: Styles tab, pick a card, click Generate and save, check whether a custom workflow appears.
- **Related items:** LR-168
- **Owner:**

## Acceptance criteria

- The question in the title is answered in Attempts with file:line evidence and a clear yes/no.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/INVESTIGATE.md (INV-013). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: code has the pattern at useReviewFlowActions.ts:344-357 (newCard assigned in the updater, then returned). Whether React runs it in time was not tested. Covered by LR-168..
