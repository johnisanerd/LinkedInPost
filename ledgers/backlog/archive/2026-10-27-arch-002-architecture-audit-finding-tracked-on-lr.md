---
id: 2026-10-27-arch-002-architecture-audit-finding-tracked-on-lr
title: ALLOWED_EMAILS is never read by the worker and new users default to status active, so any verified Google account gets in (architecture-audit view of LR-009)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-009-allowed-emails-is-never-read-by
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P0
area: arch/worker/auth
raw_id: ARCH-002
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-009.

## Evidence and reproduction

- **Covered by:** LR-009

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-002). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-009; the work is tracked on LR-009 (record 2026-10-27-lr-009-allowed-emails-is-never-read-by). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-009
