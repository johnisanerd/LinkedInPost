---
id: 2026-10-27-j033-disconnect-a-sheet-and-sync-from
title: J-033 Disconnect a sheet and sync from sheet
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Sheet connected.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/persistence/pipeline-db/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google Sheets
legacy_id: J-033
---

## Purpose and scope

Disconnect a sheet and sync from sheet. Priority P2, CORE yes. Imported from journey J-033 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Sheet connected.

## Steps and information flow

1. `ACTION syncFromSheets {}`.
2. `ACTION disconnectSpreadsheet {}`.
3. `ACTION getRows {}`.

## Modules and code map

worker/src/index.ts (`syncFromSheets`, `disconnectSpreadsheet`, `getRows`), worker/src/persistence/pipeline-db/pipeline.ts

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Step 1 `{ok:true,count:N}`. Step 2 sets `users.spreadsheet_id=''` only; the sheet itself and the service-account share remain. Step 3 returns D1 rows only (`getRowsByUserId`). Calling `syncFromSheets` when disconnected returns `No Google Sheet is connected. Connect one from the Connections page first.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
