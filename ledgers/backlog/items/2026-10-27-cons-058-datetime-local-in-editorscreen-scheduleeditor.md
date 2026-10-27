---
id: 2026-10-27-cons-058-datetime-local-in-editorscreen-scheduleeditor
title: datetime-local in EditorScreen -> ScheduleEditor
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-169-the-footer-button-says-publish-even
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/schedule
raw_id: CONS-058
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

datetime-local in EditorScreen -> ScheduleEditor.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C05-1
- **Alias:** C05-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** features/review-editor/screens/EditorScreen.tsx:310 (editor still has bare input)
- **Covered by:** LR-169

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-058). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (editor still has bare input); covered by LR-169.
