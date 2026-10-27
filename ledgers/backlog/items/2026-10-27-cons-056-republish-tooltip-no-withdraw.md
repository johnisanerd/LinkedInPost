---
id: 2026-10-27-cons-056-republish-tooltip-no-withdraw
title: Republish tooltip; no withdraw
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-178-queue-and-addtopic-polish-no-required
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: ux-gap
severity: P2
area: frontend/queue
raw_id: CONS-056
source_file: docs/launch-readiness/findings/EXISTING-REVIEWS.md
---

## Problem

Republish tooltip; no withdraw.

## Evidence and reproduction

- **Source:** launch-release/findings/raw/existing-reviews.md section 1, row C04-17
- **Alias:** C04-17
- **Original tag:** MED (mapped to P2)
- **Current status:** partial
- **Evidence:** DashboardQueue.tsx:925 title="Republish to channel" (tooltip does not say "creates new draft"; no withdraw)
- **Covered by:** LR-178

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/EXISTING-REVIEWS.md (CONS-056). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: partial; still open in code (tooltip does not say "creates new draft"; no withdraw); covered by LR-178.
