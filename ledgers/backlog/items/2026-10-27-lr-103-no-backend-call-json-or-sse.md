---
id: 2026-10-27-lr-103-no-backend-call-json-or-sse
title: No backend call (JSON or SSE) has a timeout or abort, so a stalled worker leaves Publishing or Generating stuck and invites a double publish.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j023-backend-unreachable-at-boot
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j054-network-drop-in-the-middle-of
- 2026-10-27-j065-quick-change-via-sse
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j088-double-click-on-publish
related: []
docs:
- frontend/src/services/backendApi.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: frontend/shell
raw_id: LR-103
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

No backend call (JSON or SSE) has a timeout or abort, so a stalled worker leaves Publishing or Generating stuck and invites a double publish.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-023, J-053, J-054, J-065, J-076, J-088
- **Aliases:** FEA-022
- **Evidence:** frontend/src/services/backendApi.ts:559-595,653-702,1399-1454
- **Repro:** Point the worker at a hung generation worker; click Quick Change; observe an endless spinner, no cancel.
- **Fix hint:** Wrap fetches with AbortSignal.timeout (60 s JSON, 120 s idle for SSE), expose cancel, flush the trailing buffer.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wrap fetches with AbortSignal.timeout (60 s JSON, 120 s idle for SSE), expose cancel, flush the trailing buffer.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-103). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/services/backendApi.ts:559-595,653-702,1399-1454.
