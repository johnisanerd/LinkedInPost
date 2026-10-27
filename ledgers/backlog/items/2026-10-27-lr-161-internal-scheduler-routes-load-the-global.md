---
id: 2026-10-27-lr-161-internal-scheduler-routes-load-the-global
title: Internal scheduler routes load the global config and arm without a user, and the scheduler secret and webhook verify token use weak comparison.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j115-instagram-webhook-verification-handshake
- 2026-10-27-j117-telegram-and-linkedin-webhooks-verify-signatures
- 2026-10-27-j144-scheduler-secret-internal-routes
related: []
docs:
- worker/src/index.ts
- worker/src/automations/platforms/instagram.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/schedule
raw_id: LR-161
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Internal scheduler routes load the global config and arm without a user, and the scheduler secret and webhook verify token use weak comparison.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-082, J-115, J-117, J-144
- **Aliases:** WKA-035, WKB-043
- **Evidence:** worker/src/index.ts:1298-1387; worker/src/automations/platforms/instagram.ts:15
- **Repro:** static.
- **Fix hint:** Require userId in these payloads or remove the routes, use timing-safe compare and a random per-registration verify token.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Require userId in these payloads or remove the routes, use timing-safe compare and a random per-registration verify token.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-161). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:1298-1387.
