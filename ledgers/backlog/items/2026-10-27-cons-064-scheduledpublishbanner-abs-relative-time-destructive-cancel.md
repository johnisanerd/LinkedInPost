---
id: 2026-10-27-cons-064-scheduledpublishbanner-abs-relative-time-destructive-cancel
title: ScheduledPublishBanner abs+relative time, destructive Cancel
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-169-the-footer-button-says-publish-even
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/schedule
raw_id: CONS-064
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

ScheduledPublishBanner abs+relative time, destructive Cancel.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C05-7
- **Alias:** C05-7
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** scheduled-publish/ScheduledPublishBanner.tsx:42-44 ("Cancel schedule") (no countdown)
- **Covered by:** LR-169

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-064). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (no countdown); covered by LR-169.
