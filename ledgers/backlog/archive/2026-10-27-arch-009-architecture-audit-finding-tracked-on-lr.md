---
id: 2026-10-27-arch-009-architecture-audit-finding-tracked-on-lr
title: The root wrangler.jsonc reuses the API worker name, has no main, and uploads frontend source as assets, so a root deploy overwrites the API. (architecture-audit view of LR-018)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-018-the-root-wrangler-jsonc-reuses-the
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P1
area: arch/root
raw_id: ARCH-009
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-018.

## Evidence and reproduction

- **Covered by:** LR-018

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-009). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-018; the work is tracked on LR-018 (record 2026-10-27-lr-018-the-root-wrangler-jsonc-reuses-the). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-018
