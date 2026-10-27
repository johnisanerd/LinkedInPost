---
id: 2026-10-27-j130-sheets-down-while-adding-a-topic
title: J-130 Sheets down while adding a topic
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: Same as J-129.
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
legacy_id: J-130
---

## Purpose and scope

Sheets down while adding a topic. Priority P2, CORE yes. Imported from journey J-130 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Same as J-129.

## Steps and information flow

1. `ACTION addTopic {"topic":"Offline topic"}`.
2. Restore Sheets; reload and `ACTION syncFromSheets {}`.

## Modules and code map

worker/src/index.ts (`addTopic`), worker/src/persistence/pipeline-db/pipeline.ts (`getMergedRows`)

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Request returns 200 and the row (D1 first, Sheets error only logged); the sheet lacks the row; after restore the row is still present in `/topics` and is eventually mirrored or at least not duplicated/deleted by the merge.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
