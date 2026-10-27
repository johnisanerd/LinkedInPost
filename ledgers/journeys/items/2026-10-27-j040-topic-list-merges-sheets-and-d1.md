---
id: 2026-10-27-j040-topic-list-merges-sheets-and-d1
title: J-040 Topic list merges Sheets and D1
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Sheet connected with rows edited by hand in the sheet.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/persistence/pipeline-db/pipeline.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google Sheets
legacy_id: J-040
---

## Purpose and scope

Topic list merges Sheets and D1. Priority P1, CORE yes. Imported from journey J-040 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Sheet connected with rows edited by hand in the sheet.

## Steps and information flow

1. Open `/topics` (calls `ACTION getRows {}`).
2. Add a row manually in the sheet, reload.
3. Filter by status chips in the queue (Draft / Pending / Approved / Published).

## Modules and code map

worker/src/index.ts (`getRows`), worker/src/persistence/pipeline-db/pipeline.ts (`getMergedRows`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

New sheet row appears after reload with `topicId` assigned; counts per status match; no duplicate rows for topics that exist in both stores.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
