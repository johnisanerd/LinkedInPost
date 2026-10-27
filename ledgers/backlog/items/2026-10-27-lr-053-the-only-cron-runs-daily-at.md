---
id: 2026-10-27-lr-053-the-only-cron-runs-daily-at
title: The only cron runs daily at 03:00 UTC but the newsletter scheduler needs a 2-hour window and never advances next_send_at, so most never send.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
- 2026-10-27-j119-daily-cron-housekeeping
related: []
docs:
- worker/src/newsletter/scheduler.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/cron
raw_id: LR-053
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The only cron runs daily at 03:00 UTC but the newsletter scheduler needs a 2-hour window and never advances next_send_at, so most never send.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-111, J-119
- **Aliases:** ARCH-004, WKA-024 (window stuck)
- **Evidence:** worker/wrangler.jsonc:17-21; worker/src/newsletter/scheduler.ts (processNewsletter window branches)
- **Repro:** static. Executor: create an email newsletter, approve an issue, wait for the send window.
- **Fix hint:** Run the cron hourly or every 15 minutes, or send anything with next_send_at <= now and not yet sent; advance next_send_at after every window.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Run the cron hourly or every 15 minutes, or send anything with next_send_at <= now and not yet sent; advance next_send_at after every window.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-053). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/wrangler.jsonc:17-21.
