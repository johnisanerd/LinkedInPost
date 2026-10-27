---
id: 2026-10-27-arch-005-architecture-audit-finding-tracked-on-lr
title: start.sh looks for a setup/setup.py that does not exist, silently skips provisioning in production mode, and never starts the worker. (architecture-audit view of LR-040)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-040-start-sh-looks-for-a-setup
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P1
area: arch/start.sh
raw_id: ARCH-005
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-040.

## Evidence and reproduction

- **Covered by:** LR-040

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-005). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-040; the work is tracked on LR-040 (record 2026-10-27-lr-040-start-sh-looks-for-a-setup). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-040
