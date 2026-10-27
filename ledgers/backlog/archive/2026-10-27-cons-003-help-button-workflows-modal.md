---
id: 2026-10-27-cons-003-help-button-workflows-modal
title: '? help button / workflows modal'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-frz-001-sidebar-grouping-breadcrumbs-from-location-sidebar
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/navigation
raw_id: CONS-003
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

? help button / workflows modal.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C01-3
- **Alias:** C01-3
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** App.tsx:125-134, components/HelpOverlay.tsx:4-9 (? key opens shortcuts overlay; no visible header button, no workflows content)
- **Covered by:** FZ-001

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-003). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-001 (see findings/FROZEN.md); ? key opens shortcuts overlay; no visible header button, no workflows content
