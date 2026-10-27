---
id: 2026-10-27-lr-160-the-public-waitlist-endpoint-is-unthrottled
title: The public waitlist endpoint is unthrottled with unbounded fields and a promised email that is never sent, and admin budget cannot be set to 0.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j017-non-approved-google-account-signs-in
- 2026-10-27-j018-waitlist-request-public-endpoint
- 2026-10-27-j019-admin-approves-a-waitlist-entry
- 2026-10-27-j123-admin-panel-users-approve-suspend-budget
related: []
docs:
- worker/src/modes/saas/waitlist.ts
- worker/src/modes/saas/admin.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/saas
raw_id: LR-160
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The public waitlist endpoint is unthrottled with unbounded fields and a promised email that is never sent, and admin budget cannot be set to 0.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-017..J-019, J-123
- **Aliases:** WKA-030, WKB-040
- **Evidence:** worker/src/modes/saas/waitlist.ts:4-26; worker/src/modes/saas/admin.ts:44-59
- **Repro:** static.
- **Fix hint:** Cap field lengths, add a KV/IP rate limit, send or remove the email promise, allow budget === 0.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Cap field lengths, add a KV/IP rate limit, send or remove the email promise, allow budget === 0.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-160). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/modes/saas/waitlist.ts:4-26.
