---
id: 2026-10-27-j056-send-to-generation-button-on-a
title: J-056 "Send to Generation" button on a saved Draft topic
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: A topic with status `Draft` and no variants (the card shows "Saved draft" with "Send to Generation").
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/services/backendApi.ts
- worker/src/index.ts
- worker/migrations/0001_pipeline_init.sql
- worker/migrations/0010_pipeline_user_primary.sql
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: Cloudflare, LLM provider
legacy_id: J-056
---

## Purpose and scope

"Send to Generation" button on a saved Draft topic. Priority P1, CORE yes. Imported from journey J-056 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: A topic with status `Draft` and no variants (the card shows "Saved draft" with "Send to Generation").

## Steps and information flow

1. Click "Send to Generation" (`TopicPostPreviewCard`).
2. Frontend: `POST {WORKER_URL}/` body `{"action":"sendTopicToGeneration","idToken":"T","payload":{"topicId":"<id>"}}` with `Accept: text/event-stream`.
3. Observe the response and the row afterwards.
- CODE-READING FINDING 1: after a successful generation-worker response the handler runs `UPDATE pipeline_rows SET status = 'Pending' ...`; there is no table `pipeline_rows` in any migration (the table is `pipeline_state`), so D1 throws and the request ends as HTTP 400 with a D1 error while the generation worker has already started.
- CODE-READING FINDING 2: even if that SQL worked, the SSE relay in this branch only forwards blocks; unlike `/api/generate/stream` it never calls `saveDraftVariants`, and `TopicPostPreviewCard` only checks `response.ok` and navigates without reading the body, so generated variants are never stored.

## Modules and code map

frontend/src/components/dashboard/components/TopicPostPreviewCard.tsx, frontend/src/services/backendApi.ts (`sendTopicToGeneration`), worker/src/index.ts (`sendTopicToGeneration` block), worker/migrations/0001_pipeline_init.sql, worker/migrations/0010_pipeline_user_primary.sql

Code anchors that exist: frontend/src/services/backendApi.ts, worker/src/index.ts, worker/migrations/0001_pipeline_init.sql, worker/migrations/0010_pipeline_user_primary.sql

## Success and acceptance

Desired: Row moves Draft -> Pending -> has 4 variants and the UI shows them on `/topics/:topicId`. Currently expected to FAIL.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
