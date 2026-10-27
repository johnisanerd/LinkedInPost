---
id: 2026-10-27-lr-003-when-the-rule-filter-drops-every
title: When the rule filter drops every variant the unfiltered ones are returned, and a review block verdict is stored as completed.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j063-open-generated-variants-and-pick-one
- 2026-10-27-j065-quick-change-via-sse
related: []
docs:
- generation-worker/src/modules/_shared/selector.ts
- generation-worker/src/players/review.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: generation-worker
raw_id: LR-003
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

When the rule filter drops every variant the unfiltered ones are returned, and a review block verdict is stored as completed.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-063, J-065
- **Aliases:** GWP-006
- **Evidence:** generation-worker/src/modules/_shared/selector.ts:170-178; generation-worker/src/players/review.ts:45-53
- **Repro:** static. Generate with mustAvoid containing a word the model always uses; observe variants contain it and the response is HTTP 200.
- **Fix hint:** On an empty filter result retry the creator once then return an error or flag every variant; surface review verdict block as status blocked and make the main worker withhold it.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

On an empty filter result retry the creator once then return an error or flag every variant; surface review verdict block as status blocked and make the main worker withhold it.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-003). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/modules/_shared/selector.ts:170-178.
