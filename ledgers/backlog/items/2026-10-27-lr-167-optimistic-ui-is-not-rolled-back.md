---
id: 2026-10-27-lr-167-optimistic-ui-is-not-rolled-back
title: Optimistic UI is not rolled back on failure for votes, persona delete and custom workflows
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j035-add-a-topic-from-the-scratchpad
- 2026-10-27-j049-thumbs-up-down-on-an-article
- 2026-10-27-j061-custom-workflows-post-types
related: []
docs:
- frontend/src/features/workflows/useCustomWorkflows.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P3
area: frontend/editor
raw_id: LR-167
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Optimistic UI is not rolled back on failure for votes, persona delete and custom workflows.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-035, J-049, J-061
- **Aliases:** FEA-028
- **Evidence:** frontend/src/features/feed/FeedPage.tsx:260-278; frontend/src/features/workflows/useCustomWorkflows.ts:44-76
- **Repro:** Fail the call and click thumbs up: stays highlighted.
- **Fix hint:** Revert state and show a notice in each catch.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Revert state and show a notice in each catch.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-167). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/features/feed/FeedPage.tsx:260-278.
