---
id: 2026-10-27-lr-153-multi-part-sends-leave-partial-deliveries
title: Multi-part sends leave partial deliveries on error, Instagram publishes before the container is ready, and Telegram has no length split.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j077-publish-to-instagram-image-required
- 2026-10-27-j079-send-via-whatsapp
- 2026-10-27-j080-send-via-telegram
related: []
docs:
- worker/src/integrations/telegram/index.ts
- worker/src/integrations/instagram/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/integrations
raw_id: LR-153
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Multi-part sends leave partial deliveries on error, Instagram publishes before the container is ready, and Telegram has no length split.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-077, J-079, J-080
- **Aliases:** WKB-033
- **Evidence:** worker/src/integrations/telegram/index.ts:159-233; worker/src/integrations/instagram/index.ts:162-183
- **Repro:** static.
- **Fix hint:** Return partial-delivery info, throw on container-ready timeout, split text by channel limit.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Return partial-delivery info, throw on container-ready timeout, split text by channel limit.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-153). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/integrations/telegram/index.ts:159-233.
