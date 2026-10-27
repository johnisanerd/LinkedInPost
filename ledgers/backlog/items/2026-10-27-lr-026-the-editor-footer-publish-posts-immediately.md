---
id: 2026-10-27-lr-026-the-editor-footer-publish-posts-immediately
title: The editor footer Publish posts immediately with no confirmation, and Approve and Publish are separate buttons, so one click posts live.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j088-double-click-on-publish
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
severity: P1
area: frontend/editor
raw_id: LR-026
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The editor footer Publish posts immediately with no confirmation, and Approve and Publish are separate buttons, so one click posts live.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076, J-088
- **Aliases:** C07-1, C07-4, C07-6
- **Evidence:** frontend/src/features/review-editor/screens/EditorScreen.tsx:340-430; frontend/src/features/review/context/useReviewFlowActions.ts:700
- **Repro:** (static check) Open frontend/src/features/review-editor/screens/EditorScreen.tsx:340-430 and confirm the behaviour described in the summary; then exercise the matching journey (J-076, J-088) to observe it.
- **Fix hint:** Add a confirm step (channel, time, rendered preview) before handlePublishNow in the editor, reusing the queue publishConfirmRow pattern.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a confirm step (channel, time, rendered preview) before handlePublishNow in the editor, reusing the queue publishConfirmRow pattern.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-026). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review-editor/screens/EditorScreen.tsx:340-430.
