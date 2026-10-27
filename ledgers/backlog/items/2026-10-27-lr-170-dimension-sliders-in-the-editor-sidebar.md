---
id: 2026-10-27-lr-170-dimension-sliders-in-the-editor-sidebar
title: Dimension sliders in the editor sidebar have no explanatory tooltips
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j066-variants-preview-for-a-selection
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/editor
raw_id: LR-170
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Dimension sliders in the editor sidebar have no explanatory tooltips.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-066
- **Aliases:** C06-2
- **Evidence:** frontend/src/features/review-editor/components/EditorSidebar.tsx:25-35,360-400
- **Repro:** (static check) Open frontend/src/features/review-editor/components/EditorSidebar.tsx:25-35,360-400 and confirm the behaviour described in the summary; then exercise the matching journey (J-066) to observe it.
- **Fix hint:** Add short tooltips.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Add short tooltips.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-170). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/review-editor/components/EditorSidebar.tsx:25-35,360-400.
