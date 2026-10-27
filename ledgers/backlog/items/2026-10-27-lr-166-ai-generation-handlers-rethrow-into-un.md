---
id: 2026-10-27-lr-166-ai-generation-handlers-rethrow-into-un
title: AI generation handlers rethrow into un-awaited click handlers, causing unhandled promise rejections
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j066-variants-preview-for-a-selection
- 2026-10-27-j069-content-review-checklist-before-publishing
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
severity: P3
area: frontend/editor
raw_id: LR-166
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

AI generation handlers rethrow into un-awaited click handlers, causing unhandled promise rejections.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-052, J-065, J-066, J-069
- **Aliases:** FEA-026
- **Evidence:** frontend/src/features/review/context/useReviewFlowActions.ts:229-274
- **Repro:** Break the LLM key and click Quick Change: console shows an unhandled rejection in addition to the notice.
- **Fix hint:** Catch at the call site since the wrapper already notified the user.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Catch at the call site since the wrapper already notified the user.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-166). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/context/useReviewFlowActions.ts:229-274.
