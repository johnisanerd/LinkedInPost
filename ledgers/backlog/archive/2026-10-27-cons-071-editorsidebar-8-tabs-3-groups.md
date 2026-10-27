---
id: 2026-10-27-cons-071-editorsidebar-8-tabs-3-groups
title: EditorSidebar 8 tabs -> 3 groups
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-frz-008-editor-layout-redesign-3-tab-groups
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/editor
raw_id: CONS-071
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

EditorSidebar 8 tabs -> 3 groups.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C06-1
- **Alias:** C06-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** features/review-editor/components/EditorSidebar.tsx:91-98 (now 5 base tabs (+Email) not 3 groups)
- **Covered by:** FZ-008

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-071). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-008 (see findings/FROZEN.md); now 5 base tabs (+Email) not 3 groups
