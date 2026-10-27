---
id: 2026-10-27-ac-017-modularity-no-oversized-component
title: Modularity (no oversized component)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-179-settings-is-a-2251-line-single
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: acceptance-gap
severity: P2
area: frontend/code-health
raw_id: AC-017
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Modularity (no oversized component).

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 5, row DE-5
- **Alias:** DE-5
- **Original tag:** EGW (no severity given, defaulted to P2)
- **Current status:** open
- **Evidence:** DashboardSettingsDrawer.tsx 2251 lines; FeedPage.tsx 1490; EditorSidebar large
- **Covered by:** LR-179

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (AC-017). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (DashboardSettingsDrawer.tsx 2251 lines; FeedPage.tsx 1490; EditorSidebar large); covered by LR-179.
