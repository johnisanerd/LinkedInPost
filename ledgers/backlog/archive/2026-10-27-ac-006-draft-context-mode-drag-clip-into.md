---
id: 2026-10-27-ac-006-draft-context-mode-drag-clip-into
title: 'Draft Context Mode: drag clip into editor as context block'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-frz-003-passage-clipping-from-the-stream-card
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: acceptance-gap
severity: P2
area: frontend/clips
raw_id: AC-006
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Draft Context Mode: drag clip into editor as context block.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 5, row D3-6
- **Alias:** D3-6
- **Original tag:** spec (no severity given, defaulted to P2)
- **Current status:** partial
- **Evidence:** DraftContextView.tsx:259-266 ("Generate Post in Editor"), :571 unassign (drag-into-editor insertion not found)
- **Covered by:** FZ-003

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (AC-006). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-003 (see findings/FROZEN.md); drag-into-editor insertion not found
