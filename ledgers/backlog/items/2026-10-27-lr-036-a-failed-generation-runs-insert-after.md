---
id: 2026-10-27-lr-036-a-failed-generation-runs-insert-after
title: A failed generation_runs INSERT after all LLM and image spend discards the successful result, and retries repeat deterministic failures.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
related: []
docs:
- generation-worker/src/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: generation-worker
raw_id: LR-036
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

A failed generation_runs INSERT after all LLM and image spend discards the successful result, and retries repeat deterministic failures.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053
- **Aliases:** GWP-005
- **Evidence:** generation-worker/src/pipeline.ts:240-272
- **Repro:** static; force a D1 error (oversized row per GWP-004).
- **Fix hint:** Catch the persist error, record trace.persistError, and still return the result.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Catch the persist error, record trace.persistError, and still return the result.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-036). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/pipeline.ts:240-272.
