---
id: 2026-10-27-j138-legacy-rows-and-shared-config-data
title: J-138 Legacy rows and shared-config data after upgrade
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Sheet rows created before `topicId` existed, or `topicGenerationRules` containing plain text instead of JSON.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/features/topic-navigation/utils/topicRoute.ts
- worker/src/index.ts
- worker/migrations/0002_pipeline_topic_id_pk.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Google Sheets
legacy_id: J-138
---

## Purpose and scope

Legacy rows and shared-config data after upgrade. Priority P2, CORE yes. Imported from journey J-138 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Sheet rows created before `topicId` existed, or `topicGenerationRules` containing plain text instead of JSON.

## Steps and information flow

1. Open `/topics`; open such a topic (route needs `encodeTopicRouteId(row)`).
2. Publish it (`requireTopicId(row)` in the schedule path).
3. `sendTopicToGeneration` on a row with non-JSON `topicGenerationRules`.

## Modules and code map

frontend/src/features/topic-navigation/utils/topicRoute.ts, worker/src/index.ts (`requireTopicId`, `sendTopicToGeneration`), worker/migrations/0002_pipeline_topic_id_pk.sql

Code anchors that exist: frontend/src/features/topic-navigation/utils/topicRoute.ts, worker/src/index.ts, worker/migrations/0002_pipeline_topic_id_pk.sql

## Success and acceptance

Rows get a stable `topicId` on merge (no blank id); publish works; non-JSON rules are ignored (`catch { // ignore malformed JSON }`) rather than failing; scheduled publish for a row without id is refused with a clear message.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
