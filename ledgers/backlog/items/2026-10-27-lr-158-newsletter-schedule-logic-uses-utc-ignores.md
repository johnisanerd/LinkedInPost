---
id: 2026-10-27-lr-158-newsletter-schedule-logic-uses-utc-ignores
title: Newsletter schedule logic uses UTC, ignores frequency and slots, resets next_send_at on any edit, and queries news with a literal word.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j109-create-a-newsletter-and-preview-it
- 2026-10-27-j111-scheduled-newsletter-send-vs-a-once
related: []
docs:
- worker/src/newsletter/persistence.ts
- worker/src/newsletter/contentAssembler.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/newsletter
raw_id: LR-158
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Newsletter schedule logic uses UTC, ignores frequency and slots, resets next_send_at on any edit, and queries news with a literal word.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-109, J-111
- **Aliases:** WKB-034
- **Evidence:** worker/src/newsletter/persistence.ts:3-44,264-303; worker/src/newsletter/contentAssembler.ts:79-88
- **Repro:** static; executor: create a Friday 17:00 newsletter from a UTC+5:30 account.
- **Fix hint:** Store a timezone, implement frequency, recompute only on schedule fields, bound cron concurrency, use topic keywords as the query.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Store a timezone, implement frequency, recompute only on schedule fields, bound cron concurrency, use topic keywords as the query.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-158). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/newsletter/persistence.ts:3-44,264-303.
