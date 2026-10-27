---
id: 2026-10-27-j037-edit-a-topic-s-metadata
title: J-037 Edit a topic's metadata
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Existing topic.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: none
legacy_id: J-037
---

## Purpose and scope

Edit a topic's metadata. Priority P2, CORE yes. Imported from journey J-037 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Existing topic.

## Steps and information flow

1. Open the topic from `/topics`, edit via the add-topic form in edit mode.
2. API: `ACTION updateTopicMeta {"topicId":"<id>","topic":"New title","topicMeta":{...}}`.

## Modules and code map

worker/src/index.ts (`updateTopicMeta`), frontend/src/components/dashboard/index.tsx (`AddTopicPageWithEdit`)

Code anchors that exist: worker/src/index.ts

## Success and acceptance

Returns the updated row; `topic_generation_rules` JSON updated in D1; `Topic not found.` for an id of another tenant (see J-140).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
