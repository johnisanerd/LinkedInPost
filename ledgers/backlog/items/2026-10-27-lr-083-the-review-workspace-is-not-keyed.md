---
id: 2026-10-27-lr-083-the-review-workspace-is-not-keyed
title: The review workspace is not keyed by topic, so late AI, image or save responses land on whichever topic is currently open.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j063-open-generated-variants-and-pick-one
- 2026-10-27-j064-manual-edit-with-undo-redo-draft
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j066-variants-preview-for-a-selection
- 2026-10-27-j067-pick-and-upload-images-for-a
- 2026-10-27-j091-republish-an-already-published-post
related: []
docs:
- frontend/src/features/review/context/useReviewFlowActions.ts
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
raw_id: LR-083
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The review workspace is not keyed by topic, so late AI, image or save responses land on whichever topic is currently open.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-063..J-067, J-091
- **Aliases:** FEA-013, FEA-014
- **Evidence:** frontend/src/features/review/context/useReviewFlowActions.ts:229-274; frontend/src/features/review/context/useReviewFlowState.ts:376-397
- **Repro:** Start Quick Change on topic A (slow LLM), use browser back/forward to topic B before it returns.
- **Fix hint:** Put key={row.topicId} on ReviewWorkspace (or ReviewFlowProvider) and include topicId in initKey.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Put key={row.topicId} on ReviewWorkspace (or ReviewFlowProvider) and include topicId in initKey.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-083). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowActions.ts:229-274.
