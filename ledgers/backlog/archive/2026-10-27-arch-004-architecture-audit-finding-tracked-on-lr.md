---
id: 2026-10-27-arch-004-architecture-audit-finding-tracked-on-lr
title: The only cron runs daily at 03:00 UTC but the newsletter scheduler needs a 2-hour window and never advances next_send_at, so most never send. (architecture-audit view of LR-053)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-053-the-only-cron-runs-daily-at
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P1
area: arch/worker/cron
raw_id: ARCH-004
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-053.

## Evidence and reproduction

- **Covered by:** LR-053

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-004). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-053; the work is tracked on LR-053 (record 2026-10-27-lr-053-the-only-cron-runs-daily-at). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-053
