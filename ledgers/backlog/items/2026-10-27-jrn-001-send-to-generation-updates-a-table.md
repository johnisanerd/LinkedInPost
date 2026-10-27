---
id: 2026-10-27-jrn-001-send-to-generation-updates-a-table
title: Send to Generation updates a table that does not exist (pipeline_rows), so the status flip throws after the generation worker has already started
created: '2026-10-27'
updated: '2026-10-27'
journeys:
- 2026-10-27-j056-send-to-generation-button-on-a
related:
- 2026-10-27-lr-056-send-to-generation-navigates-away-without
docs:
- worker/src/index.ts
status: open
owner: null
branch: null
worktree: null
claimed_at: null
blocked_reason: null
type: defect
severity: P0
area: worker/generation
raw_id: JRN-001
source_file: docs/launch-readiness/findings/JOURNEY-DELTA.md
---

## Problem

Send to Generation updates a table that does not exist (pipeline_rows), so the status flip throws after the generation worker has already started.

## Evidence and reproduction

- **Journeys:** J-056
- **Covers:** none (LR-056 is closest but describes the unconsumed stream and non-atomic claim, not the missing table)
- **Confidence:** confirmed-by-reading
- **Evidence:** worker/src/index.ts:1212,1219,1227 (UPDATE pipeline_rows); no migration in worker/migrations defines pipeline_rows (the table is pipeline_state)
- **Repro:** Create a Draft topic, click "Send to Generation". Expect HTTP 400 with a D1 "no such table: pipeline_rows" error while the generation worker run is already started; the topic never reaches Pending via this path. The revert-to-Draft handlers fail the same way.
- **Fix hint:** Change the three statements to the real table and columns (pipeline_state), or call the existing pipeline status helper; add a test that runs the handler against the migrated schema.

## Acceptance criteria

- The reproduction in Evidence and reproduction no longer shows the defect, checked at a named source revision.
- Journeys named in this record's journeys field pass their pass checks after the fix.

## Plan

Change the three statements to the real table and columns (pipeline_state), or call the existing pipeline status helper; add a test that runs the handler against the migrated schema.

## Attempts

- 2026-10-27 — Filed from docs/launch-readiness/findings/JOURNEY-DELTA.md (JRN-001). Static reading only; nothing executed.

## Verification

Pending. No check has been run: this record was filed from static reading only. Read-only evidence on file: read-only: worker/src/index.ts:1212-1227.
