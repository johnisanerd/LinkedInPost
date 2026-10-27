---
id: 2026-10-27-lr-067-gmail-telegram-and-whatsapp-recipients-come
title: Gmail, Telegram and WhatsApp recipients come from the request with no allow-list against saved ones, so users can message arbitrary targets.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j078-send-via-gmail
- 2026-10-27-j079-send-via-whatsapp
- 2026-10-27-j080-send-via-telegram
- 2026-10-27-j103-a-user-with-no-linkedin-connection
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
severity: P1
area: worker/publish
raw_id: LR-067
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Gmail, Telegram and WhatsApp recipients come from the request with no allow-list against saved ones, so users can message arbitrary targets.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-078..J-080, J-103
- **Aliases:** WKA-029
- **Evidence:** worker/src/index.ts:4842-4845,5102-5109
- **Repro:** static. Executor: user B with no Gmail connection calls `publishContent` channel `gmail` with `emailTo` set to an external address.
- **Fix hint:** Allow only saved recipients for shared channels and require per-user credentials for Gmail.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Allow only saved recipients for shared channels and require per-user credentials for Gmail.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-067). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:4842-4845,5102-5109.
