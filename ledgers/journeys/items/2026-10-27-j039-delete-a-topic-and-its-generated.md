---
id: 2026-10-27-j039-delete-a-topic-and-its-generated
title: J-039 Delete a topic (and its generated images)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Topic with generated images in GCS.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Google Sheets
legacy_id: J-039
---

## Purpose and scope

Delete a topic (and its generated images). Priority P1, CORE yes. Imported from journey J-039 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Topic with generated images in GCS.

## Steps and information flow

1. In the queue choose delete and confirm "Confirm Delete".
2. API: `ACTION deleteRow {"row":{<full SheetRow incl. topic,date,topicId,rowIndex>}}`.
3. Simulate a Sheets failure after step 2 starts.

## Modules and code map

worker/src/index.ts (`deleteRow`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`handleDeleteTopic`)

Code anchors that exist: worker/src/index.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts

## Success and acceptance

D1 `pipeline_state` row and news snapshots removed, GCS objects for the topic prefix removed, sheet row removed. Order in code is: GCS delete, then D1 delete in parallel with snapshot delete, then `sheets.deleteRow` last; a Sheets failure leaves the D1 row gone but the sheet row present, and the next merge may resurrect it (CODE-READING FINDING). No soft-delete / undo.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
