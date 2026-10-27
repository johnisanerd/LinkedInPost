---
id: 2026-10-27-cons-041-per-row-channel-pill
title: Per-row channel pill
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-097-the-queue-row-has-no-channel
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P1
area: frontend/queue
raw_id: CONS-041
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Per-row channel pill.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-2
- **Alias:** C04-2
- **Original tag:** HIGH (mapped to P1)
- **Current status:** open
- **Evidence:** DashboardQueue.tsx (only StatusPill at :768; CHANNEL_OPTIONS used only in bulk/confirm :1017,1274) (onboarding Tour copy at :435 claims "channel pill shows where a post will publish" - it does not)
- **Covered by:** LR-097

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-041). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: still open in code (onboarding Tour copy at :435 claims "channel pill shows where a post will publish" - it does not); covered by LR-097.
