---
id: 2026-10-27-cons-102-settings-settings-page-w-left-nav
title: Settings -> /settings page w/ left nav
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
type: ux-gap
severity: P1
area: frontend/settings
raw_id: CONS-102
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Settings -> /settings page w/ left nav.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C09-1
- **Alias:** C09-1
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardSettingsDrawer.tsx (2251 lines; left nav + grouped list ~L1285-1390; /settings route exists) (still a monolith component; not split per section)
- **Covered by:** LR-179

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-102). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (still a monolith component; not split per section); covered by LR-179.
