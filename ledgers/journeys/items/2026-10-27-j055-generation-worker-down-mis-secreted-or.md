---
id: 2026-10-27-j055-generation-worker-down-mis-secreted-or
title: J-055 Generation worker down, mis-secreted, or LLM error
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: worker
actor: Approved end user
trigger: (a) generation worker stopped, (b) `GENERATION_WORKER_SECRET` != `WORKER_SHARED_SECRET`, (c) invalid LLM key.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- worker/src/index.ts
- generation-worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider, Cloudflare
legacy_id: J-055
---

## Purpose and scope

Generation worker down, mis-secreted, or LLM error. Priority P1, CORE yes. Imported from journey J-055 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: (a) generation worker stopped, (b) `GENERATION_WORKER_SECRET` != `WORKER_SHARED_SECRET`, (c) invalid LLM key.

## Steps and information flow

1. Run J-053 under each condition.

## Modules and code map

worker/src/index.ts, worker/src/generation/ (callGenerationWorkerStream), generation-worker/src/index.ts (`checkAuth`)

Code anchors that exist: worker/src/index.ts, generation-worker/src/index.ts

## Success and acceptance

(a)/(b) main worker returns HTTP 502 `{"ok":false,"error":"Generation worker error: ..."}` and the UI shows `Generation stream error 502: ...`; (c) the SSE carries `event: error` `{message}`; UI shows the message via `handleFailure`; in all cases no row is modified. Unset `GENERATION_WORKER_URL`: HTTP 400 `GENERATION_WORKER_URL is not configured.`

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
