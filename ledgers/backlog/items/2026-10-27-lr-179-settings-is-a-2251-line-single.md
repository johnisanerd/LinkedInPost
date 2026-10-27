---
id: 2026-10-27-lr-179-settings-is-a-2251-line-single
title: Settings is a 2251-line single component with no URL subpaths or section descriptions, and save and validators are admin-only or missing.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j120-admin-settings-default-channel-allowed-models
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
area: frontend/settings
raw_id: LR-179
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Settings is a 2251-line single component with no URL subpaths or section descriptions, and save and validators are admin-only or missing.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-120
- **Aliases:** C09-1, C09-2, C09-4, C09-5, C09-13, C09-14, DE-5
- **Evidence:** frontend/src/components/dashboard/DashboardSettingsDrawer.tsx:1235-1256,1282
- **Repro:** (static check) Open frontend/src/components/dashboard/DashboardSettingsDrawer.tsx:1235-1256,1282 and confirm the behaviour described in the summary; then exercise the matching journey (J-120) to observe it.
- **Fix hint:** Defer the split; add one-line section descriptions and validators for Telegram id and similar fields.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Defer the split; add one-line section descriptions and validators for Telegram id and similar fields.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-179). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/DashboardSettingsDrawer.tsx:1235-1256,1282.
