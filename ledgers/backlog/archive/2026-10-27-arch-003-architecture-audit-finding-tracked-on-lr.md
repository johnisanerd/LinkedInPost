---
id: 2026-10-27-arch-003-architecture-audit-finding-tracked-on-lr
title: The generation worker accepts requests when WORKER_SHARED_SECRET is empty (CORS *, non-constant-time compare), so it can be called without auth. (architecture-audit view of LR-050)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-050-the-generation-worker-accepts-requests-when
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P1
area: arch/generation-worker/auth
raw_id: ARCH-003
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-050.

## Evidence and reproduction

- **Covered by:** LR-050

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-003). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-050; the work is tracked on LR-050 (record 2026-10-27-lr-050-the-generation-worker-accepts-requests-when). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-050
