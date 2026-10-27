---
id: 2026-10-27-lr-004-the-generation-worker-has-no-per
title: 'The generation worker has no per-user identity: clips, variants and runs are keyed by a caller-supplied sessionId any secret holder can use.'
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j045-attach-clips-to-a-draft-and
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j140-tenant-a-cannot-read-or-modify
- 2026-10-27-j142-per-user-lists-are-scoped-clips
related: []
docs:
- generation-worker/src/players/clips.ts
- generation-worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: generation-worker
raw_id: LR-004
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The generation worker has no per-user identity: clips, variants and runs are keyed by a caller-supplied sessionId any secret holder can use.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-044, J-045, J-053, J-140, J-142
- **Aliases:** GWP-002
- **Evidence:** generation-worker/src/players/clips.ts:8-14,32; generation-worker/src/index.ts:258-270
- **Repro:** static. With the shared secret: GET /v1/clips/<victim sessionId>; DELETE /v1/clips/<victim>/<clipId>.
- **Fix hint:** Drop the unused /v1/clips and /v1/variants routes (no caller found) or derive sessionId from the verified session; add user_id to generation_runs.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Drop the unused /v1/clips and /v1/variants routes (no caller found) or derive sessionId from the verified session; add user_id to generation_runs.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-004). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/players/clips.ts:8-14,32.
