---
id: 2026-10-27-lr-109-disconnecting-a-channel-or-sheet-has
title: Disconnecting a channel or sheet has no confirmation and no error state even with posts scheduled against it
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j102-disconnect-a-channel-three-different-disconnect
related: []
docs: []
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-109
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Disconnecting a channel or sheet has no confirmation and no error state even with posts scheduled against it.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082, J-102
- **Aliases:** FEB-011
- **Evidence:** frontend/src/pages/connections/ConnectionsPage.tsx:408-416; frontend/src/App.tsx:439-447
- **Repro:** click Disconnect with a scheduled post. Static reasoning.
- **Fix hint:** Confirm with the count of scheduled posts on that channel and show failures.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Confirm with the count of scheduled posts on that channel and show failures.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-109). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/pages/connections/ConnectionsPage.tsx:408-416.
