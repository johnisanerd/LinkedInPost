---
id: 2026-10-27-cons-009-global-command-palette-cmd-k
title: Global command palette (cmd+k)
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
raw_id: CONS-009
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Global command palette (cmd+k).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-9
- **Alias:** C01-9
- **Original tag:** MED (mapped to P2)
- **Current status:** open
- **Evidence:** grep CommandPalette: none (Cmd-K only focuses settings nav search (DashboardSettingsDrawer.tsx:1225))
- **Covered by:** FZ-001

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-009). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: real gap, frozen as FRZ-001 (see findings/FROZEN.md); Cmd-K only focuses settings nav search (DashboardSettingsDrawer.tsx:1225)
