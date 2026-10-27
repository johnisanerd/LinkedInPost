---
id: 2026-10-27-lr-165-bulk-campaign-schedule-and-channel-are
title: Bulk campaign schedule and channel are still modal dialogs and no template gallery or JSON diff exists
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j106-bulk-import-by-pasting-campaign-json
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
area: frontend/campaign
raw_id: LR-165
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Bulk campaign schedule and channel are still modal dialogs and no template gallery or JSON diff exists.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-106
- **Aliases:** C05c, C05e
- **Evidence:** frontend/src/features/campaign/CampaignPage.tsx:305-308,379-420
- **Repro:** (static check) Open frontend/src/features/campaign/CampaignPage.tsx:305-308,379-420 and confirm the behaviour described in the summary; then exercise the matching journey (J-106) to observe it.
- **Fix hint:** Defer; low value for release.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Defer; low value for release.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-165). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/campaign/CampaignPage.tsx:305-308,379-420.
