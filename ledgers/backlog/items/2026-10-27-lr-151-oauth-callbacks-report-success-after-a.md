---
id: 2026-10-27-lr-151-oauth-callbacks-report-success-after-a
title: OAuth callbacks report success after a silent per-user save failure, decodeURIComponent can throw outside the try, and state can be forged.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j094-connect-linkedin-popup-oauth
- 2026-10-27-j095-connect-instagram
- 2026-10-27-j096-connect-gmail
- 2026-10-27-j098-oauth-popup-closed-blocked-or-cancelled
- 2026-10-27-j100-replayed-or-expired-oauth-state
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
raw_id: LR-151
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

OAuth callbacks report success after a silent per-user save failure, decodeURIComponent can throw outside the try, and state can be forged.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-094..J-096, J-098, J-100
- **Aliases:** WKA-033
- **Evidence:** worker/src/index.ts:3553-3582,3533-3541
- **Repro:** static. Executor: remove the `social_integrations` table, run a connect, check the popup result.
- **Fix hint:** Let a per-user save failure fail the callback, drop decodeURIComponent, bind state to a client-side nonce.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Let a per-user save failure fail the callback, drop decodeURIComponent, bind state to a client-side nonce.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-151). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:3553-3582,3533-3541.
