---
id: 2026-10-27-lr-146-one-topics-row-without-an-id
title: One Topics row without an id breaks every read through getMergedRows, and getRowByTopicId reads the whole sheet on the generation critical path.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
- 2026-10-27-j056-send-to-generation-button-on-a
- 2026-10-27-j082-schedule-a-future-post-queued-via
- 2026-10-27-j129-google-sheets-unavailable-or-unshared-during
related: []
docs:
- worker/src/persistence/pipeline-db/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P2
area: worker/db
raw_id: LR-146
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

One Topics row without an id breaks every read through getMergedRows, and getRowByTopicId reads the whole sheet on the generation critical path.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-040, J-056, J-082, J-129
- **Aliases:** WKA-026
- **Evidence:** worker/src/persistence/pipeline-db/pipeline.ts:157-235
- **Repro:** static. Executor: add a row with an empty column C in the Topics tab, then press Send to Generation.
- **Fix hint:** Skip and report rows without ids, make getRowByTopicId a keyed D1 read with sheet fallback on miss.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Skip and report rows without ids, make getRowByTopicId a keyed D1 read with sheet fallback on miss.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-146). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/persistence/pipeline-db/pipeline.ts:157-235.
