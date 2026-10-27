---
id: 2026-10-27-j035-add-a-topic-from-the-scratchpad
title: J-035 Add a topic from the scratchpad
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Signed in with a sheet connected (see J-031).
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
priority: P1
core: 'yes'
external_service: Google Sheets
legacy_id: J-035
---

## Purpose and scope

Add a topic from the scratchpad. Priority P1, CORE yes. Imported from journey J-035 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Signed in with a sheet connected (see J-031).

## Steps and information flow

1. Go to `/topics/new` ("Add topic details").
2. Fill topic title, About, Message to convey, style, audience, notes.
3. Submit.
4. API form: `ACTION addTopic {"topic":"Why X","date":"2026-10-28","topicMeta":{"about":"...","meaning":"...","style":"Professional","audience":"...","notes":"...","pros":[],"cons":[]}}`.

## Modules and code map

frontend/src/features/add-topic/AddTopicPage.tsx, worker/src/index.ts (`addTopic`), worker/src/persistence/pipeline-db/pipeline.ts (`addTopicToD1`)

Code anchors that exist: worker/src/index.ts, worker/src/persistence/pipeline-db/pipeline.ts

## Success and acceptance

Response is the new row with a UUID `topicId`, `status:"Draft"`. A row exists in D1 `pipeline_state` (written first) and, if a sheet is connected, in the sheet. Empty topic -> `topic is required.`; `topicMeta` JSON over 8000 chars -> `Topic metadata is too large.` A Sheets error is logged but does not fail the request.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
