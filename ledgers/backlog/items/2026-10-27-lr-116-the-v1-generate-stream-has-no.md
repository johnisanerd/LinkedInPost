---
id: 2026-10-27-lr-116-the-v1-generate-stream-has-no
title: The /v1/generate stream has no client-disconnect or emit error handling, and a strict Accept match falls back to a slow 5-minute response.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j053-generate-a-draft-from-the-queue
- 2026-10-27-j054-network-drop-in-the-middle-of
related: []
docs:
- generation-worker/src/index.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: generation-worker
raw_id: LR-116
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

The /v1/generate stream has no client-disconnect or emit error handling, and a strict Accept match falls back to a slow 5-minute response.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-053, J-054
- **Aliases:** GWP-026
- **Evidence:** generation-worker/src/index.ts:132-174; worker/src/index.ts:893-945
- **Repro:** static; send Accept with extra values; cancel the stream mid-run.
- **Fix hint:** Use includes(text/event-stream), thread an AbortSignal, catch emit errors.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use includes(text/event-stream), thread an AbortSignal, catch emit errors.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-116). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of generation-worker/src/index.ts:132-174.
