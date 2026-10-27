---
id: 2026-10-27-lr-063-newsletter-send-has-no-claim-or
title: Newsletter send has no claim or lock, so a manual send racing the cron sends twice, and partial Telegram failures still mark the issue sent.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j110-draft-approve-and-send-a-newsletter
- 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
- 2026-10-27-j112-newsletter-actions-are-not-tenant-scoped
related: []
docs:
- worker/src/newsletter/handlers.ts
- worker/src/newsletter/scheduler.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/newsletter
raw_id: LR-063
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter send has no claim or lock, so a manual send racing the cron sends twice, and partial Telegram failures still mark the issue sent.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-110..J-112
- **Aliases:** WKB-018, WKA-024 (lock and swallowed cron errors)
- **Evidence:** worker/src/newsletter/handlers.ts:63-90; worker/src/newsletter/scheduler.ts:37-49,60-107
- **Repro:** static. Executor: invoke `newsletter.sendApproved` twice in parallel on one issue.
- **Fix hint:** Atomic UPDATE status=sending WHERE status=approved and proceed only if one row changed, record per-recipient results, restrict the cron to the current window issue, log cron failures.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Atomic UPDATE status=sending WHERE status=approved and proceed only if one row changed, record per-recipient results, restrict the cron to the current window issue, log cron failures.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-063). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/handlers.ts:63-90.
