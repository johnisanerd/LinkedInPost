---
id: 2026-10-27-j108-re-importing-the-same-campaign-duplicate
title: J-108 Re-importing the same campaign (duplicate `topicId`)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: A campaign already imported.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/persistence/drafts.ts
- worker/src/persistence/pipeline-db/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: Google Sheets
legacy_id: J-108
---

## Purpose and scope

Re-importing the same campaign (duplicate `topicId`). Priority P2, CORE no. Imported from journey J-108 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A campaign already imported.

## Steps and information flow

1. Import the same JSON twice.
2. Import posts without `topicId`.

## Modules and code map

worker/src/persistence/drafts.ts, worker/src/persistence/pipeline-db/pipeline.ts (`bulkImportCampaign`)

Code anchors that exist: worker/src/persistence/drafts.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Second import updates or skips rows with the same `topicId` (no duplicates in D1 `pipeline_state` PK `(user_id, topic_id)` or in the sheet); missing `topicId` is rejected with a message.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
