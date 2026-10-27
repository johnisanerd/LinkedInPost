---
id: 2026-10-27-lr-150-trending-panels-use-deployment-wide-env
title: Trending panels use deployment-wide env credentials for every user, and LinkedIn statistics accept a caller-chosen orgId.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j051-trending-panels-youtube-linkedin-instagram-use
related: []
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/integrations
raw_id: LR-150
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Trending panels use deployment-wide env credentials for every user, and LinkedIn statistics accept a caller-chosen orgId.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-051
- **Aliases:** WKA-032
- **Evidence:** worker/src/index.ts:2670-2726
- **Repro:** static.
- **Fix hint:** Admin-gate or per-user-scope these actions and restrict orgId.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Admin-gate or per-user-scope these actions and restrict orgId.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-150). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:2670-2726.
