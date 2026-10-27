---
id: 2026-10-27-lr-058-fetchwithretry-retries-non-idempotent-posts-posts
title: fetchWithRetry retries non-idempotent POSTs (posts, emails, WhatsApp) and honours Retry-After without a cap, causing duplicates or stalls.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j076-publish-now-to-linkedin
- 2026-10-27-j077-publish-to-instagram-image-required
- 2026-10-27-j078-send-via-gmail
- 2026-10-27-j079-send-via-whatsapp
- 2026-10-27-j080-send-via-telegram
- 2026-10-27-j088-double-click-on-publish
related: []
docs:
- worker/src/integrations/_shared/fetchWithRetry.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/integrations
raw_id: LR-058
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

fetchWithRetry retries non-idempotent POSTs (posts, emails, WhatsApp) and honours Retry-After without a cap, causing duplicates or stalls.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-076..J-080, J-088
- **Aliases:** WKB-009, WKB-046
- **Evidence:** worker/src/integrations/_shared/fetchWithRetry.ts:55-77
- **Repro:** static. Executor: mock the endpoint to return 502 after recording the request; count requests.
- **Fix hint:** Do not retry the final create call (retry only idempotent upload steps and pre-connection errors), cap Retry-After, honour Telegram retry_after.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Do not retry the final create call (retry only idempotent upload steps and pre-connection errors), cap Retry-After, honour Telegram retry_after.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-058). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/integrations/_shared/fetchWithRetry.ts:55-77.
