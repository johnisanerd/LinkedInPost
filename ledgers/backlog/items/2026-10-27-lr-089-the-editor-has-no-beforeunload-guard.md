---
id: 2026-10-27-lr-089-the-editor-has-no-beforeunload-guard
title: The editor has no beforeunload guard for unsaved edits, and the three discard dialogs all use identical copy
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j064-manual-edit-with-undo-redo-draft
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/editor
raw_id: LR-089
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The editor has no beforeunload guard for unsaved edits, and the three discard dialogs all use identical copy.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-064
- **Aliases:** C06-5, C06-3
- **Evidence:** frontend/src/features/review/components/ReviewDialogs.tsx:60,95,110
- **Repro:** (static check) Open frontend/src/features/review/components/ReviewDialogs.tsx:60,95,110 and confirm the behaviour described in the summary; then exercise the matching journey (J-064) to observe it.
- **Fix hint:** Add a beforeunload guard while the editor is dirty and differentiate the dialog copy.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add a beforeunload guard while the editor is dirty and differentiate the dialog copy.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-089). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review/components/ReviewDialogs.tsx:60,95,110.
