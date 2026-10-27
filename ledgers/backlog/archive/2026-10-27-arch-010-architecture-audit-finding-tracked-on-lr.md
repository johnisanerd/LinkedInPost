---
id: 2026-10-27-arch-010-architecture-audit-finding-tracked-on-lr
title: 'Publish has no server-side idempotency: the client row is trusted, status is not checked, and a failed mark step lets a retry post twice. (architecture-audit view of LR-070)'
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-070-publish-has-no-server-side-idempotency
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P1
area: arch/worker/scheduled-publish
raw_id: ARCH-010
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-070.

## Evidence and reproduction

- **Covered by:** LR-070

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-010). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-070; the work is tracked on LR-070 (record 2026-10-27-lr-070-publish-has-no-server-side-idempotency). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-070
