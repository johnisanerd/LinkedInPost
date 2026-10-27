---
id: 2026-10-27-lr-137-gmail-auto-reply-needs-a-kv
title: Gmail auto-reply needs a KV key nothing writes, the push endpoint has no sender authentication, and LinkedIn automation lacks credentials.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j114-automation-rules-admin
- 2026-10-27-j116-gmail-push-webhook-has-no-sender
- 2026-10-27-j117-telegram-and-linkedin-webhooks-verify-signatures
related: []
docs:
- worker/src/automations/platforms/gmail.ts
- worker/src/automations/routes.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/automations
raw_id: LR-137
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Gmail auto-reply needs a KV key nothing writes, the push endpoint has no sender authentication, and LinkedIn automation lacks credentials.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-114, J-116, J-117
- **Aliases:** WKB-031
- **Evidence:** worker/src/automations/platforms/gmail.ts:38-116; worker/src/automations/routes.ts:55-58,253-263
- **Repro:** static; executor: POST `/automations/webhooks/register {platform:'gmail'}`.
- **Fix hint:** Wire the OAuth token and Pub/Sub JWT verification or hide the feature.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Wire the OAuth token and Pub/Sub JWT verification or hide the feature.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-137). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/automations/platforms/gmail.ts:38-116.
