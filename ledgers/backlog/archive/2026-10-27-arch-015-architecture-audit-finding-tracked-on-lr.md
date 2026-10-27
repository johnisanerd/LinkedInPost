---
id: 2026-10-27-arch-015-architecture-audit-finding-tracked-on-lr
title: setup runs npx tsc in frontend/ without installing dependencies, so setup aborts on a clean clone, and the check does not run on every path. (architecture-audit view of LR-043)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-043-setup-runs-npx-tsc-in-frontend
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P2
area: arch/setup.py
raw_id: ARCH-015
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-043.

## Evidence and reproduction

- **Covered by:** LR-043

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-015). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-043; the work is tracked on LR-043 (record 2026-10-27-lr-043-setup-runs-npx-tsc-in-frontend). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-043
