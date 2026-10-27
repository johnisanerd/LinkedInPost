---
id: 2026-10-27-lr-098-waitlist-signup-shows-success-even-when
title: Waitlist signup shows success even when the server rejects the request
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j018-waitlist-request-public-endpoint
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
area: frontend/saas
raw_id: LR-098
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Waitlist signup shows success even when the server rejects the request.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-018
- **Aliases:** FEB-015
- **Evidence:** frontend/src/services/backendApi.ts:1612-1622; frontend/src/features/saas/Landing.tsx:179-191
- **Repro:** worker returns 400 `{ok:false}`; thank-you state still appears. Static reasoning.
- **Fix hint:** Throw when !res.ok or !body.ok.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Throw when !res.ok or !body.ok.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-098). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of frontend/src/services/backendApi.ts:1612-1622.
