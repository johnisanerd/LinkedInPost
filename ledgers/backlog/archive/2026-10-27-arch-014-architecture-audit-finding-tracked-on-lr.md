---
id: 2026-10-27-arch-014-architecture-audit-finding-tracked-on-lr
title: Several env names read by the code (YOUTUBE_CLIENT_ID, OAUTH_REDIRECT_BASE_URL, WORKER_SHARED_SECRET and others) are missing from .env.example. (architecture-audit view of LR-079)
created: '2026-10-27'
updated: '2026-10-27'
journeys: []
related:
- 2026-10-27-lr-046-the-web-wizard-dead-ends-at
docs: []
status: closed
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: architecture
severity: P2
area: arch/.env.example
raw_id: ARCH-014
source_file: docs/launch-readiness/findings/ARCH-ITEMS.md
resolution: duplicate
---

## Problem

Architecture audit finding, tracked on LR-046.

## Evidence and reproduction

- **Covered by:** LR-046

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.

## Plan

Decide the fix first; record the decision in Attempts.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/ARCH-ITEMS.md (ARCH-014). Static reading only; nothing executed. Closed as duplicate.

## Verification

Duplicate of LR-079; the work is tracked on LR-079 (record 2026-10-27-lr-079-several-env-names-read-by-the). Closed here so there is one owner for the work.

Evidence: read-only: described in ARCH-AUDIT.md; work tracked on LR-046
