---
id: 2026-10-27-lr-054-every-row-mutation-upserts-the-full
title: Every row mutation upserts the full client-supplied row with INSERT OR REPLACE, so stale tabs overwrite newer state and clients can set any field.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j063-open-generated-variants-and-pick-one
- 2026-10-27-j064-manual-edit-with-undo-redo-draft
- 2026-10-27-j087-calendar-drag-reschedule-of-an-already
- 2026-10-27-j088-double-click-on-publish
- 2026-10-27-j091-republish-an-already-published-post
related: []
docs:
- worker/src/persistence/pipeline-db/pipeline.ts
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/db
raw_id: LR-054
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

Every row mutation upserts the full client-supplied row with INSERT OR REPLACE, so stale tabs overwrite newer state and clients can set any field.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-063, J-064, J-087, J-088, J-091
- **Aliases:** WKA-011
- **Evidence:** worker/src/persistence/pipeline-db/pipeline.ts (INSERT_PIPELINE_ROW_SQL); worker/src/index.ts:2245-2258
- **Repro:** static. Executor: two tabs, publish in one, then change the schedule in the other.
- **Fix hint:** Use column-targeted UPDATE ... WHERE user_id=? AND topic_id=? per action, whitelist status transitions, add an updated_at precondition.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Use column-targeted UPDATE ... WHERE user_id=? AND topic_id=? per action, whitelist status transitions, add an updated_at precondition.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-054). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/persistence/pipeline-db/pipeline.ts (INSERT_PIPELINE_ROW_SQL).
