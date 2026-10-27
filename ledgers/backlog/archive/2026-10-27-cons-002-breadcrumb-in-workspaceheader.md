---
id: 2026-10-27-cons-002-breadcrumb-in-workspaceheader
title: Breadcrumb in WorkspaceHeader
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
raw_id: CONS-002
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
resolution: superseded
---

## Problem

Breadcrumb in WorkspaceHeader.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C01-2
- **Alias:** C01-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** components/workspace/WorkspaceHeader.tsx:47; WorkspaceChromeContext.tsx:19 (only on topic-review routes via headerOverride, not derived from location)
- **Covered by:** FZ-001

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-002). Static reading only; nothing executed. Closed as superseded.

## Verification

Frozen: needs a capability outside this release. The in-scope alternative and the frozen capability are recorded in the linked idea record.

Evidence: read-only: partial; real gap, frozen as FRZ-001 (see findings/FROZEN.md); only on topic-review routes via headerOverride, not derived from location
