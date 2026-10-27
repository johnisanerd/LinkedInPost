---
id: 2026-10-27-lr-055-addtopic-swallows-a-sheets-failure-so
title: addTopic swallows a Sheets failure so the topic disappears from the merged list for sheet users, and other write paths share the problem.
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j035-add-a-topic-from-the-scratchpad
- 2026-10-27-j040-topic-list-merges-sheets-and-d1
- 2026-10-27-j129-google-sheets-unavailable-or-unshared-during
- 2026-10-27-j130-sheets-down-while-adding-a-topic
related: []
docs:
- worker/src/index.ts
- worker/src/persistence/pipeline-db/pipeline.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P1
area: worker/db
raw_id: LR-055
source_file: docs/launch-readiness/findings/REVIEW-ITEMS.md
---

## Problem

addTopic swallows a Sheets failure so the topic disappears from the merged list for sheet users, and other write paths share the problem.

## Evidence and reproduction

- **Confidence:** confirmed-by-reading
- **Journeys:** J-035, J-040, J-129, J-130
- **Aliases:** WKA-025
- **Evidence:** worker/src/index.ts:1632-1651; worker/src/persistence/pipeline-db/pipeline.ts:197-231
- **Repro:** static. Executor: connect a sheet, revoke the service-account share, add a topic, reload.
- **Fix hint:** Fail the request when the Sheets append fails and list D1-only rows in getMergedRows.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Fail the request when the Sheets append fails and list D1-only rows in getMergedRows.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/REVIEW-ITEMS.md (LR-055). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: static reading of worker/src/index.ts:1632-1651.
