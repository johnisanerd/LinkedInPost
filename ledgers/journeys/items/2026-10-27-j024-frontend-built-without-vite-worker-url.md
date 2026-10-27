---
id: 2026-10-27-j024-frontend-built-without-vite-worker-url
title: J-024 Frontend built without `VITE_WORKER_URL`
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: workflow
scope_type: section
scope: frontend
actor: Self-hosting operator
trigger: Build with empty `VITE_WORKER_URL`.
verification_owner: unassigned (owner to set)
source_revision: null
checked_at: null
modules: &id001
- frontend/src/services/backendApi.ts
code_paths: *id001
related: []
docs:
- docs/launch-readiness/journeys/JOURNEYS.md
priority: P2
core: 'yes'
external_service: none
legacy_id: J-024
---

## Purpose and scope

Frontend built without `VITE_WORKER_URL`. Priority P2, CORE yes. Imported from journey J-024 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: Self-hosting operator. Preconditions: Build with empty `VITE_WORKER_URL`.

## Steps and information flow

1. Open the app signed out.

## Modules and code map

frontend/src/App.tsx, frontend/src/services/backendApi.ts (`normalizeWorkerApiUrl`, `isConfigured`)

Code anchors that exist: frontend/src/services/backendApi.ts

## Success and acceptance

Screen "Backend URL required" with the instruction to set `VITE_WORKER_URL`; no network calls are made. A relative value (e.g. `/topics`) is rejected by `normalizeWorkerApiUrl` and shows the same screen.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
