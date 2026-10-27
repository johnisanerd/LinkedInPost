---
id: 2026-10-27-lr-115-saved-variants-and-clips-kv-routes
title: Saved-variants and clips KV routes use timestamp keys, no TTL, unvalidated input and a 1000-key listing, and appear to be unused.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j044-clip-an-article-or-a-passage
- 2026-10-27-j045-attach-clips-to-a-draft-and
related: []
docs:
- generation-worker/src/players/variants.ts
- generation-worker/src/players/clips.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: generation-worker
raw_id: LR-115
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Saved-variants and clips KV routes use timestamp keys, no TTL, unvalidated input and a 1000-key listing, and appear to be unused.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-044, J-045
- **Aliases:** GWP-022, GWP-023
- **Evidence:** generation-worker/src/players/variants.ts:6-12,24-25; generation-worker/src/players/clips.ts:51-89
- **Repro:** static.
- **Fix hint:** Delete the routes if unused, else validate sessionId and url, add a TTL and loop cursors.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Delete the routes if unused, else validate sessionId and url, add a TTL and loop cursors.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-115). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/players/variants.ts:6-12,24-25.
