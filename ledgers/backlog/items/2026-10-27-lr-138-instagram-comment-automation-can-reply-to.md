---
id: 2026-10-27-lr-138-instagram-comment-automation-can-reply-to
title: Instagram comment automation can reply to its own comments and re-fires on webhook redelivery
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j114-automation-rules-admin
- 2026-10-27-j115-instagram-webhook-verification-handshake
related: []
docs:
- worker/src/automations/platforms/instagram.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/automations
raw_id: LR-138
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Instagram comment automation can reply to its own comments and re-fires on webhook redelivery.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-114, J-115
- **Aliases:** WKB-032
- **Evidence:** worker/src/automations/platforms/instagram.ts:42-81
- **Repro:** static; executor: enable a comment rule and comment on a post; check for a self-reply chain.
- **Fix hint:** Skip events from the page own id, store a seen-set by comment id, ack first and process in waitUntil.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Skip events from the page own id, store a seen-set by comment id, ack first and process in waitUntil.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-138). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/automations/platforms/instagram.ts:42-81.
