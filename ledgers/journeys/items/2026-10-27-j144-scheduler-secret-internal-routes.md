---
id: 2026-10-27-j144-scheduler-secret-internal-routes
title: J-144 Scheduler-secret internal routes
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Background / agent actor
trigger: '`WORKER_SCHEDULER_SECRET` set (or unset for the negative test).'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- worker/src/automations/routes.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'no'
external_service: other (GitHub Actions / external scheduler)
legacy_id: J-144
---

## Purpose and scope

Scheduler-secret internal routes. Priority P2, CORE no. Imported from journey J-144 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Background / agent actor. Preconditions: `WORKER_SCHEDULER_SECRET` set (or unset for the negative test).

## Steps and information flow

1. `POST {WORKER_URL}/internal/schedule-linkedin-publish` with header `X-Scheduler-Secret: <secret>` and body `{"topicId":"<id>","scheduledTime":"2026-10-28 09:30"}`.
2. `POST {WORKER_URL}/internal/merged-rows` and `/internal/pipeline-upsert` with and without the header.
3. `POST {WORKER_URL}/automations/internal/youtube/poll` body `{"channelId":"UC..."}`.
4. Same with `WORKER_SCHEDULER_SECRET` unset.

## Modules and code map

worker/src/index.ts (`verifySchedulerSecret`, `handleScheduledLinkedInPublishRequest`, `handleInternalMergedRowsRequest`, `handleInternalPipelineUpsertRequest`), worker/src/automations/routes.ts

Code anchors that exist: worker/src/index.ts, worker/src/automations/routes.ts

## Success and acceptance

Wrong/missing header -> 401 `Unauthorized scheduler request.`; with the secret unset every request is refused (`if (!expectedSecret || ...)`). The first route publishes using the global KV LinkedIn config only (not per-tenant). Compare the secret in constant time (current code uses `!==`).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
