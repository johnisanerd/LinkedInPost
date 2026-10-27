---
id: 2026-10-27-cons-105-unsaved-changes-guard
title: Unsaved-changes guard
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
raw_id: CONS-105
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Unsaved-changes guard.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C09-4
- **Alias:** C09-4
- **Original tag:** HIGH (mapped to P1)
- **Current status:** partial
- **Evidence:** DashboardSettingsDrawer.tsx:1235-1244 beforeunload; :1247-1256 saved toast (no in-app route-change guard; save only for admin (:1282))
- **Covered by:** LR-179

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-105). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (no in-app route-change guard; save only for admin (:1282)); covered by LR-179.
