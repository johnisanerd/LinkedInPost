---
id: 2026-10-27-j054-network-drop-in-the-middle-of
title: J-054 Network drop in the middle of the generation stream
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: Approved end user
trigger: Generation in progress.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/services/backendApi.ts
- frontend/src/components/dashboard/hooks/useDashboardQueue.ts
- worker/src/index.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P1
core: 'yes'
external_service: LLM provider
legacy_id: J-054
---

## Purpose and scope

Network drop in the middle of the generation stream. Priority P1, CORE yes. Imported from journey J-054 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Approved end user. Preconditions: Generation in progress.

## Steps and information flow

1. Start J-053.
2. Toggle the browser offline (DevTools) after the first progress event; also try closing the laptop lid / switching Wi-Fi.
3. Go back online.

## Modules and code map

frontend/src/services/backendApi.ts (`streamCallGenerationWorker`), frontend/src/components/dashboard/hooks/useDashboardQueue.ts, worker/src/index.ts (stream relay)

Code anchors that exist: frontend/src/services/backendApi.ts, frontend/src/components/dashboard/hooks/useDashboardQueue.ts, worker/src/index.ts

## Success and acceptance

The async generator ends (or the `reader.read()` rejects) without a `complete` event; `draftWithGenerationWorker` then throws `Generation worker returned an invalid response (missing variants).` and `handleFailure` shows an alert; progress UI clears (`finally`). No partial variants are saved. Verify the topic stays `Draft` and the user can retry; also confirm the worker keeps running the pipeline and charges LLM tokens after the client left (the server loop only stops when the writer errors).

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
