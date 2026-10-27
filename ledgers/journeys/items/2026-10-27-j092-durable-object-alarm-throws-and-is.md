---
id: 2026-10-27-j092-durable-object-alarm-throws-and-is
title: J-092 Durable Object alarm throws and is retried
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: Queued post; make the publish throw (bad token).
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/scheduled-publish/ScheduledPublishAlarm.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: Cloudflare, LinkedIn
legacy_id: J-092
---

## Purpose and scope

Durable Object alarm throws and is retried. Priority P2, CORE yes. Imported from journey J-092 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: Queued post; make the publish throw (bad token).

## Steps and information flow

1. Let the alarm run; `alarm()` logs "Scheduled LinkedIn publish alarm failed" and rethrows.
2. Observe Cloudflare retry behaviour and the row.

## Modules and code map

worker/src/scheduled-publish/ScheduledPublishAlarm.ts (`alarm`), worker/src/index.ts (`executeScheduledPublish`)

Code anchors that exist: worker/src/scheduled-publish/ScheduledPublishAlarm.ts, worker/src/index.ts

## Success and acceptance

Failure visible somewhere a user can see (row state or banner), no more than N retries, and no duplicate post if a retry occurs after the channel call succeeded but before `markRowPublished`. Current code has no failure status written to the row (CODE-READING FINDING).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
