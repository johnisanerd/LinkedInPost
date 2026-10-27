---
id: 2026-10-27-j023-backend-unreachable-at-boot
title: J-023 Backend unreachable at boot
status: planned
created: '2026-10-27'
updated: '2026-10-27'
journey_type: user
scope_type: section
scope: frontend
actor: New signed-in user
trigger: Worker URL set but worker down or blocked.
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
external_service: Cloudflare
legacy_id: J-023
---

## Purpose and scope

Backend unreachable at boot. Priority P2, CORE yes. Imported from journey J-023 in docs/launch-readiness/journeys/JOURNEYS.md.

## Actor, trigger and prerequisites

Persona: New signed-in user. Preconditions: Worker URL set but worker down or blocked.

## Steps and information flow

1. Sign in.
2. Wait.

## Modules and code map

frontend/src/App.tsx, frontend/src/services/backendApi.ts (`formatFetchNetworkFailure`)

Code anchors that exist: frontend/src/services/backendApi.ts

## Success and acceptance

After 10 s (`BOOTSTRAP_TIMEOUT_MS`) the screen "Unable to start the session" appears with the message "Unable to reach the backend server. Please check your connection and try again." and the backend host label.

## Failure, edge cases and recovery

Failure behaviour is described in the steps and pass check above. Defects found on this journey are linked from their backlog records (their journeys field names this record).

## Verification evidence

Not verified. Nothing was executed; the journey was derived from reading the code. Status stays planned until the steps are run at a named revision.

## Gaps and linked work

Linked work is derived from the backlog records whose journeys field names this record.

## Next actions

Run the steps on a fresh clone and the pass check; record the outcome in Verification evidence; resolve every linked backlog item before marking verified.
