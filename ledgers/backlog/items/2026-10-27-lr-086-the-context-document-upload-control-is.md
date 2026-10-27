---
id: 2026-10-27-lr-086-the-context-document-upload-control-is
title: The context-document upload control is not wired through TopicEditorPage, so the upload silently does nothing
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j070-context-document-upload-txt-md-pdf
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
raw_id: LR-086
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The context-document upload control is not wired through TopicEditorPage, so the upload silently does nothing.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-070
- **Aliases:** FEA-017
- **Evidence:** frontend/src/features/topic-navigation/screens/TopicEditorPage.tsx; frontend/src/features/review/context/useReviewFlowActions.ts:1038-1065
- **Repro:** Editor > Refine panel > "Context documents" > upload a .txt: nothing is listed.
- **Fix hint:** Add the prop to TopicReviewPagesBaseProps, pass it through, and show an error when the handler is missing.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add the prop to TopicReviewPagesBaseProps, pass it through, and show an error when the handler is missing.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-086). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/topic-navigation/screens/TopicEditorPage.tsx.
