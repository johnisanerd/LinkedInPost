---
id: 2026-10-27-lr-136-automation-rules-and-youtube-schedules-expire
title: Automation rules and YouTube schedules expire from KV after 30 days with no notice
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j114-automation-rules-admin
- 2026-10-27-j118-youtube-comment-polling-schedule
related: []
docs:
- worker/src/automations/kv.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/automations
raw_id: LR-136
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Automation rules and YouTube schedules expire from KV after 30 days with no notice.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-114, J-118
- **Aliases:** WKB-030
- **Evidence:** worker/src/automations/kv.ts:44-64,94-100
- **Repro:** static; executor: save a rule, wait 30 days or inspect KV TTL.
- **Fix hint:** Drop the TTL (cleanup already removes disabled rules) or refresh on read.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Drop the TTL (cleanup already removes disabled rules) or refresh on read.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-136). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/automations/kv.ts:44-64,94-100.
