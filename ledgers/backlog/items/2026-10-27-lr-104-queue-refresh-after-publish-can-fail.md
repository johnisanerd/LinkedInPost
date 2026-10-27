---
id: 2026-10-27-lr-104-queue-refresh-after-publish-can-fail
title: Queue refresh after publish can fail silently and loads are unordered, so a live post can still show as Approved and be published again.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
- 2026-10-27-j088-double-click-on-publish
- 2026-10-27-j089-post-is-live-but-marking-it
- 2026-10-27-j091-republish-an-already-published-post
related: []
docs:
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-104
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Queue refresh after publish can fail silently and loads are unordered, so a live post can still show as Approved and be published again.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-040, J-088, J-089, J-091
- **Aliases:** FEA-024
- **Evidence:** frontend/src/components/dashboard/hooks/useDashboardQueue.ts:106-125,572-587,716-731
- **Repro:** (static reasoning) Make `getRows` fail once after a successful publish; the row stays Approved.
- **Fix hint:** Mark the row published locally and show a published-refresh-failed notice; add a request counter to loadData.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Mark the row published locally and show a published-refresh-failed notice; add a request counter to loadData.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-104). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/components/dashboard/hooks/useDashboardQueue.ts:106-125,572-587,716-731.
