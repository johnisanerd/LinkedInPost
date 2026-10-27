---
id: 2026-10-27-lr-184-the-videos-live-panel-polls-http
title: The videos live panel polls http://127.0.0.1:8765 from the deployed HTTPS app
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j146-videos-page
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
area: frontend/videos
raw_id: LR-184
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The videos live panel polls http://127.0.0.1:8765 from the deployed HTTPS app.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-146
- **Aliases:** FEB-027
- **Evidence:** frontend/src/features/videos/LiveRunsPanel.tsx:6
- **Repro:** enable flag on a deployed build.
- **Fix hint:** Keep the flag off for release or hide the panel unless VITE_PIPELINE_LIVE_URL is set.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Keep the flag off for release or hide the panel unless VITE_PIPELINE_LIVE_URL is set.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-184). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/videos/LiveRunsPanel.tsx:6.
