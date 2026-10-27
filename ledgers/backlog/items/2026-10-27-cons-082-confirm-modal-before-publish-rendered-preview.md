---
id: 2026-10-27-cons-082-confirm-modal-before-publish-rendered-preview
title: Confirm modal before publish (rendered preview+channel+time)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-026-the-editor-footer-publish-posts-immediately
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/publish
raw_id: CONS-082
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Confirm modal before publish (rendered preview+channel+time).

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C07-1
- **Alias:** C07-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:163,852,896,1274 (queue has publishConfirmRow) (editor footer "Publish to X" calls handlePublishNow directly (EditorScreen.tsx:~393; useReviewFlowActions.ts:~700) - no confirm)
- **Covered by:** LR-026

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-082). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (editor footer "Publish to X" calls handlePublishNow directly (EditorScreen.tsx:~393; useReviewFlowActions.ts:~700) - no confirm); covered by LR-026.
