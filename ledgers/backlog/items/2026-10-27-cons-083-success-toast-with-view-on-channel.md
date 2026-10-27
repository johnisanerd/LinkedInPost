---
id: 2026-10-27-cons-083-success-toast-with-view-on-channel
title: Success toast with "View on channel" permalink
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-088-there-is-no-permalink-or-view
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/publish
raw_id: CONS-083
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Success toast with "View on channel" permalink.

## Evidence and reproduction

- **Source:** docs/launch-readiness/findings/raw/existing-reviews.md section 1, row C07-2
- **Alias:** C07-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** useDashboardQueue.ts:587 modal showAlert 'Success'; grep permalink: none for publish (USE-CASES claims link; not present)
- **Covered by:** LR-088

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-083). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (USE-CASES claims link; not present); covered by LR-088.
