---
id: 2026-10-27-j053-generate-a-draft-from-the-queue
title: J-053 Generate a draft from the queue (SSE stream)
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: '`GENERATION_WORKER_URL` and `GENERATION_WORKER_SECRET` set on the main worker; a Draft topic; LLM key on the generation worker.'
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
- frontend/src/services/backendApi.ts
- worker/src/index.ts
- generation-worker/src/index.ts
- generation-worker/src/pipeline.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P0
core: 'yes'
external_service: LLM provider, Cloudflare
legacy_id: J-053
---

## Purpose and scope

Generate a draft from the queue (SSE stream). Priority P0, CORE yes. Imported from journey J-053 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: `GENERATION_WORKER_URL` and `GENERATION_WORKER_SECRET` set on the main worker; a Draft topic; LLM key on the generation worker.

## Steps and information flow

1. In `/topics`, open the generate dialog (`GenWorkerDraftField`: Audience chips, Tone, CTA, Constraints) and click Generate.
2. Frontend: `POST {WORKER_URL}/api/generate/stream` with `Authorization: Bearer T`, `Accept: text/event-stream`, body `{"spreadsheetId":"<id>","topicId":"<id>","topic":"...","tone":"...","audience":"...","constraints":"...","llm":{...},"skipImages":true,...}`.
3. Watch progress events (`event: progress` with `{step,label,ts}`), then `event: complete` with `{variants:[{text}], runId, primaryPatternId, ...}`.
4. UI calls `ACTION saveDraftVariants {"row":{...},"variants":["v1","v2","v3","v4"]}`.

## Modules and code map

frontend/src/features/ai-draft/GenWorkerDraftField.tsx, frontend/src/components/dashboard/hooks/useDashboardQueue.ts (`draftWithGenerationWorker`), frontend/src/services/backendApi.ts (`streamCallGenerationWorker`), worker/src/index.ts (`/api/generate/stream`), generation-worker/src/index.ts (`/v1/generate`), generation-worker/src/pipeline.ts

Code anchors that exist: frontend/src/components/dashboard/hooks/useDashboardQueue.ts, frontend/src/services/backendApi.ts, worker/src/index.ts, generation-worker/src/index.ts, generation-worker/src/pipeline.ts

## Success and acceptance

Progress steps tick in the UI, completion alert "Draft generated" with N variants; row now has `variant1..4`; D1 `node_runs` gets rows (30-day TTL) and pattern metadata saved if `topicId` + `primaryPatternId`. Draft text must match topic, tone and rules (criterion 2): spot-check one output against the supplied constraints.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
