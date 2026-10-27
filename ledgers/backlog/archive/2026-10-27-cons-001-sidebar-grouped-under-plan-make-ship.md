---
id: 2026-10-27-cons-001-sidebar-grouped-under-plan-make-ship
title: Sidebar grouped under Plan/Make/Ship/Configure/Admin
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
severity: P1
area: frontend/navigation
raw_id: CONS-001
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Sidebar grouped under Plan/Make/Ship/Configure/Admin.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C01-1
- **Alias:** C01-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** components/workspace/AppSidebar.tsx (flat link() list, admin gating inline ~L269) (no group headers)
- **Covered by:** FZ-001

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-001). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: real gap, frozen as FRZ-001 (see findings/FROZEN.md); no group headers
