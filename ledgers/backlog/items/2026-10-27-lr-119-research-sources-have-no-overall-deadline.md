---
id: 2026-10-27-lr-119-research-sources-have-no-overall-deadline
title: Research sources have no overall deadline (up to about 3 minutes) and the wrapping withRetry never retries because the runner never throws.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j052-topic-news-research-and-history
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- packages/researcher/src/search.ts
- generation-worker/src/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: packages/researcher
raw_id: LR-119
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Research sources have no overall deadline (up to about 3 minutes) and the wrapping withRetry never retries because the runner never throws.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-052, J-053
- **Aliases:** GWP-013
- **Evidence:** packages/researcher/src/search.ts:23-64; generation-worker/src/pipeline.ts:82-97
- **Repro:** static; configure 40 slow feeds.
- **Fix hint:** One AbortSignal with a 15-20 s overall budget, run API providers in parallel with the RSS batch, drop the dead retry.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

One AbortSignal with a 15-20 s overall budget, run API providers in parallel with the RSS batch, drop the dead retry.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-119). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of packages/researcher/src/search.ts:23-64.
